# -*- coding:utf-8 -*-

import multiprocessing
from stationCom.cloudMsg.getMsg import GetCloudMesg
from stationCom.config import LANE_HOST, LANE_PORT, CLOUD_PORT, CLOUD_HOST
from stationCom.laneMsg.getMsg import GetLaneMesg

if __name__ == "__main__":
    # init()
    multiprocessing.Process(target=GetCloudMesg(
        host=LANE_HOST, port=LANE_PORT).getCloudMsg).start()

    multiprocessing.Process(target=GetLaneMesg(
        host=CLOUD_HOST, port=CLOUD_PORT).getLaneMsg).start()
