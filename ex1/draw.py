# -*- coding:utf-8 -*-
from matplotlib import *
import matplotlib.pyplot as plt
import numpy as np
import math
def show_shrink(X):
    #X = []
    Y = []

    for i in range(0,len(X)):
        Y.append(1.0/54.0)

    X = sorted(X)
    print X
    print Y


    plt.figure(figsize=(9, 6.5))
    YY = np.cumsum(Y)
    plt.xlabel('Code Reduction Size (MB)', fontsize=18)
    plt.ylabel('CDF', fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    #plt.title('Distribution of Code Re=',fontsize=18)
    plt.plot(X, YY,marker='d',linewidth=1,color='c')
    plt.show()

def package_size():
    f_apk = open('D:\Ubicomp\EX1//ans//apk_size.txt')
    f_pkg = open('D:\Ubicomp\EX1//ans//pkg_size.txt')

    y_apk = []
    y_pkg = []
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        #print res
        y_apk.append(res['mb'])
        #break
    while True:
        r = f_pkg.readline()
        if not r: break
        res = eval(r)
       # print res
        y_pkg.append(res['mb'])

    x = range(1,66)
    print len(y_apk)
    print len(y_pkg)
    print len(x)
   # plt.gca().set_yscale('log')
    plt.semilogy(x, y_apk, lw=1,color='r')
    plt.semilogy(x, y_pkg, lw=1,color='b')
    p2 = plt.scatter(x, y_apk, marker='*', color='r', label='Android Apps', s=30)
    p2 = plt.scatter(x, y_pkg, marker='.', color='b', label='Mini Programs', s=30)

    plt.xticks([1, 10, 20,  30, 40, 50, 60], [1, 10, 20,  30, 40, 50, 60],fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(linestyle="-.", color="#CDC5BF", linewidth=0.5)
    plt.legend(loc='lower left',edgecolor='black',fontsize=12)
    plt.xlabel('Mini Program Rank Number',fontsize=15)
    plt.ylabel('Installation Package Size (MByte)',fontsize=15)
    plt.savefig('ex1-compare-package-size.eps', format='eps', dpi=1000)
    plt.show()

def img_size():
    f_apk = open('D:\Ubicomp\EX1//ans//apk_imgsize.txt')
    f_pkg = open('D:\Ubicomp\EX1//ans//pkg_imgsize.txt')

    y_apk = []
    y_pkg = []
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        print res
        y_apk.append(res['mb'])
        # break
    while True:
        r = f_pkg.readline()
        if not r: break
        res = eval(r)
        print res
        y_pkg.append(res['mb'])
        # break
    #    print Y
    x = range(1, 66)
    ll = sorted(y_pkg)
    print ll
    plt.gca().set_yscale('log',basey=2)
    plt.semilogy(x, y_apk, lw=1, color='r',basey=10)
    plt.semilogy(x, y_pkg, lw=1, color='b',basey=10)
    p2 = plt.scatter(x, y_apk, marker='*', color='r', label='Android Apps', s=30)
    p2 = plt.scatter(x, y_pkg, marker='.', color='b', label='Mini Programs', s=30)

    plt.xticks([1, 10, 20, 30, 40, 50, 60], [1, 10, 20, 30, 40, 50, 60], fontsize=12)
 #  plt.yticks([0,0.5,1,10,100],[0,0.5,1,10,100],fontsize=12)
    plt.ylim(0,100)
    plt.grid(linestyle="-.", color="#CDC5BF", linewidth=0.5)
    plt.legend(loc='lower right',edgecolor='black',fontsize=12)
    plt.xlabel('Mini Program Rank Number', fontsize=15)
    plt.ylabel('Image Size(MByte)', fontsize=15)
    plt.savefig('ex1-compare-img-size.eps', format='eps', dpi=1000)
    plt.show()

def listener():
    f_apk = open('D:\Ubicomp\EX1//ans//apk_listener_num.txt')
    f_pkg = open('D:\Ubicomp\EX1//ans//pkg_bindtap_num.txt')

    y_apk = []
    y_pkg = []
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        print res
        y_apk.append(res['listener_num'])
        # break
    while True:
        r = f_pkg.readline()
        if not r: break
        res = eval(r)
        print res
        y_pkg.append(res['bindtap_num'])

    x = range(1, 66)
    p2 = plt.scatter(x, y_apk, marker='*', color='r', label='Android Apps', s=30)
    p2 = plt.scatter(x, y_pkg, marker='.', color='b', label='Mini Programs', s=30)

    plt.xticks([1, 10, 20, 30, 40, 50, 60], [1, 10, 20, 30, 40, 50, 60], fontsize=12)
    plt.grid(linestyle="-.", color="#CDC5BF", linewidth=0.5)
    plt.legend(loc='upper right',edgecolor='black',fontsize=12)
    #plt.legend(loc='upper right',bbox_to_anchor=(1.001,0.90),edgecolor='black')
    plt.xlabel('Mini Program Rank Number', fontsize=15)
    plt.ylabel('Listener Number', fontsize=15)
    plt.savefig('ex1-compare-listener-size.eps', format='eps', dpi=1000)
    plt.show()
def all():
    apk_img = []
    apk_code = []
    apk_lib = []
    apk_others=[]
    apk_lib_and_code = []
    cnt = 0
    f_apk_img = open('D:\Ubicomp\EX1//ans//apk_imgsize.txt','rb')
    imgTable = {}
    while True:
        r = f_apk_img.readline()
        if not r: break
        res = eval(r)
        imgTable[res['num']] = res['byte']

    f_apk = open('D:\Ubicomp\EX1//ans//apk_p.txt','rb')
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        #print res
        code = res['code_size']*1.0/(res['dir_size']*1.0)
        img = imgTable[res['num']]*1.0/(res['dir_size']*1.0)
        lib = res['lib_size']*1.0/(res['dir_size']*1.0)
        apk_lib_and_code.append(code+lib)
        apk_code.append(code)
        apk_img.append(img)
        apk_lib.append(lib)
        apk_others.append(1-code-img-lib)
        #break
    print apk_code
    print apk_code[25]
    N = 65
    ind = np.arange(N)  # the x locations for the groups
    print ind
    width = 0.5  # the width of the bars: can also be len(x) sequence
    print apk_code
    print apk_img
    plt.ylim(0, 1)
    p1 = plt.bar(ind, apk_code, width)
    p2 = plt.bar(ind, apk_lib, width, bottom=apk_code)
    p3 = plt.bar(ind, apk_img,width,bottom=apk_lib_and_code)
    plt.xlabel('Mini Program Rank Number', fontsize=15)
    plt.ylabel('Proportion', fontsize=15)
    plt.legend((p1[0], p2[0],p3[0]), ('Dalvik Byte Code', 'Dynamic Link Library','Images'),
               bbox_to_anchor=(0.35,1), ncol=2)
    plt.savefig('ex1-android_proportion.eps', format='eps', dpi=1000)
    plt.show()
def all_pkg():
    apk_img = []
    apk_code = []
    #apk_lib = []
    apk_others=[]
    #apk_lib_and_code = []
    cnt = 0
    f_apk_img = open('D:\Ubicomp\EX1//ans//pkg_imgsize.txt','rb')
    imgTable = {}
    while True:
        r = f_apk_img.readline()
        if not r: break
        res = eval(r)
        imgTable[res['num']] = res['byte']

    f_apk = open('D:\Ubicomp\EX1//ans//pkg_p.txt','rb')
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        #print res
        code = res['code_size']*1.0/(res['dir_size']*1.0)
        img = imgTable[res['num']]*1.0/(res['dir_size']*1.0)
        #lib = res['lib_size']*1.0/(res['dir_size']*1.0)
        #apk_lib_and_code.append(code+lib)
        apk_code.append(code)
        apk_img.append(img)
        #apk_lib.append(lib)
        apk_others.append(1-code-img)
        #break
    print apk_code
    print apk_code[25]
    N = 65
    ind = np.arange(N)  # the x locations for the groups
    print ind
    width = 0.5  # the width of the bars: can also be len(x) sequence
    print apk_code
    print apk_img
    plt.ylim(0, 1)
    p1 = plt.bar(ind, apk_code, width)
    #p2 = plt.bar(ind, apk_lib, width, bottom=apk_code)
    p2 = plt.bar(ind, apk_img,width,bottom=apk_code)
    plt.xlabel('Mini Program Rank Number', fontsize=15)
    plt.ylabel('Proportion', fontsize=15)
    plt.legend((p1[0], p2[0]), ('app-service.js','Images'),
               bbox_to_anchor=(0.33,1), ncol=1)
    plt.savefig('ex1-mini-program-proportion.eps', format='eps', dpi=1000)
    plt.show()
def page_num():
    f_apk = open('D:\Ubicomp\EX1//ans//apk_activity_num.txt')
    f_pkg = open('D:\Ubicomp\EX1//ans//pkg_page_num.txt')

    y_apk = []
    y_pkg = []
    while True:
        r = f_apk.readline()
        if not r: break
        res = eval(r)
        print res
        y_apk.append(res['activity_num'])
        # break
    while True:
        r = f_pkg.readline()
        if not r: break
        res = eval(r)
        print res
        y_pkg.append(res['page_num'])

    x = range(1, 66)
    p2 = plt.scatter(x, y_apk, marker='*', color='r', label='Android Apps', s=30)
    p2 = plt.scatter(x, y_pkg, marker='.', color='b', label='Mini Programs', s=30)

    plt.xticks([1, 10, 20, 30, 40, 50, 60], [1, 10, 20, 30, 40, 50, 60], fontsize=12)
    plt.grid(linestyle="-.", color="#CDC5BF", linewidth=0.5)
    plt.legend(loc='upper right', edgecolor='black', fontsize=12)
    # plt.legend(loc='upper right',bbox_to_anchor=(1.001,0.90),edgecolor='black')
    plt.xlabel('Mini Program Rank Number', fontsize=15)
    plt.ylabel('Page Number', fontsize=15)
    plt.savefig('ex1-compare-page-size.eps', format='eps', dpi=1000)
    plt.show()
if __name__ == '__main__':
    #img_size()
    #page_num()
    all()
    #all_pkg()
    #listener()
    #img_size()
    package_size()
