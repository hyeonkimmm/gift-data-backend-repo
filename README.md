# gift-data-backend-repo
**네이버 쇼핑 데이터 활용 선물 추천 프로젝트 입니다.**  
데이터 엔지니어링 & 백엔드 저장소입니다.


## TODO
### 1. 네이버 쇼핑 데이터 로컬에 저장 (크롤링 or 네이버 쇼핑&검색 API 활용)
  - 연령
  - 성별
  - 금액
  - 추후 추가 ... 
  - 자동화 (Airflow)  
### 2. 저장된 데이터 pands or spark 을 통한 데이터 처리
  - pands -> 스몰 데이터 위추
  - spark -> 분산 처리 필요..?
  - parquet - columnar 데이터 타입 활용 고려  
### 3. 데이터 베이스 스키마 설계 + DB 사용 플랫폼 고려 (AWS RDS, 파이어베이스, Repl DB, Heroku Postgres)
  - 추가로 서버리스로 갈건지 어떻게 할지 고민
  - 앱 개발 속도에 맞춰 추가 기능 구현 고려  
### 4. REST API 개발
  - 프레임워크 고민 (Django & Flask & Fast Api ...?)
  - DB Connect 코드
  - 앱에 뿌려줄 API 설계
  - 코드 작성 및 테스트
  - 배포

---
## Requirement
- Python 3.9
- pandas==1.4.1
