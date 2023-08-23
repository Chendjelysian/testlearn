from kafka import KafkaConsumer

consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'],group_id=None,auto_offset_reset='smallest')
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)