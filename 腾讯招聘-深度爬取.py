import urllib.request
from bs4 import BeautifulSoup
import re
headers={
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

def get_url(url):
    try:
        req=urllib.request.Request(url,headers=headers)
        response=urllib.request.urlopen(req).read()
        soup=BeautifulSoup(response,'lxml')
        url_list = soup.find_all(href=re.compile('position_detail'))
        # print(url_list)
        urls = []
        url1 = 'https://hr.tencent.com/'
        for url in url_list:
            new_url = url1 + str(url['href'])
            urls.append(new_url)

        return urls
    except:
        return ''
def deep_url(url):
    sonurl=get_url(url)
    for url in sonurl:
        request = urllib.request.Request(url, headers=headers)
        response=urllib.request.urlopen(request).read()
        soups=BeautifulSoup(response,'lxml')
        data0=soups.find_all('td',id='sharetitle')[0].text
        data=soups.find_all('tr',class_='c')[2].text
        data1=soups.find_all('tr',class_='c')[1].text
        print('工作岗位:')
        print(data0)
        print('工作要求/工作职责:')
        print(data)
        print(data1)
        print('*'*100)

if __name__=='__main__':
    for i in range(1):
        url='https://hr.tencent.com/position.php?keywords=python&tid=0&lid=2218&start={}#a'.format(i*10)
        # print(url)



        deep_url(url)