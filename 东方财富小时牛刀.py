import requests
import json
#  https://curl.trillworks.com/#
cookies = {
    'cowCookie': 'true',
    'qgqp_b_id': '76713a0aa88330cdb1af1f6326f1baca',
    'intellpositionL': '1215.35px',
    'st_si': '70983385315634',
    'st_sn': '1',
    'st_psi': '20200701175017664-113300300813-3177462434',
    'st_asi': 'delete',
    'st_pvi': '77912688609722',
    'st_sp': '2020-07-01^%^2017^%^3A50^%^3A18',
    'st_inirUrl': '',
    'intellpositionT': '1249.4px',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '53119902^')
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('http://push2.eastmoney.com/api/qt/clist/get?pn=1^&pz=50^&po=1^&np=1^&ut=b2884a393a59ad64002292a3e90d46a5^&fltt=2^&invt=2^&fid0=f4001^&fid=f62^&fs=m:0+t:6+f:^!2,m:0+t:13+f:^!2,m:0+t:80+f:^!2,m:1+t:2+f:^!2,m:1+t:23+f:^!2,m:0+t:7+f:^!2,m:1+t:3+f:^!2^&stat=1^&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^&rt=53119902^&cb=jQuery18307354047121553535_1593597065871^&_=1593597066355', headers=headers, cookies=cookies)
# print(response.text)
companies = []
prices = []
ups = []
code = []
data = json.loads(response.text)
dict1 = data.get('data').get('diff')
for i in dict1:
    # print(i)
    
    share_1=i.get('f184')   # 主力净流入净占比大于10
    share_2=i.get('f2')  #  每股单价小于20
    share_3=i.get('f3')  # 今日涨幅大于5
    if share_1>=10 and share_2<=30 and share_3>5:  #获得满足条件的数据
        companies.append(i.get('f14'))      #公司名称
        prices.append(i.get('f2'))    # 最新单价
        ups.append(i.get('f3'))          #单日涨幅
        code.append(i.get('f12')) 

print('公司名称',companies)
print('股票代号',code)
print('最新价',prices)
print('单日涨幅',ups)
# 第二部 数据可视化
from pyecharts.charts import Bar
bar = Bar()
bar.add_xaxis(companies)
bar.add_yaxis('股价图',prices)

bar.render("股价图.html")
