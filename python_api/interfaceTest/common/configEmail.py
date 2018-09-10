import os
import smtplib                      # smtplib封装了简单的smtp协议
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import readConfig as readConfig
from common.Log import MyLog
import zipfile
import glob

localReadConfig = readConfig.ReadConfig()

class Email:
    def __init__(self):
        global host,user,password,port,sender,title,content             # 定义全局变量，邮件信息
        host = localReadConfig.get_email("email_host")
        user = localReadConfig.get_email("mail_user")
        password = localReadConfig.get_email("mail_pass")
        port = localReadConfig.get_email("mail_port")
        sender = localReadConfig.get_email("sender")
        title = localReadConfig.get_emali("subject")
        content = localReadConfig.get_email("content")
        self.value = localReadConfig.get_email("receiver")
        self.receiver = []
        # get receiver_list
        for n in str(self.value).split("/"):                            # 遍历取出收件人
            self.receiver.append(n)
        # defined email_subject
        date = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        self.subject = title + "" + date
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_file(self):


