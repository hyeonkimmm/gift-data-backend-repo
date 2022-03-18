# gift-data-backend-repo
**네이버 쇼핑 데이터 활용 선물 추천 프로젝트 입니다.**  
데이터 엔지니어링 & 백엔드 저장소입니다.

## TODO
### 1. 네이버 쇼핑 데이터 로컬에 저장 (크롤링 or 네이버 쇼핑&검색 API 활용)
[crawl_ranking_info.py](https://github.com/hyeonkimmm/gift-data-backend-repo/blob/main/extract/crawl_ranking_info.py)
  - 연령
  - 성별
  - 금액
  - 추후 추가 ... 
  - robots.txt 기준에 맞춰 규정 준수
### 2. 저장된 데이터 pands or spark 을 통한 데이터 처리
[스코어 계산 코드 update_score.py](https://github.com/hyeonkimmm/gift-data-backend-repo/blob/main/update_score.py)
  - pands -> 스몰 데이터 위주
  - spark -> 분산 처리 필요? 로컬에서 학습용으로 진행
  - parquet - columnar 데이터 타입 활용 고려  
### 3. 데이터 베이스 스키마 설계 + DB 사용 플랫폼 고려 (AWS RDS, 파이어베이스, Repl DB, Heroku Postgres)
[파이어베이스로 결정](https://github.com/hyeonkimmm/gift-data-backend-repo/issues/3)   
[데이터베이스 스키마 설계](https://github.com/hyeonkimmm/gift-data-backend-repo/issues/5)   
[파이어스토어 업데이트 코드 update_firestore.py](https://github.com/hyeonkimmm/gift-data-backend-repo/blob/main/firebase/update_firestore.py)   
  - 앱 개발 속도에 맞춰 추가 기능 구현 고려
  - ETL 전체 자동화 코드(Airflow ?)

--- 
### 4. REST API 개발(여력이 남는다면 진행)
  - 프레임워크 고민 (Django & Flask & Fast Api ...?)
  - DB Connect 코드
  - 앱에 뿌려줄 API 설계
  - 코드 작성 및 테스트
  - 배포

---
## Requirement
- Python 3.9
- pandas==1.4.1
- bs4==0.0.1
- requests==2.27.1
- selenium==4.1.0
- firebase-admin==5.2.0
---
## Coding convention python
- PEP8 (flake8)
- flake8==4.0.1
- https://lintlyci.github.io/Flake8Rules/

## 결과 화면
![1차 결과 화면](https://user-images.githubusercontent.com/43769123/158948073-40e12505-85b5-41f8-b30a-05e6beeeb017.png)
