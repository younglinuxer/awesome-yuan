#!/usr/bin/env python
#-- coding:utf8 --
import redis,uuid

r = redis.Redis(host='192.168.123.151',port=6379,db=6,password='yuan',retry_on_timeout=60)
for _ in range(10000):
    r.set(str(uuid.uuid4()),str(uuid.uuid4()))

print r.dbsize()