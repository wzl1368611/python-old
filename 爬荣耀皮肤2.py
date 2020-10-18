import requests
import json
import time 
import os
import re
url=requests.get('http://pvp.qq.com/web201605/js/herolist.json').content
jsonFile=json.loads(url) 
headers={
    
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}
print(jsonFile)
print(len(jsonFile))
#len(jsonFile)
for i in range(95,97):
    cname=jsonFile[i]['cname'] 
    print(type(jsonFile[i]),jsonFile[i])
    pat=re.compile("'skin_name': '.*?'")
    ss=pat.findall(str(jsonFile[i]))
    #jsonFile[i].find('skin_name')
    if len(ss)>0:
        try:
            str1=jsonFile[i]['skin_name']
            if str1.find('|')>-1:
                skin_name=jsonFile[i]['skin_name'].split('|') #皮肤名称

                ename=jsonFile[i]['ename'] #皮肤id
                dir="d:/王者荣耀"
                #全部存到王者荣耀文件夹里面
                if not os.path.exists('d:/王者荣耀'):
                    os.mkdir('d:/王者荣耀')  #存储路径
                if not os.path.exists(dir+"/"+cname):
                    os.mkdir(dir+"/"+cname)
                for i in range(0,len(skin_name)):
                    
                    pic_url="http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{j}/{j}-bigskin-{k}.jpg".format(j=ename,k=i+1)
                    print(pic_url)
                    data=requests.get(pic_url,headers=headers).content
                    #skin_name[i]+
                    #pic_url.split('/')[-1]
                    with open(dir+"/"+cname+"/"+skin_name[i]+pic_url.split('/')[-1],'wb') as f:
                        f.write(data)
                print("本英雄下载完成============")
                time.sleep(0.5)
            else :
                #skin_name=jsonFile[i]['skin_name']#皮肤名称

                ename=jsonFile[i]['ename'] #皮肤id
                dir="d:/王者荣耀"
                #全部存到王者荣耀文件夹里面
                if not os.path.exists('d:/王者荣耀'):
                    os.mkdir('d:/王者荣耀')  #存储路径
                if not os.path.exists(dir+"/"+cname):
                    os.mkdir(dir+"/"+cname)
                for i in range(0,8):
                    pic_url="http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{j}/{j}-bigskin-{k}.jpg".format(j=ename,k=i+1)
                    print(pic_url)
                    data=requests.get(pic_url,headers=headers).content
                        #skin_name[i]+
                        #pic_url.split('/')[-1]
                    with open(dir+"/"+cname+"/"+pic_url.split('/')[-1],'wb') as f:
                        f.write(data)
                print("本英雄下载完成============")
                time.sleep(0.5)
        except Exception as e:
            print(e,"==========")

    else :
        #skin_name=jsonFile[i]['skin_name']#皮肤名称

        ename=jsonFile[i]['ename'] #皮肤id
        dir="d:/王者荣耀"
        #全部存到王者荣耀文件夹里面
        if not os.path.exists('d:/王者荣耀'):
            os.mkdir('d:/王者荣耀')  #存储路径
        if not os.path.exists(dir+"/"+cname):
            os.mkdir(dir+"/"+cname)
        for i in range(0,8):
            pic_url="http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{j}/{j}-bigskin-{k}.jpg".format(j=ename,k=i+1)
            print(pic_url)
            data=requests.get(pic_url,headers=headers).content
                #skin_name[i]+
                #pic_url.split('/')[-1]
            with open(dir+"/"+cname+"/"+pic_url.split('/')[-1],'wb') as f:
                f.write(data)
        print("本英雄下载完成============")
        time.sleep(0.5)

        

# https://game.gtimg.cn/images/yxzj/img201606/heroimg/531/531-smallskin-2.jpg
# http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/506/506-bigskin-2.jpg
# <img alt="" src="//game.gtimg.cn/images/yxzj/img201606/heroimg/506/506-smallskin-2.jpg" data-imgname="//game.gtimg.cn/images/yxzj/img201606/skin/hero-info/506/506-bigskin-2.jpg" data-icon="0" data-title="荷鲁斯之眼">
# http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/105/105-bigskin-0.jpg
# http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/106/106-bigskin-1.jpg
