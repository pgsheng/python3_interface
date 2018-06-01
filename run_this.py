import smtplib
import unittest
import time

import os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from public import HTMLTestRunner_jpg,HTMLTestRunner

''' 该函数功能是获最新的HTML测试报告'''
def get_report(dir):
	# dir指报告所在目录，listdir()方法是获取dir目录下所有文件和文件夹的列表
	lists = os.listdir(dir)
	# 对列表进行排序，以创建时间顺序排序
	lists.sort(key=lambda fn: os.path.getatime(dir + "\\" + fn))
	# 获取列表最后一个元素，即最新的HTML测试报告，再和目录dir拼接得到测试报告文件的路径
	filename = os.path.join(dir, lists[-1])
	# 返回获取到的测试报告文件的路径
	return filename

''' 该函数功能是通过邮件发送测试报告'''
def send_email(filename):
	#定义发送邮件的服务器主机
	mail_host = 'smtp.163.com'
	# 定义发送邮件账号和密码
	mail_user = 'xxxxxx@163.com'
	mail_pass = 'xxxxxx'
	# 定义接收邮件的账号
	recivers = ['xxxxxx@163.com']
	# 定义发送邮件的类型，'related'类型是可以携带附件
	message = MIMEMultipart('related')
	# 打开报告文件并读取文件内容作为邮件的内容
	f = open(filename, 'rb')
	mail_body = f.read()
	# 定义发送邮件附件的格式
	att = MIMEText(mail_body, 'base64', 'utf-8', )
	att["Content-Type"] = 'application/octet-stream'
	att["Content-Disposition"] = 'attachment;filename="report.html"' # 定义附件名称
	# 为邮件加载附件
	message.attach(att)
	f.close() #关闭文件读取流

	# 定义发送邮件内容的格式
	msg = MIMEText(mail_body, 'html', 'utf-8')
	# 为邮件加载邮件内容
	message.attach(msg)
	# 指定发送邮件的账号
	message['Form'] = mail_user
	# 指定接收邮件的账号
	message['To'] = ','.join(recivers)
	# 定义邮件的标题
	message['Subject'] = Header('接口自动化测试报告', 'utf-8')
	# 邮件传输协议
	smtp = smtplib.SMTP()
	# 连接服务器主机
	smtp.connect(mail_host)
	# 登录发送邮件的账号
	smtp.login(mail_user, mail_pass)
	# 发送邮件
	smtp.sendmail(mail_user, recivers, message.as_string())
	smtp.quit()


if __name__ == '__main__':
	# 测试用例所在文件夹
	test_dir = './test_case'
	# 自动识别用例,得到测试套件对象
	discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')
	# 设置时间的格式
	now_time = time.strftime('%Y-%m-%d %H-%M-%S')
	# 在目录demo_report下创建一个.html格式的文件，以当前时间命名
	filename = './test_report/' + now_time + '_test_result.html'
	# 以“wb”方式打开文件，如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
	fp = open(filename, 'wb')
	# 调用写好的HTMLTestRunner指定生成报告的文件、标题和副标题
	# runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp,
	# 						title='Demo Test Report',
	# 						description='这是测试demo的测试报告：',
	# 						retry=1)
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
							title='Demo Test Report',
							description='这是测试demo的测试报告：')
	# 执行测试用例集并生成报告
	runner.run(discover)
	# 关闭文件流
	fp.close()

	# rep = get_report('./test_report')
	# send_email(rep) # 通过邮件发送测试报告的
