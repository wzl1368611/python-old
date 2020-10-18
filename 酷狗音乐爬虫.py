import requests
import time 
import urllib
from urllib import request 
from bs4 import BeautifulSoup
from lxml import etree
import time
import re
import gzip
#http://www.kuwo.cn/search/list?type=all&
#key=%25E6%25B5%2581%25E8%25A1%258C&src=onebox
#http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?
#key=%E6%B5%81%E8%A1%8C&pn=2&rn=30&httpsStatus=1&
#reqId=a3bea1e0-b1c3-11ea-bab6-f95d27553698
strr="流行"
ss=strr.encode()
url="http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=%E6%B5%81%E8%A1%8C&pn=2&rn=30&httpsStatus=1&reqId=a3bea1e0-b1c3-11ea-bab6-f95d27553698"
url1="https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
p={"key":strr}
p1=urllib.parse.urlencode(p)

headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102\
    Safari/537.36 Edge/18.18363",
    "Accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",
    "Accept-Encoding": "br",
    "Accept-Language": "zh-Hans-CN, zh-Hans; q=0.5",

    }
response=requests.get(url1,headers=headers).text
#print(response)
soup=BeautifulSoup(response,'lxml')
data_title=soup.find_all('//a[class="pc_temp_songname" title]')
#print(data_title)
song_title=[]
html=etree.HTML(response)
titles=html.xpath('//a[@class="pc_temp_songname"]')
for i in titles:
    title=i.text
    song_title.append(title)
    print(title)

songs=html.xpath('//a[@class="pc_temp_songname"]/@href')
#https://webfs.yun.kugou.com/202006191123/d85e0a0e9a52a879fa83bf4771d03719/G219/M04/15/0D/Gw4DAF67rxCAA-UGACt13FFB1EI609.mp3
#
#
#https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=5D979B171AC34D82006555E150881A69
#https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=5D979B171AC34D82006555E150881A69


print(songs)
cookies={
    "ACK_SERVER_10015": "%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10016": "%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10017": "%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D",
    "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1592548351",
    "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1592357938,1592535595,1592547194",
    "kg_dfid": "1afPDy0EU2Uh0k7wfd3EBPIt",
    "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
    "kg_mid": "81f8a6c26d1868b05aecc8ee2bc8bf7c",
    "KuGooRandom": "66481592535619603"
}
for x in range(0,1):    
    id=songs[x]                     
    response_play=requests.get(id,headers=headers).content.decode('utf-8','ignore')
    #print(response_play)
    #<script >
    #   var dataFromSmarty = [{"hash":"CDA211CAFEBEDF4CEDAD79DD4BA5628E",
    pattern1=re.compile('"hash":"(.*?)"')
    hash=pattern1.findall(response_play)[0]
    new_url="https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash="+hash
    print(new_url)
    data_load=requests.get(new_url,headers=headers,cookies=cookies).content.decode()
    #print(data_load)
    pat22=re.compile('"play_url":"(.*?)"')
    hash1=pat22.findall(data_load)[0]
    uurl=hash1.replace("\\","")
    print(uurl,"-----------------------------")
    if uurl:
        #resp2=requests.get(uurl,headers=headers).content
        rre=request.Request(uurl,headers=headers)
        resp2=request.urlopen(rre).read()
        
        #ret = gzip.decompress(resp2)
        #print(type(ret))
   
        ss2=song_title[x].split("-")[1]
    
        try:
            print("正在下载第"+str(x+1)+"首歌曲")
            with open("d:\\music\\{}.mp3".format(ss2),"wb") as f:
                f.write(resp2)
                time.sleep(0.5)
        except Exception as e:
            print("下载出错了",e)

        

    

