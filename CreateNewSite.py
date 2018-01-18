# @File  : CreateNewSite.py
# @Author: PuJi
# @Date  : 2018/1/3 0003

import sys

# ZeroNet Modules
import zeronet


def main():
    sys.argv = [sys.argv[0]]+["getConfig"]+sys.argv[1:]
    zeronet.main()

if __name__ == '__main__':
    main()
