#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0.py, for parse_video win vesion
# used on windows, with python3

# import
import sys
import subprocess

# main function
def main():
    # get python bin
    pybin = sys.executable
    # just start not.bat
    arg = ['o\\not.bat', pybin, 'o\\a.py']
    exit_code = subprocess.call(arg, shell=True)
    return exit_code

# start from main
if __name__ == '__main__':
    exit(main())

# end 0.py

