# -*- coding:utf-8 -*-

import time
import zmq
import multiprocessing
from multiprocessing import Pool
from stationCom.clouldMsg.getMsg import getClouldMsg
from stationCom.laneMsg.getMsg import getLaneMsg

if __name__ == "__main__":
    # init()
    # multiprocessing.Process(target=getClouldMsg).start()
    multiprocessing.Process(target=getLaneMsg).start()