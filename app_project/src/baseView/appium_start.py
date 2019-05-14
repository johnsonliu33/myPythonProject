import subprocess
from time import strftime
from app_project.src.baseView.appium_port import check_port, release_port
from app_project.src.util.app_log import my_log


def check_stats(host, port):
    """"判断端口是否占用，若被占用就task kill port"""
    if check_port(host, port):  # 判断port端口是否被占用
        return True
    elif release_port(port):  # 重置port端口
        return True


def appium_start(host, port):
    logger = my_log()
    if check_stats(host, port):  # 注释掉，不会每次都重启appium
        bootstrap_port = str(port + 1)
        # 启动多个appium服务时，不要安装客户端
        # npm install -g cnpm --registry=https://registry.npm.taobao.org
        # cnpm install -g appium
        cmd = "start /b appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)
        # 说明：/b 不打开命令窗口; bp端口（ --bootstrap-port）是appium和设备之间通信的端口，如果不指定到时无法操作多台设备运行脚本。
        logger.info("{} at {}".format(cmd, strftime("%Y-%m-%d %H:%M:%S")))
        subprocess.Popen(cmd, shell=True, stdout=open("./appium_log/" + str(port) + ".log", "a"),
                         stderr=subprocess.STDOUT)
        return True


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    for i in range(2):
        port = 4723 + 2 * i
        appium_start(host, port)
