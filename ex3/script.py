# -*- coding:utf-8 -*- -
import re
import os
import shlex, subprocess
import re
import threading
import time
import signal


def setup_phone():
    os.system('adb shell "rm -rf /data/local/tmp/*"')
    os.system('adb push haos /data/local/tmp')
    os.system('adb shell "chmod 0755 /data/local/tmp/haos"')
    os.system('adb shell "ls -l /data/local/tmp/haos"')
    os.system('adb shell "mkdir -p /data/local/tmp/local/tmp"')

def get_app_info(apk_name):

    # 获取label和包名

    comand_line = 'aapt dump badging "%s"' % apk_name
    get_package_name_sub = subprocess.Popen(shlex.split(comand_line), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                            shell=True)
    out, error = get_package_name_sub.communicate()
    # print out
    ret = re.findall(r"application-label:'.*'", out)
    ll = ret[0].split("'")
    label_name = ll[1]

    ret = re.findall(r"package: name='.*'", out)
    ll = ret[0].split("'")
    package_name = ll[1]

    f = open('app.info','w')
    f.write(package_name+'\n')
    f.write(label_name)
    #f.close()

    os.system('adb push app.info /data/local/tmp/')

def install(apk_name):

    comand_line = 'adb install "%s"' % apk_name
    install_apk_sub = subprocess.Popen(shlex.split(comand_line), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       shell=True)
    out, error = install_apk_sub.communicate()

    if 'Failure' in out:
        print '安装失败'
        if 'INSTALL_FAILED_ALREADY_EXISTS' in out:
            print '重复安装'
            gd = 1
        else:
            gd = 1
    elif 'Success' in out:
        print '安装成功'

def run(apk_name):

    os.system('run.sh')
    os.system('adb push bin/TestApp.jar /data/local/tmp/')
    content = os.popen('adb shell /data/local/tmp/haos runtest TestApp.jar -c nsl.stg.tests.LaunchApp').read()

def slove(apk_name):

    get_app_info(apk_name)
    run(apk_name)

if __name__ == '__main__':

    """
    PUMA_PATH = 'D:\Bwork\ontry\PUMA-master'
    os.chdir(PUMA_PATH)

    slove("Lazada Online Shopping Deals_v6.0.3_apkpure.com.apk")
    """

    """
    t = threading.Timer(5.0, sayhello)
    t.start()
    """




