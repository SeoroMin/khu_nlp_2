# 유사도 검사를 통한 문서 추천 프로그램 개발

## 0. 사용한 개념 및 환경
Python <br>
numpy, pandas <br>
sklearn <br>
selenium <br>
konlpy <br>
cosine similarity <br>

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

Cosine similarity
![image](https://user-images.githubusercontent.com/57586314/120140386-6afd0280-c215-11eb-84f9-c73f8d700794.png)
![image](https://user-images.githubusercontent.com/57586314/120140461-9384fc80-c215-11eb-9be7-64762bbefd16.png)

코사인 유사도란 벡터와 벡터 간의 유사도를 비교할 때, 두 벡터 간의 사잇각을 구해 얼마나 유사한지 수치로 나타낸 것이다. 벡터 방향이 비슷할수록 두 벡터는 서로 유사하다. 이 프로젝트에서는 벡터가 문서의 TF-IDF값이 되며 두 문서간의 유사도를 구하는 측정 방법을 코사인 유사도를 통해 구한다.

## 4. 단어 빈도 수 계산 후, 빈도 높은 문서 리스트 출력 및 단어 TOP랭킹 출력

1) 단어의 빈도를 konlpy의 Okt를 통해 구한다. (nouns 명사기준) <br>
2) 단어를 입력받아 빈도수가 높은 문서 리스트 출력(내림차순 정렬)
3) 해당 문서를 입력받아 접속
4) 문서에서 명사 단위 추출 후 단어 빈도 계산
5) 빈도 상위 10개 출력

## 5. json형식으로 단어 사전 만들기

단어를 json형식으로 만들어 단어 사전 만든다. 중복된 것을 제거하고 고유값들에 key값을 부여해 dict형식으로 저장 후 json파일로 저장한다.
