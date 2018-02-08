# -*- coding:utf-8 -*- -
import re
import os


ANDROID_PATH = ''
import sys
import json
import pypinyin
from pypinyin import lazy_pinyin
from pypinyin import pinyin
from androguard.core.bytecodes.apk import APK
reload(sys)
sys.setdefaultencoding('gbk')
def get_listener_num(path):
    tot_num = 0
    r = re.compile(r'->setOn.*Listener|->addOn.*Listener')
    for root, dirs, files in os.walk('D:\Ubicomp\EX1//test//1_1\smali', 'rb'):
        for file in files:
            if 'android' in root: continue
           # if 'alipay' in root:continue
            #print file
            file_path = os.path.join(root,file)
            f = open(file_path)
            m1 = re.findall(r, f.read())

            if len(m1) == 0: continue
            print file_path
            print m1
            print root
            return
            tot_num = tot_num + len(m1)
            print tot_num

def unpack_pkg():
    cnt = 0
    path = 'D:\Ubicomp\EX1\pkglist'
    for root, dirs, files in os.walk(path, 'rb'):
        for file in files:
            if 'unpack2.py' in file: continue
            if 'unpack-wxapkg.php' in file: continue
            cnt = cnt + 1
            print cnt
            file_path = os.path.join(root,file)
            os.chdir(path)
            os.system('php unpack-wxapkg.php %s'%file)

def get_img_size_pkg():
    cnt = 0
    path = 'D:\Ubicomp\EX1\pkglist\\'
    list = os.listdir(path)
    table = {}
    for name in list:
        if 'unpack2.py' in name: continue
        if 'unpack-wxapkg.php' in name: continue
        if '.unpacked' in name:
            print name
            l1 = name.split('.')
            name_nu = int(l1[0])
            cnt = cnt + 1
            tot = 0
            num = 0
            for root, dirs, files in os.walk(path+name, 'rb'):
                for file in files:
                    file_dir = os.path.join(root,file)
                    #print file_dir +'---'
                    if '.png' in file or '.jpg' in file or '.jpge' in file or '.gif' in file:
                        #print file
                        size = os.path.getsize(file_dir)
                        #print size
                        tot = tot + size
                        num = num + 1
               # break
            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['byte'] = tot
            table[name_nu]['num'] = name_nu
            table[name_nu]['kb'] = tot*1.0/1024
            table[name_nu]['mb'] = tot*1.0/(1024*1024)
            #break
            #if cnt > 2: break
        else:
            continue
    fsave = open('D:\Ubicomp\EX1//ans//imgsize_pkg.txt','w')
    ll = sorted(table.items(),key=lambda d:d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1],ensure_ascii=False)+'\n')
def get_img_size_apk():
    cnt = 0
    path = 'D:\Ubicomp\EX1\\applist\\'
    list = os.listdir(path)
    table = {}
    for name in list:
        if '.unzip' in name:
            print name
            l1 = name.split('_')
            name_nu = int(l1[0])
            cnt = cnt + 1
            print cnt
            tot = 0
            num = 0
            for root, dirs, files in os.walk(path+name, 'rb'):
                for file in files:
                    file_dir = os.path.join(root,file)
                    if '.png' in file or '.jpg' in file or '.jpge' in file or '.gif' in file:
                        size = os.path.getsize(file_dir)
                        tot = tot + size
                        num = num + 1
               # break
            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['byte'] = tot
            table[name_nu]['num'] = name_nu
            table[name_nu]['img_num'] = num
            table[name_nu]['kb'] = tot*1.0/1024
            table[name_nu]['mb'] = tot*1.0/(1024*1024)
        else:
            continue
        #break

    fsave = open('D:\Ubicomp\EX1//ans//apk_imgsize.txt','w')
    ll = sorted(table.items(),key=lambda d:d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1],ensure_ascii=False)+'\n')
