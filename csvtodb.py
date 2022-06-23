import pandas as pd
import pymysql

df = pd.read_csv('data.csv', encoding = 'utf-8')

# db 연결
conn = pymysql.connect(host='localhost', port=3306, user='root', password='4889', db='project3_db', charset='utf8')
cur = conn.cursor()

# 테이블 생성
cur.execute("DROP TABLE IF EXISTS mydata;") #python 파일 재실행하면 기존 데이터 지워지도록. 작업의 편의성을 위함.

cur.execute("""CREATE TABLE mydata(
    transaction_id INT,
    apartment_id INT, 
    city varchar(50), 
    dong varchar(50), 
    jibun varchar(50), 
    apt varchar(50), 
    addr_kr varchar(50), 
    exclusive_use_area FLOAT, 
    year_of_completion INT, 
    transaction_year_month INT, 
    transaction_date varchar(50), 
    floor INT, 
    transaction_real_price INT,
    PRIMARY KEY(transaction_id)
)
""")


# 적용할 쿼리문
sql = """INSERT INTO mydata(transaction_id, apartment_id, city, dong, jibun, apt, addr_kr, exclusive_use_area, year_of_completion, transaction_year_month, transaction_date, floor, transaction_real_price)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

# 데이터 import
for idx in range(len(df)): 
    cur.execute(sql, tuple(df.values[idx]))

# 적용
conn.commit()

conn.close()