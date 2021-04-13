import random
import string
import json
import yaml
import datetime
import time


class Method:

    # 生成一个指定长度的随机字符串，其中
    #     string.digits=0123456789
    #     string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

    def generate_random_str(randomlength=4):
        # str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
        str_list = [random.choice(string.digits) for i in range(randomlength)]
        random_str = ''.join(str_list)
        return random_str

    @classmethod
    # 打印json格式
    def format(self, r):
        print(json.dumps(r.json(), indent=4, ensure_ascii=False))

    @classmethod
    # 封装加载yaml文件步骤
    def yaml_load(cls, path) -> list:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    @classmethod
    # 获取当前时间YYMMDDHHmmss
    def getLastTime(cls):
        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @classmethod
    # 获取当前日期YYMMDD
    def getLastDate(cls):
        return datetime.datetime.now().strftime('%Y%m%d')

    @classmethod
    # 获取当前时间：12.31 23:59:59
    def getDateTime(cls):
        return datetime.datetime.now().strftime('%m%d%H%M%S')

    @classmethod
    # 获取10位timestamp
    def getTimestamp(cls):
        return str(int(time.time()))

    @classmethod
    # 获取URL地址
    def get_url(cls):
        url = "http://smartesb-sit2.bankbkemobile.co.id:80/corebank"
        # url = "http://smartesb-sit1.bankbkemobile.co.id/payment"
        return url

    @classmethod
    # 获取BBW MOCK URL地址
    def get_bbw_url(cls):
        url = "http://bbwmock-sit2.bankbkemobile.co.id"
        # url = "http://bbwmock-sit1.bankbkemobile.co.id"
        return url
