import json

import requests


headers = {
    "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
url='https://fanyi.baidu.com/transapi'
item='垃圾'
data={
    'from': 'auto',
    'to': 'en',
    'query':item,
    'simple_means_flag': 3,
    'sign': 663085.982300,
    'token': '0a59ffce97275cbd2881cddd3e7b5ae1',
}
response=requests.post(url,data=data,headers=headers)
print(response.content.decode())
json_list=json.loads(response.text)
print(json_list)
print(json_list['data'][0]['dst'])
