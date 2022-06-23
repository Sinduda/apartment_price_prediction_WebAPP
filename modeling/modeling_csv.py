# -----모델 생성 - CSV 파일 읽어오는 버전 ----- #
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv', encoding = 'utf-8')

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

print('예측 가격 = ', y_pred[0][0], '만원')