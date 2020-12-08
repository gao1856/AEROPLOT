
import matplotlib.pyplot as plt
import numpy as np

# 准备数据
data = np.genfromtxt("elevator=0.DAT", skip_header=1, skip_footer=1)
xdata = data[:, 7]
ydata = data[:, 0]

# 创建画布，并详细设计坐标轴等参数,画占用画布的范围
fig, ax = plt.subplots(1, 1, figsize=(8, 5), tight_layout=([0.1, 0.9, 0.1, 0.9]))

# 画图
ax.plot(xdata, ydata, color='k', marker='o', linestyle='-', linewidth=1.5, markersize=6)
# 设置图片的名称
# ax.set_title("CL-a",fontsize=20)
# 设置x轴名称
# ax.set_xlabel('alpha', fontsize=18,fontfamily = 'sans-serif',fontstyle='italic')
# 设置y轴名称
# ax.set_ylabel('CL', fontsize='x-large', fontstyle='oblique')

# 设置图例位置以及大小等等参数
ax.legend(loc=0, fontsize=20)

# 设置图像的长宽比
# ax.set_aspect(3)

# 设置minorticks显示
ax.minorticks_on()
# 设置ticks朝向
ax.tick_params(axis='both',which='both',direction='in')

# 设置xticks
ax.set_xticks([0,4,8,12,16,20])
# 设置xtickslabel
ax.set_xticklabels(["0","4","8","12","16",r"$\alpha$"], fontdict=None, minor=False, fontsize=16)
# 设置yticks
ax.set_yticks([0,0.5,1.0,1.5,2.0])
# 设置ytickslabel
ax.set_yticklabels(["0.0","0.5","1.0","1.5",r"$C_L$"], fontdict=None, minor=False, fontsize=16)

# 设置xy轴的范围
ax.set_xlim(-5, 20)
ax.set_ylim(-0.5, 2)

# 打开网格
ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=0.5)  # y坐标轴的网格使用次刻度
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='major', linestyle='-', linewidth=1.0, color='gray')  # y坐标轴的网格使用次刻度

fig.savefig("test.jpg", dpi=300)
# 保存图片