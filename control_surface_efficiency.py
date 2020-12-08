#! /usr/bin/python
# -*- coding:utf-8 -*-
"""
功能：计算舵面效率值，并且给出横航向静安定度随迎角变化曲线。
版本：0.1
作者：高峰
"""

import numpy as np
import pandas as pd
import os

os.chdir(r"D:\Program\aerodynamic_cruve\new\longitudinal\WING1-ELEVATOR-DI")
colnames = ["CL", "CD", "CM", "MX", "MY", "CZ", "Q", "alpha", "beta", "K"]

elev_10 = np.genfromtxt("161.DAT", skip_header=1, skip_footer=1)
df_elev_10 = pd.DataFrame(elev_10)
df_elev_10.columns = colnames

elev_0 = np.genfromtxt("161A.DAT", skip_header=1, skip_footer=1)
df_elev_0 = pd.DataFrame(elev_0)
df_elev_0.columns = colnames

elev_n10 = np.genfromtxt("162.DAT", skip_header=1, skip_footer=1)
df_elev_n10 = pd.DataFrame(elev_n10)
df_elev_n10.columns = colnames

elev_n20 = np.genfromtxt("163.DAT", skip_header=1, skip_footer=1)
df_elev_n20 = pd.DataFrame(elev_n20)
df_elev_n20.columns = colnames

elev_n30 = np.genfromtxt("164.DAT", skip_header=1, skip_footer=1)
df_elev_n30 = pd.DataFrame(elev_n30)
df_elev_n30.columns = colnames

# 计算舵面效率
dz_elev_n30 = (df_elev_n30-df_elev_0)/30
dz_elev_n30["alpha"] = df_elev_0["alpha"]
dz_elev_n30.to_csv("dz_elev_n30.txt", sep='\t', header=None, columns=None, index=0)

dz_elev_n20 = (df_elev_n20-df_elev_0)/20
dz_elev_n20["alpha"] = df_elev_0["alpha"]
dz_elev_n20.to_csv("dz_elev_n20.txt", sep='\t', header=None, columns=None, index=0)

dz_elev_n10 = (df_elev_n10-df_elev_0)/10
dz_elev_n10["alpha"] = df_elev_0["alpha"]
dz_elev_n10.to_csv("dz_elev_n10.txt", sep='\t', header=None, columns=None, index=0)

dz_elev_10 = -(df_elev_10-df_elev_0)/10
dz_elev_10["alpha"] = df_elev_0["alpha"]
dz_elev_10.to_csv("dz_elev_10.txt", sep='\t', header=None, columns=None, index=0)


