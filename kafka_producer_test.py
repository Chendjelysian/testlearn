from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')  # 连接Kafka

msg = "Hello World".encode('utf-8')  # 发送内容,必须是bytes类型
producer.send('test', msg)  # 发送的topic为test
producer.close()