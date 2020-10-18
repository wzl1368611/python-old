from urllib import request
import requests
import urllib
import time 
from lxml import etree
import re

#
#
#请求 URL: http://www.5nd.com/paihang/tuijiangequ.htm
#http://mpge.5nd.com/2020/2020-6-15/97048/1.mp3
#<div class="songPlayBox"><div id="kuPlayer" data-play="2020/2020-6-15/97048/1.mp3"></div>

#<script type="text/javascript"> var urlht = "2020/2020-6-15/97048/1.mp3";</script>

songId=[]
songName=[]
singerName=[]
url="http://www.5nd.com/paihang/tuijiangequ.htm"
headers={
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}
try:

    response=requests.get(url,headers=headers).content.decode('gb2312','ignore')
    #print(response)
except Exception as e:
    print(e)
#print(response)
#解析网页获取所需信息

pat=re.compile('<a target="_ting" href="(.*?)"')
data1=pat.findall(response)

html=etree.HTML(response)
hdata=html.xpath('//a[@class="rankNane"]')
for j in hdata:
    song=j.text.split("-")[0]
    singer=j.text.split("-")[1]
    #打印歌曲名称-----------
    #print(song)
    #print(singer)
    print(song)
    songName.append(song)
    singerName.append(singer)
#print(data1[0])
#
print(songName)
for i in data1:
    #http://www.5nd.com/ting/660473.html
    myurl="http://www.5nd.com"+i
    print(myurl)
    response2=requests.get(myurl,headers=headers).text 
    pat2=re.compile('id="kuPlayer" data-play="(.*?)">')
    data2=pat2.findall(response2)
    #print(type(data2))
    #print(len(data2))
    songId.append(data2[0])


print(songId)
   
    
    
for x in range(0,len(songId)):
    print(x+1)
    playurl="http://mpge.5nd.com/"+songId[x]
    print(playurl)
    
    data=requests.get(playurl,headers=headers).content
    #print(data)
    print("正在下载第"+str(x+1)+"首歌曲")
    sn=songName[x]
    print(sn)
    with open("E:\\music\\{}.mp3".format(sn),"wb") as f:
        f.write(data)
        time.sleep(0.5)





        











