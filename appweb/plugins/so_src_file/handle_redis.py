# -*- coding:utf-8 -*-
import json

import redis


class MyRedis(object):
    def __init__(self, ip, password, port=6379, db=2):

        # 构造函数
        try:
            self.r = redis.Redis(host=ip, password=password, port=port, db=db)
        except Exception as e:
            print 'redis连接失败，错误信息%s' % e

    def str_get(self, k):
        res = self.r.get(k)
        if res:
            return res.decode()

    def str_set(self, k, v, time=None):
        res = self.r.set(k, v, time)
        if res:
            return True
        else:
            return False

    def delete(self, k):
        tag = self.r.exists(k)  # 判断这个Key是否存在
        if tag:
            self.r.delete(k)
            return True
        else:
            return False

    def hash_hget(self, name, key):
        res = self.r.hget(name, key)
        if res:
            return res.decode()
        else:
            return False

    def hash_hset(self, name, k, v):
        res = self.r.hset(name, k, v)
        if res:
            return True
        else:
            return False

    def hash_hmset(self, name, mapping):
        res = self.r.hmset(name=name, mapping=mapping)
        if res:
            return True
        else:
            return False

    def hash_getall(self, name):
        res = self.r.hgetall(name=name)
        new_dict = {}
        if res:
            for k, v in res.items():
                k = k.decode()
                v = v.decode()
                new_dict[k] = v
        return new_dict

    def hash_del(self, name, k):
        res = self.r.hdel(name, k)
        if res:
            return True
        else:
            return False

    def set_expire(self, name, timeout):
        res = self.r.expire(name=name, time=timeout)
        if res:
            return True
        else:
            return False

    @property
    def clean_redis(self):
        self.r.flushdb()
        return True


RedisHelper = MyRedis(ip="172.16.52.38", password="xmrbi2580056redis2017", port=6379, db=2)
