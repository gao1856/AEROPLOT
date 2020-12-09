
import matplotlib.pyplot as plt
import numpy as np
import os


def fun_plot(x, y, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath):
    # x,y 为准备画图的数据。为列表，x列表的数据和y列表的数据一一对应。
    # 图标列表，图中最多支持13条曲线。
    markerlist= ['o', 'p', 's', '*', 'D', 'x', '>', '<', 'v', '+', '^', 'P', 'X']
    # 创建画布，给出画布的尺寸，画布上1个子图，画占用画布的范围
    fig, ax = plt.subplots(1, 1, figsize=(8, 5), tight_layout=([0.1, 0.9, 0.1, 0.9]))

    for i in range(len(x)):
    # 画图
        ax.plot(x[i], y[i], color='k', marker=markerlist[i], linestyle='-',
                linewidth=1.5, markersize=5, label=labellist[i])
    # 设置图片的名称
    # ax.set_title("CL-a",fontsize=20)
    # 设置x轴名称
    # ax.set_xlabel('alpha', fontsize=18,fontfamily = 'sans-serif',fontstyle='italic')
    # 设置y轴名称
    # ax.set_ylabel('CL', fontsize='x-large', fontstyle='oblique')

    # 设置图例位置以及大小等等参数
    ax.legend(loc=0, fontsize=12)

    # 设置图像的长宽比
    # ax.set_aspect(3)

    # 设置minorticks显示
    ax.minorticks_on()
    # 设置ticks朝向
    ax.tick_params(axis='both',which='both',direction='in')

    # 设置xticks
    ax.set_xticks(xticks)
    # print("========================")
    # print(xticks)
    # print("========================")
    # 设置xtickslabel
    ax.set_xticklabels(xtickslabel, fontdict=None, minor=False, fontsize=16)
    # 设置yticks
    ax.set_yticks(yticks)
    # 设置ytickslabel
    ax.set_yticklabels(ytickslabel, fontdict=None, minor=False, fontsize=16)

    # 设置xy轴的范围
    # ax.set_xlim(-5, 20)
    # ax.set_ylim(-0.5, 2)
    # 打开网格
    ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # y坐标轴的网格使用次刻度
    ax.xaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # y坐标轴的网格使用次刻度
    # print("11112222211111111")
    # plt.show()
    fig.savefig(savepath, dpi=300)
    # print("11111333333333333333333111111")
    # 保存图片


# xytickslabel = [r"$C_L$", r"$C_D$", r"$C_m$", r"$C_l$", r"$C_n$", r"$C_Y$",
#               r"$\alpha$", r"$\beta$",
#               r"$C_l^\beta$", r"$C_n^\beta$", r"$C_Y^\beta$",
#               r"$C_m^{\detla_e}$", r"$C_l^{\detla_a}$", r"$C_n^{\detla_r}$"]
# 准备数据
# 分为纵向绘图和横航向绘图。
# 纵向：CL~alpha;CL~CD;CD-alpha;Cm~alpha;Cm~CL;k~alpha;k~CL
# 横航向：1 每个迎角下均绘制 Cl-beta;Cn~beta;CY~beta;
#        2 Clb~alpha;Cnb~alpha;CYb~alpha;

# yticks = [0, 0.05, 0.1, 0.15, 0.2, 0.25]
# ytickslabel = ["0", "0.05", "0.1", "0.15", "0.2", r"$C_D$"]
# 将ticks列表转为tickslabel，并将最后一个转为特殊符号。
def ticks2label(ticks, tlabel):
    newticks = list(map(str, ticks))
    newticks[-1] = tlabel
    # newticks.append(tlabel)
    print(newticks)
    return newticks


def myticks(ticks):
    # ticks 为二维数组，找到里面的最大值和最小值
    ticksmax = np.max(ticks)
    ticksmin = np.min(ticks)
    # 以5或者0.5，或者0.005形成一个列表，最大最小值包含在其中。
    flag = 5
    while True:
        temp = (ticksmax - ticksmin) // flag
        # 当marjor grid的数量大于2才执行下列代码
        if temp >= 2:
            newticksmax = (ticksmax // flag + 1) * flag
            newticksmin = (ticksmin // flag) * flag

            if (newticksmax-ticksmax) / flag < 0.2:
                newticksmax = newticksmax + flag
            if -(newticksmin - ticksmin) / flag < 0.2:
                newticksmin = newticksmin - flag

            newticksmax = newticksmax + flag
            flaglen = int(len(str(flag))) - 1
            myticks = np.arange(newticksmin, newticksmax, flag)
            myticks = np.round(myticks, flaglen)
            return myticks
        flag = flag/10


os.chdir(r"D:\Pyprogram\AEROPLOT\data")
file = filter(lambda x: ".DAT" in x, os.listdir())
file = list(file)
file.sort(key=lambda x: int(x[9:-4]))

CLdata = [ ]
CDdata= [ ]
Cmdata = [ ]
Cldata = [ ]
Cndata = [ ]
CYdata = [ ]
Qdata = [ ]
alphadata = [ ]
betadata = [ ]
kdata = [ ]

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
    kdata.append(temp[:, 9])


labellist = [r"$\delta_e=-30^\circ$", r"$\delta_e=-20^\circ$",r"$\delta_e=-10^\circ$",
             r"$\delta_e=0^\circ$", r"$\delta_e=10^\circ$"]

# 绘制CL~alpha曲线
savepath = "CL~alpha.jpeg"
xticks = myticks(alphadata)
print("==============is:", xticks)
xtickslabel = ticks2label(xticks, r"$\alpha$")
yticks = myticks(CLdata)
ytickslabel = ticks2label(yticks, r"$C_L$")
fun_plot(alphadata, CLdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制CD~alpha曲线
savepath = "CD~alpha.jpeg"
xticks = myticks(alphadata)
xtickslabel = ticks2label(xticks, r"$\alpha$")
yticks = myticks(CDdata)
ytickslabel = ticks2label(yticks, r"$C_D$")
fun_plot(alphadata, CDdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制Cm~alpha曲线
savepath = "Cm~alpha.jpeg"
xticks = myticks(alphadata)
xtickslabel = ticks2label(xticks, r"$\alpha$")
yticks = myticks(Cmdata)
ytickslabel = ticks2label(yticks, r"$C_m$")
fun_plot(alphadata, Cmdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制k~alpha曲线
savepath = "k~alpha.jpeg"
xticks = myticks(alphadata)
xtickslabel = ticks2label(xticks, r"$\alpha$")
yticks = myticks(kdata)
ytickslabel = ticks2label(yticks, r"$K$")
fun_plot(alphadata, kdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制k~CL曲线
savepath = "k~CL.jpeg"
xticks = myticks(CLdata)
xtickslabel = ticks2label(xticks, r"$C_L$")
yticks = myticks(kdata)
ytickslabel = ticks2label(yticks, r"$K$")
fun_plot(CLdata, kdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制k~CL曲线
savepath = "Cm~CL.jpeg"
xticks = myticks(CLdata)
xtickslabel = ticks2label(xticks, r"$C_L$")
yticks = myticks(Cmdata)
ytickslabel = ticks2label(yticks, r"$C_m$")
fun_plot(CLdata, Cmdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
# 绘制CL~CD曲线
savepath = "CL~CD.jpeg"
xticks = myticks(CDdata)
xtickslabel = ticks2label(xticks, r"$C_D$")
yticks = myticks(CLdata)
ytickslabel = ticks2label(yticks, r"$C_L$")
fun_plot(CDdata, CLdata, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)




