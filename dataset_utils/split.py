"""
@Author: HuKai
@Date: 2022/5/29  10:44
@github: https://github.com/HuKai97
"""
import os
from os import path
import random

import shutil
from shutil import copy2


import conf
home_dir = conf.get_home()
def get_dir(dir):
    return path.join(home_dir, dir)

trainfiles = os.listdir(get_dir(r"./Sampling_of_CCPD_files"))  #（图片文件夹）
trainfiles = trainfiles[:3000]
num_train = len(trainfiles)
print("num_train: " + str(num_train) )
index_list = list(range(num_train))
print(index_list)
random.shuffle(index_list)  # 打乱顺序
num = 0
trainDir = get_dir(r"./images/train")   #（将图片文件夹中的6份放在这个文件夹下）
validDir = get_dir(r"./images/val")     #（将图片文件夹中的2份放在这个文件夹下）
detectDir = get_dir(r"./images/test")   #（将图片文件夹中的2份放在这个文件夹下）

for dir in [trainDir, validDir, detectDir]:
    if not os.path.exists(dir):
        os.makedirs(dir)

for i in index_list:
    fileName = os.path.join(get_dir(r"./Sampling_of_CCPD_files"), trainfiles[i])  #（图片文件夹）+图片名=图片地址
    if num < num_train*0.7:  # 7:1:2
        print(str(fileName))
        copy2(fileName, trainDir)
    elif num < num_train*0.8:
        print(str(fileName))
        copy2(fileName, validDir)
    else:
        print(str(fileName))
        copy2(fileName, detectDir)
    num += 1
