
import matplotlib.pyplot as plt
import numpy as np


def fun_plot(x, y, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath):
    # x,y 为准备画图的数据。为列表，x列表的数据和y列表的数据一一对应。
    # 图标列表，图中最多支持13条曲线。
    markerlist= ['o', 's', '*', 'D', 'x', '>', '<', 'v', 'p', '+', '^', 'P', 'X']
    # 创建画布，给出画布的尺寸，画布上1个子图，画占用画布的范围
    fig, ax = plt.subplots(1, 1, figsize=(8, 5), tight_layout=([0.1, 0.9, 0.1, 0.9]))

    for i in range(len(x)):
    # 画图
        ax.plot(x[i], y[i], color='k', marker=markerlist[i], linestyle='-',
                linewidth=1.5, markersize=6, label=labellist[i])
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
    # 设置xtickslabel
    ax.set_xticklabels(xtickslabel, fontdict=None, minor=False, fontsize=16)
    # 设置yticks
    ax.set_yticks(yticks)
    # 设置ytickslabel
    ax.set_yticklabels(ytickslabel, fontdict=None, minor=False, fontsize=16)

    # 设置xy轴的范围
    ax.set_xlim(-5, 20)
    ax.set_ylim(-0.5, 2)

    # 打开网格
    ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # y坐标轴的网格使用次刻度
    ax.xaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # y坐标轴的网格使用次刻度

    fig.savefig(savepath, dpi=300)
    # 保存图片



# 准备数据
x = []
y = []
data = np.genfromtxt("elevator=0.DAT", skip_header=1, skip_footer=1)
data1 = np.genfromtxt("elevator=10.DAT", skip_header=1, skip_footer=1)
x.append(data[:, 7])
y.append(data[:, 0])
x.append(data1[:, 7])
y.append(data1[:, 0])
labellist = [r"$\delta_e=0^\circ$", r"$\delta_e=10^\circ$"]
savepath = "test.jpeg"
xticks = [-5, 0, 5, 10, 15, 20]
xtickslabel = ["-5", "0", "5", "10", "15", r"$\alpha$"]
yticks = [-0.5, 0, 0.5, 1.0, 1.5, 2.0]
ytickslabel = ["-0.5", "0.0", "0.5", "1.0", "1.5", r"$C_L$"]
fun_plot(x, y, labellist, xticks, yticks, xtickslabel, ytickslabel, savepath)
