# -*- coding:utf-8 -*-
import os,urllib2

def downloadBAT():
    url='https://raw.githubusercontent.com/wkcn/SYSULAB/master/AddENV.bat'
    try:
        content = urllib2.urlopen(url).read()
        f = open("AddENV.bat", "w")
        f.write(content)
        f.close()
        return True
    except Exception, e:
        return False


def main():
    if downloadBAT():
        need = r"E:\nasm" # 要添加的环境变量，没有空格
        cmd = '%s\\AddENV.bat %s' % (os.getcwd(), need)
        # print cmd
        ret = os.popen(cmd).readlines()
        # print ret
        return 0
    else:
        return 1

if __name__ == '__main__':
    main()