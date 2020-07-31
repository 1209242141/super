import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(smtpserver, port, sender, psw, receiver):
    # 写信模板
    msg=MIMEMultipart()
    msg['Subject']="这是ssp项目自动化报告"
    msg['From']=sender
    msg['to']=receiver
    # 通过os获取文件路径
    current_path=os.getcwd()# 获取当前脚本所在的文件夹路径
    print(current_path)
    annex_path=os.path.join(current_path,"report.html")# 附件内容的路径
    annex=open(annex_path,"r",encoding="utf-8").read()
    cur_path=os.path.join(current_path,"commen")
    print(cur_path)
    main_path=os.path.join(cur_path,"report.html")# 正文内容的路径
    main_body=open(main_path,"r",encoding="utf-8").read()
    # 添加正文到容器
    body=MIMEText(main_body,"html","utf-8")
    msg.attach(body)
    # 添加附件到容器
    att=MIMEText(annex,"base64","utf-8")
    att["Content-Type"]="application/octet-sream"
    att["Content-Disposition"]='attachment;filename="ssp_test_report.html"'
    msg.attach(att)
    # 连接发送邮件
    smtp=smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    send_email("smtp.qq.com", 465, "1209242141@qq.com", "sxystcfanazebage", "1209242141@qq.com")