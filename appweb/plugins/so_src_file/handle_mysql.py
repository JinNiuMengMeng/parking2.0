# -*- coding:utf-8 -*-

import pymysql
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(
    creator=pymysql,
    maxconnections=10,
    mincached=10,
    maxcached=0,
    blocking=True,
    maxusage=None,
    ping=0,
    # host='127.0.0.1',
    host='192.168.14.137',
    port=3306,
    user='root',
    database='yilu_park',
    password='emb@3967968',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)


class MysqlHelper(object):
    conn = None
    cur = None

    @classmethod
    def __connect(cls):
        try:
            cls.conn = POOL.connection()
            cls.cur = cls.conn.cursor()
            if cls.conn and cls.cur:
                return True
        except:
            return False

    @classmethod
    def fetchone(cls, sql, params=None):
        data_one = -2
        try:
            if not cls.__connect():
                return -1
            count = cls.cur.execute(sql, params)
            if count != 0:
                data_one = cls.cur.fetchone()
                return data_one
            else:
                return count
        except Exception as ex:
            return data_one

    @classmethod
    def fetchall(cls, sql, params=None):
        data_all = -2
        try:
            if not cls.__connect():
                return -1
            count = cls.cur.execute(sql, params)
            if count != 0:
                data_all = cls.cur.fetchall()
            return data_all
        except Exception as ex:
            return data_all
            
    @classmethod
    def __item(cls, sql, params=None):
        count = -3
        try:
            if not cls.__connect():
                return -1
            count = cls.cur.execute(sql, params)
            cls.conn.commit()
            return count
        except Exception as ex:
            return count

    @classmethod
    def update(cls, sql, params=None):
        return cls.__item(sql, params)

    @classmethod
    def insert(cls, sql, params=None):
        return cls.__item(sql, params)

    @classmethod
    def delete(cls, sql, params=None):
        return cls.__item(sql, params)

    @classmethod
    def __close(cls):
        if cls.cur:
            cls.cur.close()
