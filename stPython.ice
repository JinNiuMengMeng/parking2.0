module stpy {
    interface st2py
	{
		// 成功返回seq, 失败返回-seq
		int upLaneRecord(string dataJson, int seq);
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
		参数:   st2py* p 	-python Ice代理   由登陆接口传给站级服务端
				user	-用户名
				passWd	-用户密码
		返回：   	0:成功， -1：失败
		说明:	车道将本地代理通过登陆接口站级， 站级将其映射在本地， 方便调用车道接口。
		*/
		int login(st2py* p, string user, string passWd);


		/*代理请求接口
		参数:
				doorNo	-
				laneNo	-
		返回：   	0:成功 -1：失败
		说明:	页面将目标车场的门号道号传给站级，站级通过代理映射关系，向车道发起代理请求。
		*/
		int request(int doorNo, int laneNo);


		/*登出接口
		参数:
				st2py* p	- 登陆时上传的代理
				user		- 登陆用户名
		返回：   	0:成功 -1：失败
		说明:	登出接口，页面退出，站级将python代理置为不使能，停止消息推送
		*/
		int logout(st2py* p, string user);


		/*心跳接口
		参数:   缺省
		返回：   	0:成功 -1：失败
		说明:	由python客户端定时调用，维持连接心跳
		*/
		int heartBeat();
    };
};
