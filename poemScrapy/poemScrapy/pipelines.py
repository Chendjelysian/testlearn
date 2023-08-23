# import json
#
# class PoemscrapyPipeline:
#     def __init__(self):
#         # 打开文件
#         self.file = open('data.txt', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         # 读取item中的数据
#         line = json.dumps(dict(item), ensure_ascii=False) + '\n'
#         # 写入文件
#         self.file.write(line)
#         return item

from itemadapter import ItemAdapter
import json
import pymysql


class PoemscrapyPipeline:
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',  # 设置成用户自己的数据库密码
            db='poem',
            charset='utf8'
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 写入数据库
        self.cursor.execute(
            'INSERT INTO beautifulsentence(source,sentence,content,url) VALUES ("{}","{}","{}","{}")'.format(
                item['source'], item['sentence'], item['content'], item['url']))
        self.connect.commit()
        return item


def close_spider(self, spider):
    # 关闭数据库连接
    self.cursor.close()
    self.connect.close()
