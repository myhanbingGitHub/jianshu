import pymysql

cnn= pymysql.connect(
    host='localhost',user='root',password='Hukecld8010',database='forscrapy'
)
cursor= cnn.cursor()

try:
    sql="insert into article (title,name,url,collection) values (%s,%s,%s,%s)"
    cursor.execute(sql,("标题","作者名字","网页地址","收录专题"))
    cnn.commit()
except:
    cnn.rollback()
finally:
    cursor.close()
    cnn.close()





