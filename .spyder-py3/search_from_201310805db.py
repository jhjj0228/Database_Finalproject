# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:26:00 2020

@author: jangi
"""


import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='!j39273927', db='db_201310805', charset='utf8', local_infile = 1)

curs=conn.cursor(pymysql.cursors.DictCursor)



def UserInterface():

    genre = input("장르를 입력하세요 : ")
    occupation = input("사용자의 직업은 무엇입니까 : ")
    print ("=============평점 ============= ")
    min = input("min rating : ")
    max = input("max rating : ")
    sort = input("sorting by:")
    sql = MakeSql(genre,occupation,min,max,sort)
    executeSql(sql)


def MakeSql(genre, occupation, min, max, sort):

#    """
    sql = """SELECT d.Movie_id, m.Movie_title, g.Genre, AVG(d.Rating), count(d.User_id)
    FROM datas d
    JOIN movie m ON d.Movie_id = m.Movie_id
    JOIN movie_genre g ON m.Movie_id = g.Movie_id
    JOIN users u ON d.User_id = u.User_id
    
    """
    
  
    
    if genre != "":
        sql += """and g.Genre = '%s' """%(genre)

    if occupation != "":
        sql += """and u.occupation = '%s' """%(occupation)

    sql += """\ngroup by d.Movie_id """

    if min != "":
        sql += """\nhaving AVG(d.rating) >= %f """%(float(min))
    else :
        min=0
        sql += """\nhaving AVG(d.rating) >= 0 """
    if max != "":
        sql += """and AVG(d.rating) <= %f """%(float(max))


    if sort != "":
        if sort == "영화제목":
            sql += """\norder by m.Movie_title asc """
        elif sort == "평균평점":
            sql += """\norder by AVG(d.Rating) desc"""
        elif sort == "투표수":
            sql += """\norder by (count(d.User_id)) asc """
    return sql


def executeSql(sql):
    curs.execute(sql)

    row = curs.fetchone()
    
    print("\n[Movie_id]        [Movie_title]       [Genre]     [rating]    [투표수]")
    while row:
        print("%d  |%s  |%s  |%f  |%d"
              % (row['Movie_id'], row['Movie_title'], row['Genre'], row['AVG(d.Rating)'], row['count(d.User_id)']))
        row = curs.fetchone()
    curs.close()
    conn.close()


UserInterface()
