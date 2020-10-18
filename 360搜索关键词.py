import urllib 
from urllib import request
import requests
url="https://www.so.com/s?"
q={"q":"长城"}
wd2=urllib.parse.urlencode(q)   #注意用法
wd3=urllib.parse.urlencode(q).encode("utf-8") 
print("wd2的格式",type(wd2))
print("wd3的格式",type(wd3))
fullurl=url+wd2
print(fullurl)
req=request.Request(fullurl)
response=request.urlopen(req).read().decode()
#print(response)
