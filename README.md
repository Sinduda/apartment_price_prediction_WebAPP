# 다중선형회귀 모델을 통한 서울 아파트 가격 예측 웹앱 배포
### (코드스테이츠 데이터 엔지니어링 섹션 개인 프로젝트)
- 진행 기간: 6월 22일 ~ 6월 26일
- 사용 언어: `Python`,`MySQL`
- **프로젝트 발표 영상**은 [여기](https://youtu.be/eXWBu-wuSBw)에서 보실 수 있습니다.
- 아래 내용은 [노션 페이지](https://inhwan-hwang.notion.site/Transformer-c9f48d8ca85c401d8324fa872fae7938)에서 좀 더 편하게 읽으실 수도 있습니다.

---

<br/>

## **프로젝트 개요**

다중선형회귀 모델을 통한 **서울 아파트 가격 예측 웹앱 배포**

> 👉🏻  *원하는 아파트 조건(평수/연식/층수)을 입력하면 가격을 예측해주는 웹 API 서비스 개발 및 배포.*
> 
> 
> `#엔지니어링`, `#DB구축부터_서비스_배포까지`,`#데이터_파이프라인_구축`
> 
> ---
> 
> 서버형 로컬 DB를 구축해 데이터를 저장하고, 적재된 데이터를 활용해 ML 모델을 포함한 서비스를 개발 및 배포하기까지의 파이프라인을 구축하는 프로젝트입니다. 
> 
> 1. 직방의 [아파트 실거래가 예측](https://dacon.io/competitions/official/21265/data) 데이터를 `PyMySQL`을 이용하여 MySQL에 적재하였습니다.
> 2. `SQLAlchemy`를 이용하여 적재 데이터를 통해 아파트 가격을 예측해주는 머신러닝 모델을 만들고, 이 모델을 `Pickling` 하였습니다.
> 3. Flask를 사용하여 훈련된 ML 모델을 serving하고, Heroku를 통해 서비스를 배포하였습니다.
> 4. MeteBase를 사용하여 데이터 분석 시각화 및 대시보드를 제공하였습니다. 
>     
>     *(Docker 사용, 로컬 환경에서만 동작)*
>     
> 
> 🏠 [[Web APP] 서울 아파트 가격 예측, 자꿈, 서비스 웹앱 링크](https://aiproject3.herokuapp.com/)
> 
> ---
> 
- **서비스 파이프라인**은 아래와 같습니다.
  <img width="1132" alt="pipline" src="https://user-images.githubusercontent.com/81467922/184500541-8c921950-6f8f-4e10-a591-5c4d1ee31bd2.png">    
- 서비스 핵심 기능의 모습은 아래와 같습니다.
  <img width="1080" alt="corefunc" src="https://user-images.githubusercontent.com/81467922/184500553-44728948-ba93-41dd-a4cc-23401f7a00d8.png">

<br/>

## **문제 정의**

**[문제 상황]**

- 최근 10여년 간 아파트 가격의 상승으로 인해 내 집 마련이 점점 어려워지고 있습니다.
- 특히 서울 지역의 경우 중위 소득 가구 기준으로 중간 가격대의 아파트를 구매하기 위해서 월급을 한 푼도 쓰지 않고 18.4년을 모아야 하는 것으로 나타나는 등 **내 집 마련을 위한 장기적인 자금 계획 수립이 필수적인 상황**입니다.
    
    *(출처: 뉴시스 “서울서 내 집 마련 18.4년 걸려…전세자금도 9.8년 모아야” (22.05)*
    
- 장기적인 자금 계획 수립을 위해서는 **‘내가 원하는 조건의 아파트가 어느 정도의 가격일지'**를 예측하는 것이 가장 중요한 시작이라고 생각하였습니다.

즉, 이번 프로젝트는 **내가 원하는 조건의 아파트 가격이 얼마일지 알고 자금 계획 때 활용할 수 있으면 좋겠다**는 것으로부터 시작되었습니다.

<br/>

**[기존 서비스의 문제점]**

- 본격적으로 시작하기에 앞서, 현재 이런 목적을 달성하기 위한 서비스는 없는지 가장 먼저 확인해보았습니다.
- 실제로 ‘네이버 부동산’ 등에 가면 아래와 같이 다양한 조건에 따라 매물 정보 확인이 가능합니다.
    <img width="1138" alt="naver" src="https://user-images.githubusercontent.com/81467922/184500685-98bffbfc-013e-4453-9b74-b99060cd1adf.png">
- 그러나 저는 기존 서비스로부터 아래 두 가지 문제점을 발견하였습니다.
    1. 현재 매물로 나온 정보만 확인 가능하다는 점. 매물 가격은 실거래 가격이 아니라서 정확한 예측이 어렵다.
    2. ‘현재'만을 기준으로 하고 있어 조건별 오랜 기간의 전반적인 매매가 트렌드를 보기 어렵다.
- 소비자가 장기적 자금 마련 계획이라는 소기의 목표를 달성하기 위해 기존 서비스에는 불편함이 존재하는 것입니다.

<br/>

## **사용한 데이터셋**

**[필요한 데이터셋]**

- ML 모델 학습을 위한 서울 지역 아파트 실제 매매 가격 데이터.
- 해당 데이터에는 가격 뿐 아니라 평수, 연식 등의 다양한 조건을 포함하고 있어야 함.

<br/>

**[선정한 데이터셋]**

- 직방에서 제공한 **[아파트 실거래가 예측](https://dacon.io/competitions/official/21265/overview/description)** 데이터셋을 모델 학습 데이터로 선정하였습니다.
        - 거래 지역, 면적, 완공년도, 층수, 매매가 등의 정보가 포함된 샘플을 약 160만 건 포함하고 있습니다.
    - 데이터셋을 EDA 해본 결과, 결측치 및 이상치가 없는 이상적인 데이터라 판단해 최종 선정하였습니다.
- 160만 건의 샘플 중에서 ML 모델 학습에는 **서울 지역 거래 데이터 1만 건**을 무작위 추출하여 사용했습니다.
    - 이유
        - 이번 프로젝트에서 시계열 예측은 목표 범위가 아님.
        - ML 모델의 높은 성능보다는 빠른 학습이 우선시 됨.
        
<br/>

## **데이터 저장**

[**데이터의 적재]**

- 서버형 로컬 DB인 `MySQL`에 저장하였는데, 이때 `PyMySQL` 라이브러리를 사용하였습니다.
    - (로컬 DB 생성 과정은 기록 생략)
    
    ```python
    # 로컬 DB에 데이터 적재하기
    
    import pandas as pd
    import pymysql
    
    df = pd.read_csv('data.csv', encoding = 'utf-8')
    
    # db 연결
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='0000', db='project3_db', charset='utf8')
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
    ```
    
<br/>

## ML 모델 개발

**[모델 선택]**

- 이번 서비스에 사용할 ML 모델로는 `다중선형회귀` 모델을 선택하였습니다.
- **이번 프로젝트의 목표는 전체적인 데이터 파이프라인을 구축해보는 것으로, ML 모델이 높은 성능을 내도록 하는 것은 주목표가 아니었습니다.**
    - 따라서 가장 빠르게 구축할 수 있는 선형 회귀 모델을 선택했으며, 하이퍼 파라미터 최적화 등의 작업은 이번 프로젝트 간 수행하지 않았습니다.

**[진행 과정]**

1. DB에 저장되어 있는 데이터를 가져와 학습시키기 위해 `SQLAlchemy` 라이브러리를 이용하였습니다. 
2. 추후 웹 앱에서 해당 모델을 사용하기 위해 피클링(Pickling) 하였습니다. (= 모델 인코딩)

<br>

## API 서비스 개발 및 배포

**[API 서비스 개발]**

- 웹 어플리케이션 개발은 `Flask`를 이용하여 진행하였습니다.
- 이 과정에서 피클링했던 ML 모델을 디코딩하였고(=언피클링),
- 사용자가 입력한 조건*(평수/연식/층수)*에 대한 아파트 가격의 예측값을 출력하도록 구성하였습니다.

**[배포]**

- `Heroku`를 통해 로컬 뿐 아니라 다른 환경에서도 웹 접속이 가능하도록 배포까지 진행하였습니다.
    
    🏠 [[Web APP] 서울 아파트 가격 예측, 자꿈, 서비스 웹앱 링크](https://aiproject3.herokuapp.com/)
    

**[Metabase 대시보드 임베딩]**

- `Metabase` 라는 BI툴을 Docker를 통해 접속하고, 구축한 DB를 연결하여 대시보드를 만들고 웹에 반영하였습니다. 
- 하지만 Docker를 통해  `Metabase` 를 사용하면, 로컬 환경에서만 임베딩된 대시보드를 볼 수 있었습니다. 대시보드까지 배포할 수 없었다는 점이 아쉬운 점으로 남았습니다.

<br/>

## **한계점 및 향후 목표**

이번 프로젝트의 포커스가 **전체적인 데이터 파이프라인을 구축해보는 것**으로 맞춰져 있었기에, ML 모델과 관련해 아쉬운 점이 많이 남습니다.

1. 가장 기본적인 선형회귀 모델을 사용하였는데, 좀 더 정확한 예측이 가능하도록 모델 최적화 필요.
2. 데이터를 추가 확보해 서울 지역 뿐 아니라 다른 지역에도 + 아파트 외에도 다른 주택 유형에도 서비스 확장.
3. 최근 10년 매매 데이터를 한 번에 전체 활용했는데, 추후 시계열 분석까지도 진행해보면 좋을 것 같음.

또한 Metabase를 통해 구축한 대시보드 항목을 좀 더 다양화하여, 서비스를 이용하는 고객이 좀 더 많은 인사이트를 얻어갈 수 있도록 하는 것도 추후 진행해볼만 한 점이라고 생각합니다.

<br/>

## **프로젝트 회고**

- 이번 프로젝트를 완료한 직후 작성한 회고 글은 아래에서 읽어보실 수 있습니다.

[220622-0626 데이터 엔지니어링 개인 프로젝트 회고](https://velog.io/@cualquier/220622-0626-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4%EB%A7%81-%EA%B0%9C%EC%9D%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0)
