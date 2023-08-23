# producer_json.py
from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))  # 连接kafka

data = {
    "sno": "95001",
    "name": "John",
    "sex": "M",
    "age": 23
}

producer.send('json_topic', data)  # 发送的topic为json_topic
producer.close()
