# 接口测试框架（基于python3 + unittest + ddt + excel实现的一套测试框架）

### 1.环境准备：

- python3.7
- requests
- xlrd 
- openpyxl
- HTMLTestRunner

### 2.目前实现的功能：

- 封装requests请求方法
- 封装excel表读取和写入方法
- 在excel填写接口请求参数、断言判断等,运行完后，把结果写入excel
- 用unittest+ddt+excel数据驱动模式执行
- 使用HTMLTestRunner生成可视化的html报告
- 可使用全局变量存储上个请求的结果是下个请求的参数，如token。
- 封装Logger日志类
- 实现通过邮箱发送测试报告功能 

### 3.项目结构图：
![](https://github.com/pgsheng/python3_interface/raw/master/img/ProjectStruct.png)


