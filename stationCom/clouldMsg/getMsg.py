# -*- coding:utf-8 -*-

import socket
import sys
import time
from stationCom.clouldMsg.handleMsg import handleMessage
from stationCom.config import HOST, PORT


def getClouldMsg():
    """
    获取云端发送的数据
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(2)
    buffer = list()
    while True:
        msg = s.recv(2048).decode('utf-8')
        handleMessage(msg)



"""  
    while True:
        try:
            msg = s.recv(2048).decode('utf-8')
        except socket.timeout as e:
            err = e.args[0]
            if err == 'timed out':
                time.sleep(2)
                continue
            else:
                sys.exit(1)
        else:
            if len(msg) == 0:
                sys.exit(0)
            else:
                buffer.append(msg)
                data = ''.join(buffer)
                print(data)
"""