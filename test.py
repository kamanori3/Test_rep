# -*- coding: utf-8 -*-

import csv   #csvモジュールをインポートする
import os
import shutil

f = open('C:\\Users\\kaman_000\\Desktop\\list.csv','r', encoding='utf-8')

dataReader = csv.reader(f)

s_dir="d:\\Users\\kaman_000\\Documents\\80 書籍\\evernote移動済み\\"
t_dir="C:\\Users\\kaman_000\\Desktop\\test\\"

for row in dataReader:
    print(row)
    shutil.copy(s_dir + "".join(row),t_dir + "".join(row))

