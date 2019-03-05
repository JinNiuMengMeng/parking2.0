# -_- coding:utf-8 -_-

import Ice
Ice.loadSlice("stPython.ice")
import stpy

ICE_CONFIG = ['--Ice.ThreadPool.Server.Size=5', '--Ice.ThreadPool.Server.SizeMax=10']


class FakeLane(stpy.py2st):
    def login(self, p, user, passWd, current=None):
        print("模拟车道服务端--接收数据为: ")
        print("p:", p)
        print("user:", user)
        print("passWd:", passWd)
        return 1

    def laneRailUp(self, doorNo, laneNo, current=None):
        print("模拟车道服务端--接收数据为: ")
        print("doorNo:", doorNo)
        print("laneNo:", laneNo)
        return 1


with Ice.initialize(ICE_CONFIG) as ic:  # 初始化运行环境
    adapter = ic.createObjectAdapterWithEndpoints("xmrbi", "default -p 9528")
    st_handle = FakeLane()

    adapter.add(st_handle, ic.stringToIdentity("Epms_st"))
    adapter.activate()
    ic.waitForShutdown()
