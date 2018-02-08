
import json
import os
LIB = ['android/support/v4/',
       'org/apache/http/',
       'com/google/gson/',
       'com/google/zxing/'

       ]


def get_lib_size(output_dir, apk_dir):
    apk_dir = 'D:\Ubicomp\EX2//fuyou3.0.3//classes-dex2jar'
    f = open('ans.txt', 'rb')
    r = f.read()
    res = eval(r)
    library_path = []
    for item in res:
        path = item['cpn']
        library_path.append(path)

    no_lib_size = 0
    total_size = 0
    for root, dirs, files in os.walk(apk_dir, 'rb'):
        for file in files:
            file_path = os.path.join(root, file)
            total_size = total_size + os.path.getsize(file_path)
            flag = False
            for libs in library_path:
                file_path_change = file_path.replace('\\', '/')
                if libs in file_path_change:
                    flag = True
                    break
            if flag == True:
                gd = 1
            else:
                no_lib_size = no_lib_size + os.path.getsize(file_path)


    return total_size, no_lib_size
if __name__ == '__main__':

    get_lib_size('ans.txt','D:\Ubicomp\EX2//fuyou3.0.3//classes-dex2jar')
    total_size, no_lib_size = get_lib_size('ans.txt','D:\Ubicomp\EX2//fuyou3.0.3//classes-dex2jar')

    print total_size, no_lib_size
