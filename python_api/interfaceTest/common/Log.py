
#为方便写log的时候方便，单独启用一个线程
#主要是对输出日志的一些操作，包括输出格式的规定，输出等级的定义以及其他一些输出的定义
#python标准库是在安装python时自动安装的，不用再下载，而第三方库是之后下载的

import logging
from datetime import datetime
import threading                                    # 单独启用一个线程，在写log的时候会比较方便
from interfaceTest import readConfig
import os

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")

        if not os.path.exists(resultPath):      # 判断是否存在结果文件夹，如果不存在，则创建一个结果文件
            os.mkdir(resultPath)

        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))      # 通过本地时间定义测试结果文件名称

        if not os.path.exists(logPath):         # 判断是否存在测试结果文件，如果不存在，则创建一个文件
            os.mkdir(logPath)

        self.logger = logging.getLogger()       # 定义logger,如果参数为空，则默认为返回Root对象

        self.logger.setLevel(logging.INFO)      # setLevel方法设置日志级别为“INFO”，信息

        handler = logging.FileHandler(os.path.join(logPath, "output.log"))      # 定义handler

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')   #定义formatter

        handler.setFormatter(formatter)         # 定义formatter

        self.logger.addHandler(handler)         # 添加handler

class MyLog:                                    # 将日志添加到线程之中
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log