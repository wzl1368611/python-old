import requests
import urllib
from urllib import request
import time 
from lxml import etree


#https://www.qiushibaike.com/8hr/page/1/
#https://www.qiushibaike.com/8hr/page/3/


#https://www.qiushibaike.com/article/123226836
#https://www.qiushibaike.com/article/123206974

#<a class="recmd-content" href="/article/123206974" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-user','chick'])">这么多年，我都是错的吗？</a>
#<div class="recmd-detail clearfix">
headers={
    
   "Accept": "text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8",

   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}
url="https://www.qiushibaike.com/8hr/page/"
beginPage=1
endPage=10
for page in range(beginPage,6):
    myUrl=url+str(page)+"/"
    print(myUrl)
    req=request.Request(myUrl,headers=headers)
    response=request.urlopen(req).read().decode()
    #print(response)
    html=etree.HTML(response)
    data=html.xpath('//div[@class="recmd-right"]/a/@href')
    print(data)
    for i in data:
        print(i)
        url2="https://www.qiushibaike.com"+i
        print(url2)
        req2=request.Request(url2,headers=headers)
        response2=request.urlopen(req2).read().decode()
        
        html2=etree.HTML(response2)
        data2=html2.xpath('//div/h1[@class="article-title"]')
        #data3=html2.xpath('//div[@class="content"]')
        for x in range(0,len(data2)):
            print(data2[x].text)
            #print(data3[x].contents)
            print("----------------------------------")





#('//div/h1[@class="article-title"]')
#('//div[@class="content"]')




