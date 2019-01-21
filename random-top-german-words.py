#!/usr/bin/python
# -*- coding: UTF-8 -*-
from os import listdir
from os.path import isfile, join
import re
import distutils.dir_util
import random

print("""Please choose which word list to use:
1- Top 2000 words
2- Top 25k words
3- Top 50k words
""")

c = raw_input()
if c == "1":
    file_name = "./docs/top-2000.txt"
elif c == "2":
    file_name = "./docs/top-25k.txt"
elif c == "3":
    file_name = "./docs/top-50k.txt"

raw_data = open(file_name, 'r').read().decode("utf-8")
words_array = raw_data.split(',')

words_count = len(words_array)

print("Press ENTER to print new words, or CTRL+C to exit...")

while True:
    c = raw_input()
    if c == '':
        i = random.randint(1, words_count)
        print(words_array[i])
    else:
        break

exit()
