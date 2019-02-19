# -*- coding:utf-8 -*-
import pymysql


class MysqlHelper(object):
    host = "192.168.43.38"
    # host = "127.0.0.1"
    port = 3306
    database = "yilu_park"
    user = "root"
    password = "123456"
    charset = "utf8"
    conn = None
    cur = None

    @classmethod
    def __connect(cls):
        try:
            cls.conn = pymysql.connect(host=cls.host, user=cls.user, password=cls.password,
                                       database=cls.database, port=cls.port, charset=cls.charset,
                                       cursorclass=pymysql.cursors.DictCursor)
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
        finally:
            cls.__close()

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
        finally:
            cls.__close()

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
        finally:
            cls.__close()

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