def get_page_num_pkg():
    cnt = 0
    path = 'D:\Ubicomp\EX1\pkglist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:

        if 'unpack2.py' in name: continue
        if 'unpack-wxapkg.php' in name: continue
        if '.unpacked' in name:
            l1 = name.split('.')
            name_nu = int(l1[0])
            print name
            file_dir = path+name+'\\app-config.json'
            f = open(file_dir)
            r = eval(f.read())
            pages = r['pages']

            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['page_num'] = len(pages)
            table[name_nu]['num'] = name_nu

        else:
            continue

    fsave = open('D:\Ubicomp\EX1//ans//pkg_page_num.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def get_pkg_size():
    cnt = 0
    path = 'D:\Ubicomp\EX1\pkglist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:

        if 'unpack2.py' in name: continue
        if 'unpack-wxapkg.php' in name: continue
        if '.unpacked' in name: continue
        if '.wxapkg_dir' in name: continue
        l1 = name.split('.')
        name_nu = int(l1[0])
        print name
        size = os.path.getsize(path+name)
        print size
        table[name_nu] = {}
        table[name_nu]['name'] = name
        table[name_nu]['byte'] = size
        table[name_nu]['kb'] = size*1.0/1024
        table[name_nu]['mb'] = size*1.0/(1024*1024)
        table[name_nu]['num'] = name_nu

    fsave = open('D:\Ubicomp\EX1//ans//pkg_size.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def get_apk_size():
    cnt = 0
    path = 'D:\Ubicomp\EX1//applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        l1 = name.split('_')
        name_nu = int(l1[0])
        print name
        size = os.path.getsize(path+name)
        print size
        table[name_nu] = {}
        table[name_nu]['name'] = name
        table[name_nu]['byte'] = size
        table[name_nu]['kb'] = size*1.0/1024
        table[name_nu]['mb'] = size*1.0/(1024*1024)
        table[name_nu]['num'] = name_nu

    fsave = open('D:\Ubicomp\EX1//ans//apk_size.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')
def get_bindtap_num():
    cnt = 0
    path = 'D:\Ubicomp\EX1\pkglist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:

        if 'unpack2.py' in name: continue
        if 'unpack-wxapkg.php' in name: continue
        if '.unpacked' in name:
            l1 = name.split('.')
            name_nu = int(l1[0])
            print name
            try:
                file_dir = path+name+'\\app-wxss.js'
                f = open(file_dir)
            except:
                file_dir = path + name + '\\page-frame.html'
                f = open(file_dir)
            r = re.compile(r"'bindtap'")
            m1 = re.findall(r, f.read())
            print len(m1)
            table[name_nu] = {}
            table[name_nu]['bindtap_num'] = len(m1)
            table[name_nu]['name'] = name
            table[name_nu]['num'] = name_nu

        else:
            continue
        #break

    fsave = open('D:\Ubicomp\EX1//ans//pkg_bindtap_num.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def unzip_apk():
    print 'unzip'
    cnt = 0
    path = 'D:\Ubicomp\EX1//applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        if os.path.isfile(path + name) == True:
            l1 = name.split('_')
            name_nu = int(l1[0])
            print name
            cnt = cnt + 1
            print cnt
            os.chdir(path)
            os.system('7z.exe x -r -y -aos -o"%s" "%s"'%(path+name+'.unzip',path+name))
            os.system('apktool.bat d %s' % (path + name))
            # break
def unpack_apk():
    cnt = 0
    path = 'D:\Ubicomp\EX1//applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        if os.path.isfile(path + name) == True:
            l1 = name.split('_')
            name_nu = int(l1[0])
            print name
            if name == '101_33dazhongdianping.apk': continue
            cnt = cnt + 1
            print cnt
            os.chdir(path)
            os.system('apktool.bat d %s'%(path+name))
            #break

def get_activity_num():
    path = 'D:\Ubicomp\EX1//applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        l1 = name.split('_')
        name_nu = int(l1[0])
        if os.path.isfile(path+name) == True:

            print name

            try:
                a = APK(path + name)
                acnum = len(a.get_activities())
                table[name_nu] = {}
                table[name_nu]['name'] = name
                table[name_nu]['activity_num'] = acnum
                table[name_nu]['num'] = name_nu
            except Exception as e:
                print 'fail!!!!'
                print name
                continue
            #break

    fsave = open('D:\Ubicomp\EX1//ans//apk_activity_num.txt', 'w')
    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def get_spec_activity_num():
    f = open('D:\Ubicomp\EX1//applist//4_3mogujie//AndroidManifest.xml')
    #print f.read()
    r = re.compile(r'<activity')
    m1 = re.findall(r, f.read())
    print '4_3mogujie'
    print len(m1)


    f3 = open('D:\Ubicomp\EX1//applist//83_30xiaomishangcheng//AndroidManifest.xml')
    #print f.read()
    r = re.compile(r'<activity')
    m1 = re.findall(r, f3.read())
    print '83_30xiaomishangcheng'
    print len(m1)

def get_listener_num():
    cnt = 0
    path = 'D:\Ubicomp\EX1\\applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        if os.path.isfile(path+name) == True: continue
        elif '.unzip' in name: continue
        else:
            print name
            cnt = cnt + 1
            print cnt
            l1 = name.split('_')
            name_nu = int(l1[0])
            inlist = os.listdir(path+name)
            total = 0
            for inname in inlist:
                if 'smali' in inname:
                    for root, dirs, files in os.walk(path + name+'\\'+inname, 'rb'):
                        for file in files:
                            file_dir = os.path.join(root, file)
                            if 'android' in file_dir: continue
                            try:
                                ff = open(file_dir)
                                r = re.compile(r'->setOn.*Listener|->addOn.*Listener')
                                m1 = re.findall(r, ff.read())
                                total = total + len(m1)
                            except: continue
                            #print total
            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['num'] = name_nu
            table[name_nu]['listener_num'] = total
            print total


    fsave = open('D:\Ubicomp\EX1//ans//apk_listener_num.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def getp_apk():
    cnt = 0
    path = 'D:\Ubicomp\EX1\\applist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        if os.path.isfile(path + name) == True:
            continue
        elif '.unzip' in name:
            cnt = cnt + 1
            print cnt
            l1 = name.split('_')
            name_nu = int(l1[0])
            inlist = os.listdir(path + name)
            code_size = 0
            dir_size = 0
            lib_size = 0
            print name
            for root, dirs, files in os.walk(path + name, 'rb'):
                for file in files:
                    file_dir = os.path.join(root, file)
                    dir_size = dir_size + os.path.getsize(file_dir)

            for inname in inlist:
                if 'classes' in inname:
                    code_size = code_size + os.path.getsize(path+name+'\\'+inname)
                    print code_size
                if 'lib'in inname:
                    for root, dirs, files in os.walk(path+name+'\\'+inname, 'rb'):
                        for file in files:
                            file_dir = os.path.join(root, file)
                            print file_dir
                            lib_size = lib_size + os.path.getsize(file_dir)


            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['num'] = name_nu
            table[name_nu]['dir_size'] = dir_size
            table[name_nu]['code_size'] = code_size
            table[name_nu]['lib_size'] = lib_size

            #break
        else: continue


    fsave = open('D:\Ubicomp\EX1//ans//apk_p.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')

def getp_pkg():
    cnt = 0
    path = 'D:\Ubicomp\EX1\\pkglist\\'
    list = os.listdir(path)
    table = {}
    false = False
    true = True
    for name in list:
        if os.path.isfile(path + name) == True:
            continue
        elif '.unpacked' in name:
            cnt = cnt + 1
            print cnt
            l1 = name.split('.')
            name_nu = int(l1[0])
            inlist = os.listdir(path + name)
            code_size = 0
            dir_size = 0
            print name
            for root, dirs, files in os.walk(path + name, 'rb'):
                for file in files:
                    file_dir = os.path.join(root, file)
                    dir_size = dir_size + os.path.getsize(file_dir)

            for inname in inlist:
                if 'app-service.js' in inname:
                    code_size = code_size + os.path.getsize(path + name + '\\' + inname)
                    print code_size

            table[name_nu] = {}
            table[name_nu]['name'] = name
            table[name_nu]['num'] = name_nu
            table[name_nu]['dir_size'] = dir_size
            table[name_nu]['code_size'] = code_size

            #break
        else:
            continue

    fsave = open('D:\Ubicomp\EX1//ans//pkg_p.txt', 'w')

    ll = sorted(table.items(), key=lambda d: d[0])
    for i in ll:
        print i[1]
        fsave.write(json.dumps(i[1], ensure_ascii=False) + '\n')
if __name__ == "__main__":
    getp_apk()
    #getp_pkg()
    #a = APK('D:\Ubicomp\EX1//meipian.apk')
    #print a.get_main_activity()

    #get_listener_num()
    #get_spec_activity_num()
    #get_img_size_apk()
    #unzip_apk()
    #from androguard.core.bytecodes.apk import APK

    #a = APK('D:\Ubicomp\EX1//applist//4_3mogujie.apk')
    #a.get_activities()
    #print 'activity'
    #print 'unpack'
    #unpack_apk()
    #get_activity_num()
    #get_apk_size()
    #get_bindtap_num()
    #get_pkg_size()
    #get_page_num_pkg()
    #get_img_size_pkg()
    #init()
    #get_listener_num()
