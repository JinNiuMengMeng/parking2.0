# -*- coding:utf-8 -*-
import pymysql


class MysqlHelper(object):
    host = "192.168.43.38"
    port = 3306
    database = "movie"
    user = "root"
    password = "123456"
    charset = "utf8"
    conn = None
    cur = None

    @classmethod
    def __connect(cls):
        cls.conn = pymysql.connect(host=cls.host, user=cls.user, password=cls.password,
                                   database=cls.database, port=cls.port, charset=cls.charset,
                                   cursorclass=pymysql.cursors.DictCursor)
        cls.cur = cls.conn.cursor()

    @classmethod
    def fetchone(cls, sql, params=None):
        data_one = None
        try:
            cls.__connect()
            count = cls.cur.execute(sql, params)
            if count != 0:
                data_one = cls.cur.fetchone()
        except Exception as ex:
            return ex
        finally:
            cls.__close()
        return data_one

    @classmethod
    def fetchall(cls, sql, params=None):
        data_all = None
        try:
            cls.__connect()
            count = cls.cur.execute(sql, params)
            if count != 0:
                data_all = cls.cur.fetchall()
        except Exception as ex:
            return ex
        finally:
            cls.__close()
        return data_all

    def __item(self, sql, params=None):
        count = 0
        try:
            self.__connect()
            count = self.cur.execute(sql, params)
            self.conn.commit()
        except Exception as ex:
            return ex
        finally:
            self.__close()
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
