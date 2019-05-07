import subprocess
from time import ctime


def appium_start(host, port):
    bootstrap_port = str(port + 1)
    # 启动多个appium服务时，不要安装客户端
    # npm install -g cnpm --registry=https://registry.npm.taobao.org
    # cnpm install -g appium
    cmd = "start /b appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)
    # 说明：/b 不打开命令窗口; bp端口（ --bootstrap-port）是appium和设备之间通信的端口，如果不指定到时无法操作多台设备运行脚本。
    print("{} at {}".format(cmd, ctime()))
    subprocess.Popen(cmd, shell=True, stdout=open("./appium_log/" + str(port) + ".log", "a"), stderr=subprocess.STDOUT)


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 4723
    for i in range(2):
        port = 4723 + 2 * i
        appium_start(host, port)
