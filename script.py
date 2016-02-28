# -*- coding:utf-8 -*-
import os

def downloadBAT():
    url = ""


def main():
    downloadBAT()
    need = r"E:\nasm"
    cmd = '%s\\AddENV.bat %s' % (os.getcwd(), need)
    print cmd
    # ret = os.popen(cmd).readlines()
    # print ret
    return 0

if __name__ == '__main__':
    main()