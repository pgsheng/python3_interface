"""
 @Author  : pgsheng
 @Time    : 2019/3/20 10:50
"""

import requests

json = {"data": "{\"page\":1,\"limit\":10,\"status\":\"\"}", "action": "app.patterList",
        "sessionId": "b1b42bd0-3361-11e9-b301-2dab4fcab8b0"}

res = requests.post('http://127.0.0.1:6000/action', data=json)
# res = requests.get('http://127.0.0.1:6000/monitor')
print(res.text)
