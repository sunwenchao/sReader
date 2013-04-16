#coding: utf-8
__author__ = 'sunwenchao'

import os

dirname = os.path.dirname

def isRunYear(year):
    ret = False
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        ret = True
    return ret

# print isRunYear(2001)

# for v in range(1, 100):
#     isSu = True
#     for j in range(1, 100):
#         if j == 1 or j == v:
#             continue
#         if v % j == 0:
#             isSu = False
#     if isSu and v != 1:
#         print v

rootDir = dirname(dirname(dirname(__file__)))
print os.path.abspath(rootDir)
for root, dirs, files in os.walk(rootDir):
    print root, dirs, files