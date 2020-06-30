# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 14:49:24 2020

@author: jangi
"""


import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost', port=3306, user='root', password='!j39273927', db='db_201310805', charset='utf8', local_infile = 1)

curs=conn.cursor(pymysql.cursors.DictCursor)

################ 유저 테이블에 데이터 넣기

#sql = "load data local infile 'C:/Users/jangi/movielens dataset/u.user.tsv' ignore into table users fields terminated by '|' lines terminated by '\n'"

###########################################


############################### 영화테이블에 데이터 넣기

#data=pd.read_csv("C:/Users/jangi/movielens dataset/u.item.tsv", sep = "|", encoding = 'ISO-8859-1')
#data2=data[['1', 'Toy Story (1995)', '01-Jan-1995', 'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)']]
#data2.to_csv("C:/Users/jangi/movielens dataset/u.item2.tsv", index = None, sep='|')
#sql = "load data local infile 'C:/Users/jangi/movielens dataset/u.item2.tsv' ignore into table movie fields terminated by '|' lines terminated by '\n'"

################################


################################### 영화장르 테이블에 데이터 넣기
'''
data=pd.read_csv("C:/Users/jangi/movielens dataset/u.item.tsv", sep = "|", names=[ 'movie_title', 'release_date', 'IMDb URL', 'unknown', 'Action', 'Adventure','Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'], encoding = 'ISO-8859-1')
data2=data[['unknown', 'Action', 'Adventure','Animation', 'Childrens', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']]
 
count=0

for i in data2.index:        

    count+=1
    
    genre=[]
    
    real_genre=[]
    
    
    if(data2.loc[i,'unknown'])==1:
        genre.append('unknown')
    if(data2.loc[i,'Action'])==1:
        genre.append('Action')
    if(data2.loc[i,'Adventure'])==1:
        genre.append('Adventure')
    if(data2.loc[i,'Animation'])==1:
        genre.append('Animation')
    if(data2.loc[i,'Childrens'])==1:
        genre.append('Childrens')
    if(data2.loc[i,'Comedy'])==1:
        genre.append('Comedy')
    if(data2.loc[i,'Crime'])==1:
        genre.append('Crime')
    if(data2.loc[i,'Documentary'])==1:
        genre.append('Documentary')
    if(data2.loc[i,'Drama'])==1:
        genre.append('Drama')
    if(data2.loc[i,'Fantasy'])==1:
        genre.append('Fantasy')
    if(data2.loc[i,'Film-Noir'])==1:
        genre.append('Film-Noir')
    if(data2.loc[i,'Horror'])==1:
        genre.append('Horror')
    if(data2.loc[i,'Musical'])==1:
        genre.append('Musical')
    if(data2.loc[i,'Mystery'])==1:
        genre.append('Mystery')
    if(data2.loc[i,'Romance'])==1:
        genre.append('Romance')
    if(data2.loc[i,'Sci-Fi'])==1:
        genre.append('Sci-Fi')
    if(data2.loc[i,'Thriller'])==1:
        genre.append('Thriller')
    if(data2.loc[i,'War'])==1:
        genre.append('War')
    if(data2.loc[i,'Western'])==1:
        genre.append('Western')
    
        
    
    real_genre = ",".join(str(v) for v in genre)
    real_genre.lstrip('[]')
    real_genre.rstrip('[]')

    
    
    sql = """INSERT INTO movie_genre (Movie_id, Genre) VALUES (%s, %s) """
    insert_data=(count, real_genre)
    curs.execute(sql,insert_data)  
    
'''

################################### data테이블에 데이터 넣기

sql = "load data local infile 'C:/Users/jangi/movielens dataset/u.data.tsv' ignore into table datas fields terminated by '\t' lines terminated by '\n'"

########################################

curs.execute(sql)

conn.commit()

curs.close()
conn.close()