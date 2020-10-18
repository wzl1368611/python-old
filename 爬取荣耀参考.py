import requests
import re
import threading


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}


def get_page(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('获取网页失败')
    except Exception as e:
        print(e)

def getname(webno):
    url = 'https://pvp.qq.com/web201605/herodetail/{i}.shtml'.format(i = webno)
    datas = get_page(url)
    data  = re.findall('<h2 class="cover-name">(.*?)</h2>', datas, re.S)
    s = "".join(data).encode('raw_unicode_escape').decode('gbk')
    return s

def download(html):
    try:
        pics = requests.get(html, headers=headers, timeout=10)  # 请求URL时间（最大10秒）
    except requests.exceptions.ConnectionError:
        print('您当前请求的URL地址出现错误')

    if pics.status_code != 404:
      no = html[-5]
      webno = html[-17:-14]
      name = getname(webno)
      fq = open('F:\\image\\' + (name + no + '.jpg'), 'wb')  # 下载图片，并保存和命名
      fq.write(pics.content)
      fq.close()
def down(y):
      urls = ['http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{i}/{i}-bigskin-{j}.jpg'.format(i =k+y, j= l+1) for k in range(30) for l in range(8)]
      for url in urls:
          download(url)


threads = []
try:
  t1 = threading.Thread(target=down, args=(500,))
  t1.start()
  threads.append(t1)
  t2 = threading.Thread(target=down, args=(100,))
  t2.start()
  threads.append(t2)
  t3 = threading.Thread(target=down, args=(130,))
  t3.start()
  threads.append(t3)
  t4 = threading.Thread(target=down, args=(160,))
  t4.start()
  threads.append(t4)
  t5 = threading.Thread(target=down, args=(190,))
  t5.start()
  threads.append(t5)
  for t in threads:
      t.join()
  print("退出主线程")
except:
   print ("Error: 无法启动线程")
