import subprocess
from time import ctime
import multiprocessing
from app_project.baseView.check_port import check_port, release_port


def appium_start(host, port):
    checkPort = check_port(host, port)

    if checkPort:
        bootstrap_port = str(port + 1)
        cmd = "start /b appium -a " + host + " -p " + str(port) + " -bp " + str(bootstrap_port)
        print("{} at {}".format(cmd, ctime()))
        subprocess.Popen(cmd, shell=True, stdout=open("./appium_log/" + str(port) + ".log", "a"),
                         stderr=subprocess.STDOUT)
    else:
        killPort = release_port(port)
        if killPort:
            appium_start(host, port)



appium_process = []

for i in range(2):
    host = "127.0.0.1"
    port = 4723 + 2 * i
    appium = multiprocessing.Process(target=appium_start, args=(host, port))
    appium_process.append(appium)

if __name__ == '__main__':
    for app in appium_process:
        app.start()
    for app in appium_process:
        app.join()
