"""
 @Author  : pgsheng
 @Time    : 2019/3/20 10:50
"""
import requests

r = requests.get('http://hq.sinajs.cn/list=sh601228')

print(r.text)
