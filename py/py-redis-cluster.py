#!/usr/bin/env python
#-- coding:utf8 --
from rediscluster import RedisCluster
import redis,uuid
# r = redis.Redis(host='192.168.123.151',port=6380,db=0,password='yuan',retry_on_timeout=60)  #单机redis连接
startup_nodes = [{"host": "192.168.123.151", "port": 6380}]
r = RedisCluster(startup_nodes=startup_nodes, password="yuan", decode_responses=True, max_connections=200)
#
# for _ in range(1000000):
#     r.set(str(uuid.uuid4()),str(uuid.uuid4()))
# print(r.dbsize())

print('字符串')
r.mset({'name':'younglinuxer','tel':'18983359239'})
r.set('code','shell')
print(r.get('code'))
print(r.mget('name','tel','code'))

print("列表")
r.lpush('list',1,2,3,4,5,6)
r.lpush('list','左边')
r.rpush('list','右边')

print(r.lrange('list',0,-1))


print("哈希类型")
r.hset('user:info', 'name', 'Jack')
r.hset('user:info',mapping={'name2':'younglinuxer','tel':'18983359239','email':'younglinuxer@gmail.com'} )
print(r.hgetall('user:info'))

print("集合类型")
r.sadd('set','ss')
r.sadd('set','r')
print(r.smembers('set'))
print("有序集合")
r.zadd('linux',{'centos':2,'debian':1,'mint':0})
print(r.zrange('linux',0,3))


print('清除数据',r.flushdb())
