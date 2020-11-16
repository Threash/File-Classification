'''
Author: your name
Date: 2020-11-16 16:37:09
LastEditTime: 2020-11-16 18:59:57
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefinedc:/Users/Administrator/Desktop/File classification.py
'''


import os
import sys
import shutil
list = os.listdir(os.getcwd())


def create_dir_not_exist(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)


print(os.getcwd())
print(sys.argv[0])
for item in list:
    if os.path.isfile(item) and sys.argv[0].split('\\')[-1] != item:
        dir = item[item.rfind('.') + 1:]
        if dir != item:
            create_dir_not_exist(dir)
            shutil.move(item, dir)
