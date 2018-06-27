# -*- coding:utf-8 -*-

import socket
from stationCom.cloudMsg.handleMsg import HandleCloudMesg
from stationCom.config import EOF, LANE_HOST, LANE_PORT


class GetCloudMesg(object):
    """
    获取云端消息 - socket通信
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def getCloudMsg(self):
        """
        获取云端发送的数据
        """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, self.port))
        try:
            full_data = ""
            while True:
                data = sock.recv(1024).decode(encoding='utf-8')
                if data:
                    full_data += data
                    if full_data.endswith(EOF):
                        full_data = full_data[0:len(full_data) - len(EOF)]
                        HandleCloudMesg().handleMessage(message=full_data)
                else:
                    print("something error ...")
        except Exception as e:
            print(e)
        finally:
            sock.close()


if __name__ == "__main__":
    sc = GetCloudMesg(host=LANE_HOST, port=LANE_PORT)
    sc.getCloudMsg()
