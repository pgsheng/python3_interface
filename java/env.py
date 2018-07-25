# coding=utf-8
from jpype import *
import sys
import getopt

# import jdk class
System = JClass("java.lang.System")
String = JClass("java.lang.String")
Boolean = JClass("java.lang.Boolean")
Byte = JClass("java.lang.Byte")
Short = JClass("java.lang.Short")
Integer = JClass("java.lang.Integer")
Long = JClass("java.lang.Long")
Float = JClass("java.lang.Float")
Double = JClass("java.lang.Double")

# 将端口放在这里，是因为需要将int类型转为java类型的int
unicastPort = Integer(6868)
multicastPort = Integer(8080)

# import all classes
ZmsClient = JClass("com.gzzn.zmssdk.ZmsClient")
ZmsMulticasSender = JClass("com.gzzn.zmssdk.sender.ZmsMulticasSender")
Attribute = JClass("com.gzzn.zmsapi.v1.Attribute")
MessageBody = JClass("com.gzzn.zmsapi.v1.MessageBody")
RequestSendMessage = JClass("com.gzzn.zmsapi.v1.RequestSendMessage")
ResponseSuccess = JClass("com.gzzn.zmsapi.v1.ResponseSuccess")
AttributeModel = JClass("com.gzzn.zmsapi.v1.impl.AttributeModel")
MessageBodyModel = JClass("com.gzzn.zmsapi.v1.impl.MessageBodyModel")
ObjectInitException = JClass("com.gzzn.zmsapi.v1.impl.ObjectInitException")
RequestSendMessageModel = JClass("com.gzzn.zmsapi.v1.impl.RequestSendMessageModel")
LogicException = JClass("com.gzzn.zmssdk.exception.LogicException")
ServerException = JClass("com.gzzn.zmssdk.exception.ServerException")
ZmsHttpSenderException = JClass("com.gzzn.zmssdk.exception.ZmsHttpSenderException")

# 工商测试jar包导入
MySendMulticast = JClass("com.gzzn.zmssdk.testing.util.MySendMulticast")
# 工商测试jar包导入

# 发送avro数据
People = JClass("com.gzzn.model.People")
Menber = JClass("com.gzzn.model.Menber")
Home = JClass("com.gzzn.model.Home")
Base64Utils = JClass("com.gzzn.zmssdk.utils.Base64Utils")
ArrayList = JClass("java.util.ArrayList")

MeatCategoryInfo = JClass("com.gzzn.model.nyj.info.MeatCategoryInfo")
MeatCertRecordNew = JClass("com.gzzn.model.nyj.niu.MeatCertRecordNew")

# 发送avro数据

# 接收常规数据实体类
RequestReceiveMessage = JClass("com.gzzn.zmsapi.v1.RequestReceiveMessage")
RequestReceiveMessageModel = JClass("com.gzzn.zmsapi.v1.impl.RequestReceiveMessageModel")
ReceiveMessages = JClass("com.gzzn.zmsapi.v1.ReceiveMessages")
ReceiveMessagesModel = JClass("com.gzzn.zmsapi.v1.impl.ReceiveMessagesModel")
MultiMessage = JClass("com.gzzn.zmsapi.v1.MultiMessage")
MultiMessageModel = JClass("com.gzzn.zmsapi.v1.impl.MultiMessageModel")
RequestSendMultiMessageModel = JClass("com.gzzn.zmsapi.v1.impl.RequestSendMultiMessageModel")
SendMultiMsgResult = JClass("com.gzzn.zmsapi.v1.SendMultiMsgResult")
List = JClass("java.util.List")
ZMSGsonUtils = JClass("com.gzzn.zmsapi.tools.ZMSGsonUtils")


# 接收常规数据实体类

# 获取传过来的参数
def configs(argv):
	global apiId
	global apiKey
	global hostName
	global rQueue
	global sQueue
	global testSample
	global unicastPort
	global multicastPort
	global hostNameList
	global apiIdList
	global apiKeyList
	global queueList

	try:
		options, args = getopt.getopt(argv, "?p:i:k:t:r:s:u:m:",
									  ["help", "hostName=", "apiId=", "apiKey=", "testSample=", "rQueue=", "sQueue=",
									   "unicastPort=", "multicastPort="])
	except getopt.GetoptError:
		print("获取Jenkins参数异常")
		sys.exit()

	for option, value in options:
		if option in ("-?", "--help"):
			print("help")
		if option in ("-p", "--hostName"):
			hostName = value
		if option in ("-t", "--testSample"):
			testSample = value
		if option in ("-i", "--apiId"):
			apiId = value
		if option in ("-k", "--apiKey"):
			apiKey = value
		if option in ("-r", "--rQueue"):
			rQueue = value
		if option in ("-s", "--sQueue"):
			sQueue = value
		if option in ("-u", "--unicastPort"):
			unicastPort = Integer(Integer.parseInt(value))
		if option in ("-m", "--multicastPort"):
			multicastPort = Integer(Integer.parseInt(value))

	hostNameList = hostName.split(";")
	apiIdList = apiId.split(";")
	apiKeyList = apiKey.split(";")
	queueList = sQueue.split(";")
