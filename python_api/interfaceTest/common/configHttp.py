import requests
import readConfig as readConfig
from Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):                     # 基地址+路径=url
        self.url = host + url

    def set_headers(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self,file):
        self.files = file


    def get(self):                               # 定义get请求方式
        try:
            response = requests.get(self.url, param=self.params, headers=self.headers, timeout=float(timeout))
            return response                          # 返回响应值
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    def post(self):                              # 定义post请求
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
