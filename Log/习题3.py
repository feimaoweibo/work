#!user/bin/env python3
# -*- coding: gbk -*-
#���ݲ�ͬ�ĺ�����ʹ��װ���������벻ͬ����־��Ϣ
import logging
log_format = "%(asctime)s------ %(levelname)s ----%(message)s"
logging.basicConfig(format=log_format, filename="ϰ��3.log")
def log(zhi):
    def lianxi(func):
        def wrapper(*args, **kwargs):
            logging.warning(zhi)
            return func(*args, **kwargs)
        return wrapper
    return lianxi

@log("����lstest�ı���")
def lstest():
    print("�������1�ĺ������")
@log("����lstest2�ı���")
def lstest2():
    print("�������2�ĺ������")
lstest()
lstest2()