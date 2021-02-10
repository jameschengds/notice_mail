import json
import logging
import time

from notice_offer.get_status import get_status
from notice_offer.mail import send_mail

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    resp = get_status()
    send_mail({"msg": "开始监听状态", "info": "当前状态为" + str(json.loads(resp.text)[0].get("status"))})
    while resp.status_code == 200:
        data = json.loads(resp.text)[0].get("status")
        if data != "Application Submitted":
            send_mail({"msg":"申请状态变化","info":"当前状态为"+str(data)})
            logging.info("发送状态变化邮件")
        time.sleep(60)
        resp = get_status()
        logging.info("监听中")

    send_mail({"msg": "查询失败", "info": ""})
    logging.info("查询失败，退出")