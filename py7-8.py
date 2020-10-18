#股票提醒系统 tushare
import tushare 
import time
import smtplib
from email.mime.text import MIMEText
#获取股票数据
def getrealtimedata(share):
    dataNow=tushare.get_realtime_quotes(share.code)
    share.name=dataNow.loc[0][0]

    share.price=float(dataNow.loc[0][3])
    share.high=dataNow.loc[0][4]
    share.low=dataNow.loc[0][5]
    share.volumn=dataNow.loc[0][8]
    share.amount=dataNow.loc[0][9]
    share.openToday=dataNow.loc[0][1]
    share.pre_close=dataNow.loc[0][2]
    share.timee=dataNow.loc[0][30]
    share.describe="股票名："+share.name+"当前价格："+str(share.price)
    return share
#print(dataNow)
#print(name)

#发送邮件
def sendemail(subject,content):
    
    msg_from ="wzl13686114760@126.com" #发送方
    pwd="GSRRKVWKBJEEWHUN"
    to="1977840861@qq.com"
    #构造邮件
    #msg=MIMEText(content,"html","utf-8") #msg邮件对象
    msg=MIMEText(content) #msg邮件对象
    msg["Subject"]=subject
    msg["From"]=msg_from
    msg["To"]=to
#发送邮件
    try:
        ss=smtplib.SMTP_SSL("smtp.126.com",465)
        ss.login(msg_from,pwd)
        ss.sendmail(msg_from,to,msg.as_string())#发送
        print("发送成功")
    except Exception as e:
        print("发送失败!详情：",e)





   
#股票类
class Share():
    def __init__(self,code,buy,sale):
        self.name=""

        self.price=""
        self.high=""
        self.low="" 
        self.volumn=""
        self.amount=""
        self.openToday=""
        self.pre_close=""
        self.timee=""
        self.describe=""
        self.code=code
        self.buy=buy
        self.sale=sale
def main(sharelist):
    for share in sharelist:

        
        sss=getrealtimedata(share)
        print(sss.describe)
        buy=sss.buy #买点
        sale=sss.sale  #卖点
        if sss.price<=buy:


            print("达到买点，如果有钱请赶紧买!")
            sendemail("达到买点",sss.describe)
        elif sss.price>=sale:
            print("达到卖点，如果有货请赶紧卖")
            sendemail("达到卖点",sss.describe)
        else :
            print("别买也别卖")
        
while 1==1:
    share1=Share("600106",2.4,3.2)
    share2=Share("601988",3.5,3.8)
    share3=Share("000591",3.3,3.5)
    print("------------")
    list1=[share1,share2,share3]
    main(list1)
    time.sleep(30)






