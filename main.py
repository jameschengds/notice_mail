import json
import logging
import time

import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_status():
    url = "https://jlu.radiusbycampusmgmt.com/ssc/applications/load.ssc?_dc=1612951226121&page=1&start=0&limit=25"

    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=AEB604E882BF7E4E3580EE7C747F2099'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response


def send_mail(data):
    # 邮件smtp的地址
    HOST = 'smtp.sina.com'
    # 定义邮件的标题
    SUBJECT = data.get("msg")
    # 发件人
    FROM = 'chengqxnull@sina.com'
    # 收件人
    To = '363852549@qq.com'
    # 发送的邮件文本内容
    TEXT = data.get("info")
    # 创建要发送的邮件正文及附件对象
    # related 使用邮件内嵌资源, 可以把附件中的图片等附件嵌入到正文中
    msg = MIMEMultipart('related')
    # 设置必要请求信息
    msg['From'] = FROM
    msg['T0'] = To
    msg['Subject'] = SUBJECT
    # 邮件正文
    msg.attach(MIMEText(TEXT))
    # 构造smtp服务对象，可以在构造对象时将host和port传入，可以直接连接服务器
    smtp_server = smtplib.SMTP()
    # # 开启发送debug模式，把发送邮件的过程显示出来
    smtp_server.set_debuglevel(1)
    # 连接邮箱服务器
    smtp_server.connect(host=HOST, port='25')
    # 登录邮箱服务器
    smtp_server.login(FROM, 'ecb16977ce666235')
    # 发送邮件
    smtp_server.sendmail(FROM, To, msg.as_string())
    # 关闭smtp服务器连接
    smtp_server.quit()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    resp = get_status()
    send_mail({"msg": "开始监听状态", "info": "当前状态为" + str(json.loads(resp.text)[0].get("status"))})
    while resp.status_code == 200:
        data = json.loads(resp.text)[0].get("status")
        if data != "Application Submitted":
            send_mail({"msg": "申请状态变化", "info": "当前状态为" + str(data)})
            logging.info("发送状态变化邮件")
        time.sleep(60)
        resp = get_status()
        logging.info("监听中")

    send_mail({"msg": "查询失败", "info": ""})
    logging.info("查询失败，退出")
