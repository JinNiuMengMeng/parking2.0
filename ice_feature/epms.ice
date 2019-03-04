
module stpy {
    interface st2py
	{
		/*站级向前端上送消息
		参数:   dataJson 	-消息内容，Json串格式
				command		-命令字
				sessionID 	-序列号
		返回：   	{"sessionID": ssID, "errorID": erID, "message": "msg"}

		说明:	根据命令字和Json串内容，确定具体服务类型
		*/
		// 上传车辆信息
        ["amd"] string msgSt2py(string dataJson, int command, int sessionID);
    };

    interface py2st
	{

		/*前端下发消息给站级
		参数:   dataJson 	-消息内容，Json串格式
				command		-命令字
				sessionID 	-序列号
		返回：   	0 成功; < 0 失败;

		说明:	根据命令字和Json串内容，确定具体服务类型
		*/
		// 抬杆落杆
		 int msgPy2st(string dataJson, int command, int sessionID);
    };
};
