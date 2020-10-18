from requests_html import HTMLSession
import urllib.request,os,json
from urllib.parse import quote
import re
import requests
import time 
global zz
zz=0
class KuGou():
    def __init__(self):
        self.get_music_url='https://songsearch.kugou.com/song_search_v2?keyword={}&platform=WebFilter'
        self.get_song_url='https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}'
        if not os.path.exists("d:/music"):
            os.mkdir('d:/music')

    def parse_url(self,url):
        session = HTMLSession()

        response = session.get(url)
        res=response.content.decode()
        print("所得到的的网页信息为",res)
        return response.content.decode()

    def get_music_list(self,keyword):
        music_dirt=json.loads(self.parse_url(self.get_music_url.format(quote(keyword))))
        music_list=music_dirt['data']['lists']
        song_list=[]
        for music in music_list:
            song_name=music['FileName'].replace("<\\/em>", "").replace("<em>", "")
            song_list.append({'hash':music['FileHash'], 'song_name':song_name})
            print(str(len(song_list))+'---'+song_name)
        return song_list

    def download(self,song):
        myUrl=self.get_song_url.format(song['hash'])
        print(myUrl)
        #jj=self.parse_url(myUrl)
        #将这一步替换成自己写的获取网页
        headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102\
        Safari/537.36 Edge/18.18363"}
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
        myResponse=requests.get(myUrl,headers=headers,cookies=cookies).content.decode()
        #https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}
        #http://www.kugou.com/yy/index.php?r=play/getdata&hash=CB7EE97F4CC11C4EA7A1FA4B516A5D97
        print(myResponse)
        #song_dirt=json.loads(myResponse)
        
        #for i in song_dirt:
        #    print("===========",i)
        #"play_url":"https:\/\/webfs.yun.kugou.com\/202"
        #pat="'play_url':'(.*?)'"
        pattern=re.compile('"play_url":"(.*?)"')
        uurl=pattern.findall(myResponse)[0]
        print(uurl,"歌曲下载url")
        #download_url=song_dirt['data']['play_url']
        download_url=uurl.replace("\\","")
        
        if download_url:
            try:
                # 根据音乐url地址，用urllib.request.retrieve直接将远程数据下载到本地
                #urllib.request.urlretrieve(download_url, 'd:/music/' + song['song_name'] + '.mp3')
                #print('Successfully Download:' + song['song_name'] + '.mp3')
                print("正在下载歌曲，请等待")
                res2=requests.get(download_url,headers=headers,cookies=cookies).content
                #with open("D:/music/1.mp3","wb") as f11:

                #   f11.write(res2)
                with open("d:\\music\\{}.mp3".format(song['song_name'].split("-")[1]),"wb") as f:

                    f.write(res2)
                    time.sleep(0.5)
                print("歌曲已下载完成，请欣赏")
            except Exception as e :
                print('Download wrong~',e)
               


if __name__ == '__main__':
    kugou=KuGou()
    while True:
        keyword=input('请输入要下载的歌曲名：')
        print('-----------歌曲《'+keyword+'》的版本列表------------')
        music_list=kugou.get_music_list(keyword)
        song_num=input('请输入要下载的歌曲序号：')
        a=music_list[int(song_num)-1]
        print("闯过来的url:",a)
        kugou.download(a)

#https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery191014794547761396992_1592548350710&hash=5D979B171AC34D82006555E150881A69&album_id=37596377&dfid=1afPDy0EU2Uh0k7wfd3EBPIt&mid=81f8a6c26d1868b05aecc8ee2bc8bf7c&platid=4&_=1592548350720
#https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=5D979B171AC34D82006555E150881A69&album_id=37596377


