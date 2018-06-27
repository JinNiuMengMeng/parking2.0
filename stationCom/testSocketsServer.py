#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
from threading import Thread
from stationCom.config import CLOUD_HOST, CLOUD_PORT, EOF


class SocketServer(object):

    def __init__(self, host=None, port=None):
        self.port = port
        self.host = host

    def startup(self):
        sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_server.bind((self.host, self.port))
        sock_server.listen(3)
        while True:
            sock, address = sock_server.accept()
            Thread(target=self.__invoke, args=(sock, address)).start()

    def shutdown(self):
        pass

    def __invoke(self, sock, address):
        try:
            while True:
                sock.send(("1234567890" + EOF).encode('utf-8'))
                time.sleep(2)
                message = sock.recv(1024).decode('utf-8')
                print(address, "消息为:", message)
        except Exception as e:
            print(e)
        finally:
            sock.close()


if __name__ == "__main__":
    ss = SocketServer(host=CLOUD_HOST, port=CLOUD_PORT)
    ss.startup()
