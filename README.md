# 유사도 검사를 통한 문서 추천 프로그램 개발

## 0. 사용한 개념 및 환경
Python
numpy, pandas
sklearn
selenium
konlpy
cosine similarity

## 1. 뉴스 크롤링

네이버 뉴스 예시 이미지
![image](https://user-images.githubusercontent.com/57586314/120138757-1b690780-c212-11eb-8257-15c4f384a49d.png)

네이버 중앙일보 뉴스 약 800개 크롤링 - 제목과 내용


## 2. 제목에 해당하는 문서 출력
데이터 예시
![image](https://user-images.githubusercontent.com/57586314/120139286-1b1d3c00-c213-11eb-8053-b41c5931a9dd.png)
정규표현식을 활용해 데이터 cleaning 후, csv형식으로 제목 내용 저장

## 3. 문서와 유사도가 높은 다른 문서 출력
tf-idf
![image](https://user-images.githubusercontent.com/57586314/120139649-dc3bb600-c213-11eb-8e9b-30346821e85e.png)
TF(term frequency)는 단어빈도로 특정한 단어가 문서 내에 얼마나 자주 등장하는지를 나타내는 값으로, 이 값이 높을수록 문서에서 중요하다고 판단한다. 하지만 하나의 문서에서 많이 나오지 않고 다른 문서에서 자주 등장하면 단어의 중요도는 낮아지는데, 이를 DF(document frequency)문서 빈도라고 하며 이 값의 역수를 IDF(inverse document frequency)라고 한다. 이 TF-IDF를 곱한 값이 높을수록 다른 문서에는 많지 않고 해당 문서에서 자주 등장하는 단어로 의미한다.


## 4. 단어 빈도 수 계산 후, 빈도 높은 문서 리스트 출력 및 단어 TOP랭킹 출력

## 5. json형식으로 단어 사전 만들기
