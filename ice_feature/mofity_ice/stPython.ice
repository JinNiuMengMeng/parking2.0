module stpy {
    interface st2py
	{
		
		/*前端实现*/
		int upLaneDevStat(string dataJson, int seq);
		int upLaneWorkstat(string dataJson, int seq);
	};

	
    interface py2st 
	{
        
		//站级实现
		int laneRailUp(int doorNo, int laneNo);
		int laneRailDown(int doorNo, int laneNo);
		int configTideLane(int doorNo, int laneNo, int onOff);
		int uploadCarImg(int doorNo, int laneNo, int onOff);
		int openFreePass(int doorNo, int laneNo);
		int closeFreePass(int doorNo, int laneNo);
		int trigger2ndLpr(int doorNo, int laneNo);
		int laneSleep(int doorNo, int laneNo);
		int laneWakeup(int doorNo, int laneNo);
		int onDuty(int doorNo, int laneNo);
		int offDuty(int doorNo, int laneNo);
		/*登陆接口
		参数:   st2py* p 	-前端Ice代理   由登陆接口传给站级服务端 
				user	-用户名
				passWd	-用户密码		
		返回：   	0:成功
			           
		说明:	车道将本地代理通过登陆接口站级， 站级将其映射在本地， 方便调用车道接口。
		*/
		int login(st2py* p, string user, string passWd);
		int heartBeat();
    };
};