import os
import smtplib                      # smtplib封装了简单的smtp协议
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import threading
import readConfig as readConfig
from common.Log import MyLog
import zipfile                                                          # 对文件进行压缩处理
import glob                                                             # 对文件进行过滤处理

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
        date = datetime.now().strftime("%Y-%M-%d %H:%M:%S")             # 获取当前本地时间并格式化，datetime=date+time
        self.subject = title + "" + date
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()                             # log.get_logger???
        self.msg = MIMEMultipart('mixed')                               # 使用MIMEmultipart发送多个附件的邮件

    def config_header(self):                                            # 邮件发送配置信息头
        self.msg['subject'] = self.subject                              # 邮件主题，使用附件名作为主题
        self.msg['from'] = sender
        self.msg['to'] = ";".join(self.receiver)

    def config_(self):
        content_plain = MIMEText(content,'plain', 'utf-8')
        self.msg.attach(content_plain)


    def config_file(self):

        if self.check_file():                                            # 如果文件内容不为空，则配置该文件邮件
            reportpath = self.log.get_result_path()                      # self.log.get_result_path()是哪里来的？
            zippath = os.path.join(readConfig.proDir, "result", "test.zip")

            files = glob.glob(reportpath + "\*")                         # glob查找文件和目录
            '''filelist = glob.glob(r'./*.py');可查找到文件名为'./1.py','./2.py'''

            f = zipfile.Zipfile(zippath, 'w', zipfile.ZIP_DEFLATED)      #









