"""
对风洞试验结果数据进行绘图，主要包括纵向和横航向数据绘图。
采用中苏坐标系绘图
"""
import matplotlib as plt
import matplotlib.font_manager as fm
from pylab import *
import numpy as np
import os
import math

# 对文件名进行排序
def sort_key(s):
    # 排序关键字匹配
    # 匹配开头数字序号
    temp1 = s.split("=")[-1]
    temp2 = temp1.split(".")[0]
    return int(temp2)

# 导入数据，并进行简单处理
def read_file():
    wt_data = []
    tmp_max = 10*[0.0]
    tmp_min = 10*[0.0]
    file_list = os.listdir()
    print(file_list)

    data_file = filter(lambda x:".DAT" in x.upper(), file_list)
    data_file = sorted(list(data_file), key=sort_key)

    print(list(data_file))
    for ifile in data_file:
        # 如果
        tmp = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
        tmp_max_0 = np.max(tmp, axis=0)
        tmp_min_0 = np.min(tmp, axis=0)
        for i in range(0,len(tmp_max)):
            if tmp_max_0[i] > tmp_max[i]:
                tmp_max[i] = tmp_max_0[i]
            if tmp_min_0[i] < tmp_min[i]:
                tmp_min[i] = tmp_min_0[i]

        wt_data.append(tmp)

    # 返回风洞试验数据三维数组，每一列的最大值，最小值。
    return wt_data, tmp_max, tmp_min






# 绘制一张图片，给出定制方案，并保存
def plot_fun(xcol, ycol, label_x, label_y, xxtick, yytick, outfile):
    # 图像定义
    fig = plt.figure(figsize=(10, 6.2))
    ax = fig.add_axes([0.06, 0.06, 0.9, 0.9])
    # 设定字体大小
    fm.FontProperties(fname=r'C:/Windows/Fonts/simkai_0.ttf', size=12)
    # 中文图例显示
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    # 准备数据
    wt_data, col_max, col_min = read_file()

    # 主刻度设置
    max_x = (int(col_max[xcol] / xxtick + 0.5) + 1) * xxtick
    min_x = (int(col_min[xcol] / xxtick - 0.5) - 1) * xxtick
    max_y = (int(col_max[ycol] / yytick + 0.5) + 1) * yytick
    min_y = (int(col_min[ycol] / yytick - 0.5) - 1) * yytick
    print(max_y,min_y)
    print(math.ceil(col_max[ycol] / yytick),math.floor(col_min[ycol] / yytick))
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    # 修改主刻度
    xmajorLocator = MultipleLocator(xxtick)  # 将x主刻度标签设置为2的倍数
    xmajorFormatter = FormatStrFormatter('%5.2f')  # 设置x轴标签文本的格式
    ymajorLocator = MultipleLocator(yytick)  # 将y轴主刻度标签设置为0.5的倍数
    ymajorFormatter = FormatStrFormatter('%1.2f')  # 设置y轴标签文本的格式

    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)
    # 修改次刻度
    xminorLocator = MultipleLocator(xxtick / 5)  # 将x轴次刻度标签设置为5的倍数
    yminorLocator = MultipleLocator(yytick / 5)  # 将此y轴次刻度标签设置为5的倍数

    # 设置次刻度标签的位置,没有标签文本格式
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    # 打开网格
    ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # y坐标轴的网格使用次刻度
    ax.xaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # y坐标轴的网格使用次刻度

    # 刻度线超内
    ax.tick_params(which='both', direction='in')
    # marker 列表
    marker_list = ['o', 's', '*', 'D', 'x', '>', '<', 'v', 'p', '+','^', '1','2','3','4']
    # label 列表
    label_list = []
    for line in open("zs.legend"):
        label_list.append(line.strip())

    # 设置刻度的值
    x_list = np.linspace(min_x, max_x, int((max_x - min_x) / xxtick + 0.5) + 1)
    xx_list = []
    for item in x_list:
        xx_list.append(str(item))

    xx_list[-1] = label_x

    y_list = np.linspace(min_y, max_y, int((max_y - min_y) / yytick + 0.5) + 1)
    print((abs(max_y - min_y) / yytick))
    yy_list = []
    for item in y_list:
        yy_list.append(str(round(item, 3)))

    yy_list[-1] = label_y
    # print(yy_list)
    plt.xticks(x_list, xx_list,size=12)
    plt.yticks(y_list, yy_list,size=12)

    # 绘制图片
    i = 0
    for idata in wt_data:
        x = idata[:,xcol]
        y = idata[:,ycol]
        plt.plot(x, y, color='k', linewidth=1.5, linestyle='-',
                 markersize=6.0, marker=marker_list[i], label=label_list[i])
        i = i + 1

    plt.legend(loc='best', frameon=True, fontsize=12)
    plt.savefig(outfile,dpi=400)


# 绘制一系列图片
def wt_plot(plot_flag):
    if plot_flag == "lon":
        # 绘制纵向曲线，7条
        # cy-a曲线
        plot_fun(7,0,r"$\alpha$",r"$C_y$", 5, 0.5, "cy-a.png")
        # cx-a曲线
        plot_fun(7,1,r"$\alpha$",r"$C_x$", 5, 0.05, "cx-a.png")
        # # cy-cx曲线
        plot_fun(1,0,r"$C_x$",r"$C_y$", 0.05, 0.5, "cy-cx.png")
        # # mz-a曲线
        plot_fun(7,2,r"$\alpha$",r"$m_z$", 5, 0.5, "mz-a.png")
        # # mz-cy曲线
        plot_fun(0,2,r"$C_y$",r"$m_z$", 0.5, 0.5, "mz-cy.png")
        # # k-a曲线
        plot_fun(7,9,r"$\alpha$",r"$K$", 5, 5, "k-a.png")
        # # k-cy曲线
        plot_fun(0,9,r"$C_y$",r"$K$", 0.5, 5, "k-cy.png")

    elif plot_flag == "lat":
        # 绘制横航向曲线，3条
        # mx-b曲线
        plot_fun(8, 3, r"$\beta$", r"$m_x$", 5, 0.01, "mx-b.png")
        # my-b曲线
        plot_fun(8, 4, r"$\beta$", r"$m_y$", 5, 0.01, "my-b.png")
        # cz-b曲线
        plot_fun(8, 5, r"$\beta$", r"$C_z$", 5, 0.1, "cz-b.png")

    else:
        print("绘制nothing！！！")


# # # if "__name__" == "__main__":
# os.chdir(r"D:\Program\aerodynamic_cruve\new\lateral-directional\RUDDER-L-H\RUDDR0-L-A")
# wt_plot("lat")

