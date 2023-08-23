# consumer_json.py
from kafka import KafkaConsumer
import json
import pymysql.cursors

consumer = KafkaConsumer('json_topic', bootstrap_servers=['localhost:9092'], group_id=None,
                         auto_offset_reset='earliest')
for msg in consumer:
    msg1 = str(msg.value, encoding="utf-8")  # 字节数组转成字符串
    dict = json.loads(msg1)  # 字符串转换成字典
    # 连接数据库
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',  # 数据库用户名
        passwd='123456',  # 密码
        db='school',
        charset='utf8'
    )

    # 获取游标
    cursor = connect.cursor()

    # 插入数据
    sql = "INSERT INTO student(sno,sname,ssex,sage) VALUES ('%s', '%s', '%s', %d)"
    data = (dict['sno'], dict['name'], dict['sex'], dict['age'])
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入数据')

    # 关闭数据库连接
    connect.close()
