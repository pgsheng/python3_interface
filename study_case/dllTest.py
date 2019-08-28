import clr
import sys

from public import config

project_path = config.study_case_path
sys.path.append(project_path)

clr.FindAssembly("TestDemo")  # 加载c#dll文件
from TestDemo import *  # 导入命名空间

def test():
    instance = TestTxt()  # TestTxt是dll里面的类
    print(instance.GetStr())  # 一个简单的打印


if __name__ == '__main__':
    test()
