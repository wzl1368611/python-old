#邮件发送方（发送方地址，发送方客户端授权密码12344321a，SMTP服务器地址smtp.126.com)
#邮件内容  ZHYOLPBFOJIAAOQX
#邮件接收方 GSRRKVWKBJEEWHUN
import smtplib
from email.mime.text import MIMEText
msg_from ="wzl13686114760@126.com" #发送方
pwd="ZHYOLPBFOJIAAOQX"
to="1793268783@qq.com"
subject="毕业论文要求！"
content="今天一起去野餐非常期待！"
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