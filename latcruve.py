# 纵向数据曲线绘图

import os
import eacruve


def latcruve(floder, flag):
    os.chdir(floder)
    # 风洞试验数据

    legend = []
    if flag == "EA":
        with open("EA.legend") as file:
            for line in file:
                legend.append(line.strip())

        while '' in legend:
            legend.remove('')

    plot_flag = "lat"
    label_list = legend
    rx4e = eacruve.PlotAerodynamicProfile(floder, plot_flag, label_list, "EA")
    rx4e.read_file()
    rx4e.plot()

latcruve(r"D:\Program\aerodynamic_cruve\wind_tunnel\lateral-directional\AILERON-L\A=0", "EA")