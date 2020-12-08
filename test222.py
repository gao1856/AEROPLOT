import os
import re

# def sort_key(s):
#     # 排序关键字匹配
#     # 匹配开头数字序号
#     temp1 = s.split("=")[-1]
#     temp2 = temp1.split(".")[0]
#     return int(temp2)
#
#
# path = r"D:\Program\aerodynamic_cruve\new\lateral-directional\RUDDER-L-H\RUDDR0-H-A"
# file_list = os.listdir(path)
# print(file_list)
# file_list = filter(lambda x: ".DAT" in x.upper(), file_list)
# temp = list(file_list)
# print(temp)
# temp = sorted(temp, key = sort_key)
# print(temp)