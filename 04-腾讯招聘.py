import urllib.request
headers = {
    "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
# https://hr.tencent.com/position_detail.php?id=49003&keywords=python&tid=0&lid=2218'
for i in range(40000,4001):
    url = 'https://hr.tencent.com/position_detail.php?id=49003&keywords=python&tid=0&lid=2218'
    data={
        'id': i,
        'keywords': 'python',
        'tid': 0,
        'lid': 2218
    }

    req=urllib.request.Request(url,data=data,headers=headers)
    print(req)
    response=urllib.request.urlopen(req)
    print(response)
    print(response.read().decode())