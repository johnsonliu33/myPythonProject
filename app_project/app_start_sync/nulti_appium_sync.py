# -*-coding:utf-8-*-

import subprocess
from time import ctime
import multiprocessing
from app_project.app_start_sync.check_port import check_port, release_port


def appium_start(host, port):
    """启动appium命令"""
    bootstrap_port = str(port + 1)
    cmd = "start /b appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)
    print("{} at {}".format(cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open("./appium_log/" + str(port) + ".log", "a"),
                     stderr=subprocess.STDOUT)


def check_stats(host, port):
    """"判断端口是否占用，若被占用就kill"""

    checkPort = check_port(host, port)
    # print("port_tatus:", checkPort)
    if checkPort:
        appium_start(host, port)
    else:
        killPort = release_port(port)
        # print("port_kill:", killPort)
        if killPort:
            appium_start(host, port)


appium_process = []

for i in range(2):
    host = "127.0.0.1"
    port = 4723 + 2 * i
    appium = multiprocessing.Process(target=check_stats, args=(host, port))
    appium_process.append(appium)

if __name__ == '__main__':
    for app in appium_process:
        app.start()
    for app in appium_process:
        app.join()
