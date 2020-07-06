import os,configparser,re
from selenium import webdriver

def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]
    # return os.path.realpath(__file__)
    # return os.getcwd()
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path()+"config.ini")
    return config.get('testUrl', 'url')
def jiayinhaode_url():
    target_dir_temp_list1 = list(config_url())  # 先把字符串转成列表
    target_dir_temp_list1.insert(0, "\"")  # 把列表的第一位加上一个双引号
    target_dir_temp_str1 = "".join(target_dir_temp_list1)  # 转成字符串

    target_dir_temp_list1.append("\"")  # 加上最后一个双引号，再转成字符串
    target = "".join(target_dir_temp_list1)
    return target


    # return config.get('productUrl', 'url')
if __name__=='__main__':

    print("项目路径为："+project_path())
    print(config_url())
    print(jiayinhaode_url())

