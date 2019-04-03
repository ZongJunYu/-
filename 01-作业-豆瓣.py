import json
import urllib.request


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"



def getData(url):
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    req=urllib.request.Request(url,headers=headers)
    response=urllib.request.urlopen(req)
    conent=response.read().decode()
    data=json.loads(conent)
    # print(data)
    for i in data:
        img=i.get('cover_url')
        title=i.get('title')
        print(img,title)
        urllib.request.urlretrieve(img,filename='img/%s.jpg' %title)

if __name__ == "__main__":

    for i in range(1,5):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"
        getData(url)











