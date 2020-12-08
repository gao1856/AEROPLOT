#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
功能：计算横航向静安定度
版本：0.1
作者：高峰
"""

import numpy as np
import pandas as pd
import os


path = r"D:\Program\aerodynamic_cruve\new\lateral-directional\AILERON-L"

def efficiency_beta(folder_name):
    colnames = ["CL", "CD", "CM", "MX", "MY", "CZ", "Q", "alpha", "beta", "K"]

    path1 = path + "\\" + folder_name
    os.chdir(path1)
    file_list = os.listdir(path1)
    file_list = filter(lambda ifile: ".DAT" in ifile, file_list)

    # print(list(file_list))
    temp = []
    res = []
    for ifile in file_list:
        # print(ifile)
        np_temp = np.genfromtxt(ifile, skip_header=1, skip_footer=2)
        df_temp = pd.DataFrame(np_temp)
        df_temp.columns = colnames
        temp.append(df_temp)
        x = df_temp.loc[[0, 1, 2], "beta"]
        y = df_temp.loc[[0, 1, 2], "CZ"]

        reg = np.polyfit(x, y, 1)
        res.append(reg[0])
        # df_reg = pd.DataFrame(reg)
        # df_reg.to_csv(ifile.split(".")[0]+".txt", sep='\t', header=None, columns=None, index=0)

    # 效率
    d10 = (temp[1] - temp[0]) / 10
    d20 = (temp[2] - temp[0]) / 20

    print(d10.mean()["MX"],d20.mean()["MX"])

    # print(res)
    df_res = pd.DataFrame([res])
    df_res.to_csv(folder_name+".txt", sep='\t', header=None, columns=None, index=0)

efficiency_beta("A=-4")
efficiency_beta("A=0")
efficiency_beta("A=2")
efficiency_beta("A=4")
efficiency_beta("A=6")
efficiency_beta("A=8")
efficiency_beta("A=10")
efficiency_beta("A=12")
efficiency_beta("A=14")
efficiency_beta("A=15")
efficiency_beta("A=16")







