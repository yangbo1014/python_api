#配置文件

import os                                                   #对文件或目录进行操作
import codecs
import configparser                                         #使用该模块的类ConfigParser使配置文件生效

proDir = os.path.split(os.path.realpath(__file__))[0]   #获取当前脚本所在路径并分割存入字典，取路径
configPath = os.path.join(proDir, "config.ini")         #将路径与文件名拼接

class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):                          #获取email中的具体key的value值
        value = self.cf.get("Email", name)
        return value

    def get_http(self, name):                           #获取http名称，get(section、option)
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):                      #获取数据库名称, https://my.oschina.net/u/3041656/blog/793467
        value = self.cf.get("database", name)
        return value
