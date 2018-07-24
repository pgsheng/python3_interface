#coding=utf-8
import jpype
from jpype import *
from jpype import JavaException
import sys

# 模拟接收失败的场景Avro
# 目的：发送正确的消息，使用错误的方式来接受，若能够捕捉到异常，说明sdk是可以的
from test import env


def sendAvro(hostName):
    print ("going to send a avro fail message...")

    zmsClient = env.ZmsClient(env.apiId, env.apiKey, hostName,
                              env.unicastPort, env.multicastPort)

    people = env.People()

    people.setName(env.String("刘德华"))
    people.setAge(env.Integer(56))
    people.setGender(env.String("男"))
    people.setAddress(env.String("广州市天河区"))
    people.setIdNumber(env.String("450xxxxxxxxxxxxxxxxxx"))

    #此处发送的Avro数据，需要修改成发送Json数据
    #blob = testSDKParent.Base64Utils.avroEncoder(people)
    blob = env.ZMSGsonUtils.toJson(people)

    zmsClient.applyMulticastToken()
    zmsMulticasSender = zmsClient.getZmsHttpSenderToken()

    requestSendMessage = env.RequestSendMessageModel()
    requestSendMessage.setQueueName(env.sQueue)
    requestSendMessage.setFrom(env.sfrom)
    requestSendMessage.setSendTs(java.lang.String.valueOf(java.lang.System.currentTimeMillis()))

    messageBodyModel = env.MessageBodyModel()
    messageBodyModel.setBlobType(env.sQueue + "^" + env.version)
    messageBodyModel.setVersion(env.version)
    messageBodyModel.setBlobCategory(env.String("AVRO"))

    # data = "测试数据Avro"
    messageBodyModel.setBlob(blob)
    requestSendMessage.setMessageBody(messageBodyModel)

    customAttributes = java.util.ArrayList()
    attributes = env.AttributeModel("attr1", "attr2")
    customAttributes.add(attributes)

    requestSendMessage.setCustomAttributes(customAttributes)

    try:
        bb = env.ZMSGsonUtils.toJson(requestSendMessage);
        responseSuccess = zmsMulticasSender.sendMessage(requestSendMessage)


        zmsClient.closeAccess()
    except JavaException as ex:
        print ("Caught Java exception : ", ex.message())
        print (ex.stacktrace())

#无令牌接收
def receiveAvro(hostName):
    print ("going to receive avro messages...")
    zmsClient = env.ZmsClient(env.apiId, env.apiKey, hostName,
                              env.unicastPort, env.multicastPort)

    # zmsClient.applyMulticastToken()
    zmsMulticastReceiver = zmsClient.getZmsHttpReceiverToken()

    requestReceiveMessage = env.RequestReceiveMessageModel()
    requestReceiveMessage.setDuration("3000")
    requestReceiveMessage.setMsgNumber("3")
    requestReceiveMessage.setQueueName(env.rQueue)
    requestReceiveMessage.setRequestTs(java.lang.String.valueOf(java.lang.System.currentTimeMillis()))

    try:
        zmsMulticastReceiver.receiveMessages(requestReceiveMessage)
        zmsClient.closeAccess()
        print ("没有申请令牌消息可以接收成功！！！")
        exit(1)
    except JavaException as ex:
        print ("Caught Java exception : ", ex.message())
        print (ex.stacktrace())

if __name__ == '__main__':
    env.configs(sys.argv[1:])
    # # 执行信息发送
    # for ip in env.hostNameList:
    #     print "发送ip = %s" % (ip)
    #     sendAvro(ip)
    #     break
    #
    # time.sleep(1)
    # # 执行信息接收
    # for ip in env.hostNameList:
    #     print "接收ip = %s" % (ip)
    #     receiveAvro(ip)

# 测试java输出
# jprintln = System.out.println
# jprintln("hello world")

# 关闭JVM
shutdownJVM()