import os
import re

def rename(path):
    os.chdir(path)
    file_list = os.listdir(path)
    for ifile in file_list:
        new_name = re.findall(r"\d+", ifile)  # 提取所有整数
        os.rename(ifile, new_name[0]+".DAT")


path=r"D:\Program\aerodynamic_cruve\new\lateral-directional\RUDDER-L-H\RUDDR0-L"
rename(path)


