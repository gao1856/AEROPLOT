# 纵向数据曲线绘图
import numpy as np

import os
import eacruve


def loncruve(floder, flag):
    os.chdir(floder)
    # 风洞试验数据

    legend = []
    if flag == "EA":
        with open("EA.legend") as file:
            for line in file:
                legend.append(line.strip())

        while '' in legend:
            legend.remove('')

    plot_flag = "lon"
    label_list = legend
    rx4e = eacruve.PlotAerodynamicProfile(floder, plot_flag, label_list, "EA")
    rx4e.read_file()
    rx4e.plot()

# loncruve(r"D:\Program\aerodynamic_cruve\wind_tunnel\longitudinal\elevator", "EA")