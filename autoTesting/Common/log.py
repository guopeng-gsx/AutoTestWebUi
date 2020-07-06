import logging,time
from Common.seting import project_path
#用字典保存日志级别
format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
}


# 开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件
class Logger():
    def __init__(self, loglevel, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        self.log_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

        self.log_path = project_path() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_time)
        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__=='__main__':
    log = Logger(loglevel=1, logger="fox").getlog()
    log.info('ddddddd')
#
# # 创建一个logger
# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
#
# # 创建一个handler，用于写入日志文件
# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.DEBUG)
#
# # 再创建一个handler，用于输出到控制台
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
#
# # 定义handler的输出格式
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # 给logger添加handler
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 记录一条日志
# logger.info('foorbar')