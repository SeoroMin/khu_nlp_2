from flask import Flask, json, render_template, request, jsonify
import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from konlpy.tag import Okt 
from collections import Counter

app = Flask(__name__)

file = r'C:\Users\tkdal\Desktop\project\data_746.csv'

# 데이터 불러오기
df = pd.read_csv(file)

# 데이터 cleaning
df["내용"] = df["내용"].str.replace(pat=r'[^\w]', repl=r' ', regex=True)

@app.route('/')
def hello_world():

    df_title = df[['제목', '내용']].head(10)

    return df_title.to_html()

@app.route('/test')
def test():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():

    value = request.form['test']

    title = df[df['제목'] == value]

    return title.to_html()

@app.route('/test2')
def test2():
    return render_template('post.html')

@app.route('/post2', methods=['POST'])
def post2():

    value2 = request.form['test2']

    # overview에 대해서 tf-idf 수행
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['내용'])

    # title = df[df['제목'] == value]

    # 선택한 뉴스의 타이틀로부터 해당되는 인덱스를 받아옵니다. 선택한 뉴스를 가지고 연산.
    indices = pd.Series(df.index, index=df['제목']).drop_duplicates()
    idx = indices[value2]

    # 모든 뉴스에 대해서 해당 뉴스와의 유사도 구하기
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 뉴스들을 정렬합니다.
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # 가장 유사한 10개의 뉴스를 받아옵니다.
    sim_scores = sim_scores[1:11]

    # 가장 유사한 10개의 뉴스의 인덱스를 받아옵니다.
    news_indices = [i[0] for i in sim_scores]

    # 가장 유사한 10개의 뉴스의 제목을 리턴합니다.
    si = df[['제목', '내용']].iloc[news_indices]

    return si.to_html()

@app.route('/test3')
def test3():
    return render_template('post.html')

@app.route('/post3', methods=['POST'])
def post3():
    
    # 단어 입력
    word = request.form['test3']

    okt=Okt()
    
    # 제일 빈도가 높은 단어, 개수 column에 추가
    most_1_word_list = []
    most_1_count_list = []
    
    for i in range(len(df)):
        corpus = df['내용'][i]
        noun = okt.nouns(corpus)
        count = Counter(noun)
        most_1_word = count.most_common(1)[0][0]
        most_1_count = count.most_common(1)[0][1]
        most_1_word_list.append(most_1_word)
        most_1_count_list.append(most_1_count)
        
    df['top1'] = most_1_word_list
    df['top1_count'] = most_1_count_list
    
    # 검색한 단어에 맞는 dataframe 생성
    search_list = df[df['top1'] == word]
    
    # 빈도수가 높은 순으로 정렬
    count_sort = search_list.sort_values(by=['top1_count'], axis=0, ascending=False)
    
    # 검색한 단어가 가장 많이 출현한 문서 리스트 출력
    print("문서 출력 : ", count_sort['제목'])
    
    # 제목 입력
    title = request.form['test4']
    
   
    # overview에 대해서 tf-idf 수행
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['내용'])
    
    # 선택한 뉴스의 타이틀로부터 해당되는 인덱스를 받아옵니다. 선택한 뉴스를 가지고 연산.
    indices = pd.Series(df.index, index=df['제목']).drop_duplicates()
    idx = indices[title]
    
    # 선택한 뉴스의 내용 저장
    corpus = df['내용'][idx]
    
    # 명사 단위 추출 , 형태소 -> okt.morphs()
    noun = okt.nouns(corpus)

    # 단어 빈도 계산
    count = Counter(noun)

    return count_sort[['제목', '내용']], count.most_common(10)


if __name__ == '__main__':
    app.run()