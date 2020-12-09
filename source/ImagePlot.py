import matplotlib.pyplot as plt
import numpy as np
import os


class Image(object):
    # 图片中包括：x坐标轴，y坐标轴，图例，曲线。
    def __init__(self, x, y, xlabel, ylabel, legend, savepath):
        self.x = x  # x数据
        self.y = y  # y数据
        self.xlabel = xlabel  # xlabel，比如r"$C_L$"
        self.ylabel = ylabel  # ylabel，比如r"$\alpha$"
        self.legend = legend  # 图例
        self.savepath = savepath  # 保存路径，文件名

        # 本程序在一个图中最多绘制13条曲线。
        self.makerlist = ['o', 'p', 's', '*', 'D', 'x', '>', '<', 'v', '+', '^', 'P', 'X']

    def ticks2label(self, ticks, tlabel):
        newticks = list(map(str, ticks))
        newticks[-1] = tlabel
        return newticks

    def myticks(self, data):
        # data 即x或者y数据，为二维数组，找到里面的最大值和最小值
        ticksmax = np.max(data)
        ticksmin = np.min(data)
        # 以5或者0.5，或者0.005形成一个列表，最大最小值包含在其中。
        flag = 5
        while True:
            temp = (ticksmax - ticksmin) // flag
            # 当marjor grid的数量大于2才执行下列代码
            if temp >= 2:
                newticksmax = (ticksmax // flag + 1) * flag
                newticksmin = (ticksmin // flag) * flag

                if (newticksmax - ticksmax) / flag < 0.2:
                    newticksmax = newticksmax + flag
                if -(newticksmin - ticksmin) / flag < 0.2:
                    newticksmin = newticksmin - flag

                newticksmax = newticksmax + flag
                flaglen = int(len(str(flag))) - 1
                myticks = np.arange(newticksmin, newticksmax, flag)
                myticks = np.round(myticks, flaglen)
                return myticks
            flag = flag / 10

    def plot(self):
        # x,y 为准备画图的数据。为列表，x列表的数据和y列表的数据一一对应。
        # 创建画布，给出画布的尺寸，画布上1个子图，画占用画布的范围
        fig, ax = plt.subplots(1, 1, figsize=(8, 5), tight_layout=([0.1, 0.9, 0.1, 0.9]))
        for i in range(len(self.x)):
            # 画图
            ax.plot(self.x[i], self.y[i], color='k', marker=self.makerlist[i], linestyle='-',
                    linewidth=1.5, markersize=5, label=self.legend[i])
        # 设置图例位置以及大小等等参数
        ax.legend(loc=0, fontsize=12)
        # 设置minorticks显示
        ax.minorticks_on()
        # 设置ticks朝向
        ax.tick_params(axis='both', which='both', direction='in')
        # 设置xticks
        xticks = self.myticks(self.x)
        xtickslabel = self.ticks2label(xticks, self.xlabel)
        ax.set_xticks(xticks)
        # 设置xtickslabel
        ax.set_xticklabels(xtickslabel, fontdict=None, minor=False, fontsize=16)
        # 设置yticks
        yticks = self.myticks(self.y)
        ytickslabel = self.ticks2label(yticks, self.ylabel)
        ax.set_yticks(yticks)
        # 设置ytickslabel
        ax.set_yticklabels(ytickslabel, fontdict=None, minor=False, fontsize=16)

        # 打开网格
        ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # x坐标轴的网格使用主刻度
        ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # y坐标轴的网格使用次刻度
        ax.xaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # x坐标轴的网格使用主刻度
        ax.yaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # y坐标轴的网格使用次刻度
        fig.savefig(self.savepath, dpi=300)


def longitudinal_plot(floder, legend):
    # 准备数据
    os.chdir(floder)
    file = filter(lambda x: ".DAT" in x, os.listdir())
    file = list(file)
    file.sort(key=lambda x: int(x[9:-4]))

    CLdata = [ ]
    CDdata= [ ]
    Cmdata = [ ]
    alphadata = [ ]
    Kdata = [ ]

    for ifile in file:
        temp = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
        CLdata.append(temp[:, 0])
        CDdata.append(temp[:, 1])
        Cmdata.append(temp[:, 2])
        alphadata.append(temp[:, 7])
        Kdata.append(temp[:, 9])

    # 创建一个图片对象   x, y, xlabel, ylabel, legend, savepath

    CL_alpha = Image(alphadata, CLdata, r"$\alpha$", r"$C_L$", legend, "CL~alpha.jpeg")
    CL_alpha.plot()
    CL_CD = Image(CDdata, CLdata, r"$C_D$", r"$C_L$", legend, "CL~CD.jpeg")
    CL_CD.plot()
    CD_alpha = Image(alphadata, CDdata, r"$\alpha$", r"$C_D$", legend, "CD~alpha.jpeg")
    CD_alpha.plot()
    Cm_alpha = Image(alphadata, Cmdata, r"$\alpha$", r"$C_m$", legend, "Cm~alpha.jpeg")
    Cm_alpha.plot()
    K_alpha = Image(alphadata, Kdata, r"$\alpha$", r"$K$", legend, "K~alpha.jpeg")
    K_alpha.plot()
    K_CL = Image(CLdata, Kdata, r"$C_L$", r"$K$", legend, "K~CL.jpeg")
    K_CL.plot()
    Cm_CL = Image(CLdata, Cmdata, r"$C_L$", r"$C_m$", legend, "Cm~CL.jpeg")
    Cm_CL.plot()


def lateral_directional_plot(floder, legend):
    # legend 中添加alpha。
    # 准备数据
    os.chdir(floder)
    file = filter(lambda x: ".DAT" in x, os.listdir())
    file = list(file)
    file.sort(key=lambda x: int(x[9:-4]))

    Cldata = [ ]
    Cndata = [ ]
    CYdata = [ ]
    betadata = [ ]

    for ifile in file:
        temp = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
        CLdata.append(temp[:, 0])
        CDdata.append(temp[:, 1])
        Cmdata.append(temp[:, 2])
        Cldata.append(temp[:, 3])
        Cndata.append(temp[:, 4])
        CYdata.append(temp[:, 5])
        Qdata.append(temp[:, 6])
        alphadata.append(temp[:, 7])
        betadata.append(temp[:, 8])
        Kdata.append(temp[:, 9])

    # 创建一个图片对象   x, y, xlabel, ylabel, legend, savepath

    Cl_beta = Image(betadata, Cldata, r"$\beta$", r"$C_l$", legend, "Cl~beta.jpeg")
    Cl_beta.plot()
    Cn_beta = Image(betadata, Cndata, r"$\beta$", r"$C_n$", legend, "Cn~beta.jpeg")
    Cn_beta.plot()
    CY_beta = Image(betadata, CYdata, r"$\beta$", r"$C_Y$", legend, "CY~beta.jpeg")
    CY_beta.plot()

# 纵向绘图
# floder = r"D:\Pyprogram\AEROPLOT\data"
# legend = [r"$\delta_e=-30^\circ$", r"$\delta_e=-20^\circ$", r"$\delta_e=-10^\circ$",
#           r"$\delta_e=0^\circ$", r"$\delta_e=10^\circ$"]
# longitudinal_plot(floder, legend)


# 横航向绘图，需要在legend加入alpha
floder = r"D:\Pyprogram\AEROPLOT\data"
legend = [r"$\alpha=0^\circ \delta_e=-30^\circ$",
          r"$\alpha=0^\circ \delta_e=-20^\circ$",
          r"$\alpha=0^\circ \delta_e=-10^\circ$",
          r"$\alpha=0^\circ \delta_e=0^\circ$",
          r"$\alpha=0^\circ \delta_e=10^\circ$"]
lateral_directional_plot(floder, legend)

# 计算Clbeta,Cnbeta,CYbeta,并绘制其随迎角的变化。


# 计算三个舵面效率，并绘制其随迎角的变化。

