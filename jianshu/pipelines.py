# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class JianshuPipeline:
    # 初始化类,定义自己的属性: self.cnn, self.cur
    def __init__(self):
        cnn_param={
            'host':'localhost',
            'port':3306,
            'user':'root',
            'password':'Hukecld8010',
            'database':'forscrapy',
            'charset':'utf8'
        }
        self.cnn= pymysql.connect(**cnn_param)
        self.cur=self.cnn.cursor()

    # 数据入库
    def process_item(self,item,spider):
        try:
            sql = "insert into article (title,name,url,collection) values (%s,%s,%s,%s)"
            self.cur.execute(sql, (item['title'],
                                   item['name'],
                                   item['url'],
                                   item['collection']))
            self.cnn.commit()   # 默认是需要手工提交
            print("入库成功！")
        except:
            self.cnn.rollback()
            print("入库失败！")


        return item
