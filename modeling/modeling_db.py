# -----모델 생성 - MySQL에서 불러와서 사용하는 버전----- #
import pandas as pd
from sklearn.linear_model import LinearRegression
import pymysql
pymysql.install_as_MySQLdb() # reference - http://i5on9i.blogspot.com/2020/05/no-module-named-mysqldb.html
from sqlalchemy import create_engine

# MySQL의 데이터를 데이터프레임으로 가져오기
engine = create_engine('mysql://root:0000@localhost/project3_db')
conn = engine.connect()

df = pd.read_sql_table('mydata', conn)

# 쓸 칼럼만 선택
df = df[['exclusive_use_area', 'year_of_completion', 'floor', 'transaction_real_price']]

# 객체 생성
model = LinearRegression()

# 데이터 구분 
target = ['transaction_real_price']
X_train = df.drop(columns = target)
y_train = df[target]

# 학습
model.fit(X_train, y_train)

# 예측
X_test = [[90, 2002, 6]]
y_pred = model.predict(X_test)

print('예측 가격 = ', round(y_pred[0][0]), '만원')

### ----- pickling ----- ###

import pickle

with open('model.pkl', 'wb') as pickle_file:
    pickle.dump(model, pickle_file)