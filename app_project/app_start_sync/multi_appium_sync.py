# -*-coding:utf-8-*-

import subprocess
from time import strftime
import multiprocessing
from app_project.app_start_sync.appium_port import check_port, release_port
from app_project.common.app_log import my_log


def check_stats(host, port):
    """"判断端口是否占用，若被占用就task kill port"""
    if check_port(host, port):  # 判断port端口是否被占用
        return True
    elif release_port(port):  # 重置port端口
        return True


def appium_start(host, port):
    logger = my_log()
    # if True:
    if check_stats(host, port):  # 注释掉，不会每次都重启appium
        """启动appium命令"""
        bootstrap_port = str(port + 1)
        cmd = "start /b appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)
        logger.info("{} at {}".format(cmd, strftime("%Y-%m-%d %H:%M:%S")))
        subprocess.Popen(cmd, shell=True, stdout=open("./appium_log/" + str(port) + ".log", "a"),
                         stderr=subprocess.STDOUT)


def multi_appium(host, devices_list):
    # 构建进程组
    appium_pocess = []
    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        appium = multiprocessing.Process(target=appium_start, args=(host, port,))
        appium_pocess.append(appium)
    for app in appium_pocess:
        app.start()
    for app in appium_pocess:
        app.join()


if __name__ == '__main__':
    host = "127.0.0.1"
    devices_list = ["127.0.0.1:62001", "127.0.0.1:62025"]
    multi_appium(host, devices_list)
