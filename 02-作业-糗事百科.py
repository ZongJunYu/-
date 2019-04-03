import urllib.request
import time
import re

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示：
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

def getData(url):
    # print(url)
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    data=response.read().decode()
    # print(data)
    nameCom=re.compile('<h2>(.*?)</h2>', re.S)
    nameComs=nameCom.findall(data)
    # print(nameComs)
    contentCom = re.compile('<span>\n\n(.*?)</span>', re.S)
    contentComs=contentCom.findall(data)
    # print(contentComs)
    return nameComs,contentComs




if __name__ == "__main__":

    # 所有数据
    allData = []
    # [{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},{name1:zh, content:22},...]

    # 遍历每一页的数据
    for i in range(1,4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        list1 = getData(url)
        # print(list1)
        allData.extend(list1)
        # print(allData)
        # print(allData)
    # print(len(allData))
    # print(allData)
    # print(len(allData[1]))
    # print(len(allData[0]))
    # print(allData[0])
    # print(allData[1])

        # time.sleep(0.5)

    dir={}
    # 遍历allData 把数据显示
    for j in range(len(allData)):
        if not j % 2:
            for i in range(len(allData[j])):
                print('%s 说 %s \n'%(allData[j][i].strip('\n'),allData[j+1][i].strip('\n')))




