
"""
对风洞试验结果数据进行绘图，主要包括纵向和横航向数据绘图。
所有的计算结果均放在统一文件夹下。
采用欧美坐标系绘图
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.font_manager as fm
from pylab import *
import os


class AeroCruve(object):
	# def __init__(self, folder, plot_flag, label_list, coordinate_flag):
	def __init__(self):
		# self.folder = folder
		# 设置曲线标识:lat表示横航向曲线，lon表示纵向曲线
		# self.plot_flag = plot_flag
        # 设置字体大小
		self.font_size = 15
        # 设置图片的大小
		self.figuresize = (1200, 1000)
		# self.label_list = label_list
        # 坐标系选择，欧美/中苏
		# self.coordinate_flag = coordinate_flag
        # 列名称
		self.name1 = ["C_L", "C_D", "C_m", "C_l", "C_n", "C_Y", "Q", "alpha", "beta", "K"]
		self.name2 = []

        # 设置字体, 每次绘图之前，修改图例。最多10条曲线。
		self.myfont = fm.FontProperties(fname=r'C:/Windows/Fonts/simkai.ttf', size=self.font_size)
		self.marker_list = ["o", "s", "^", "*", "D", "H", "<", ">", "V", "X"]
		self.cfd_data = []

	def read_file(self):
		# 列出文件夹下所有的目录与文件，并读取所有数据存储到DataFrame中
		path1 = r"D:\Program\aerodynamic_cruve\test"
		os.chdir(path1)
		file_list = os.listdir(path1)
		for i in file_list:
			if i == "ea.legend":
				file_list.remove(i)

		row = [-4.00, 0.00, 2.00, 4.00, 6.00, 8.00, 10.00, 12.00, 14.00, 15.00, 16.00]
		temp = pd.DataFrame(columns=(file_list),index=row)

		for ifile in file_list:
			data = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
			temp[ifile] = data[:,0]
		tt = temp.max(level=0)
		print(tt)
		mylegend = []

		for line in open("ea.legend"):
			mylegend.append(line.strip())

		print(mylegend)
		plt.figure(figsize=(6, 6.5))
		# ax = temp.plot(grid=True, legend=mylegend, marker=self.marker_list)
		# ax = plt.subplot(111)
		i= 0
		for index, col in temp.iteritems():
			print(len(col))
			print(len(index))
			ax = plt.plot(row, col, linewidth=2, marker=self.marker_list[i],
			markersize=10.0, color='k')
			i = i + 1
		# 打开网格
		plt.legend(prop=self.myfont, loc="best")
		# 打开网格
		ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=1)  # x坐标轴的网格使用主刻度
		ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=1)  # y坐标轴的网格使用次刻度
		ax.xaxis.grid(True, which='major', linestyle='-', linewidth=2, color='k')  # x坐标轴的网格使用主刻度
		ax.yaxis.grid(True, which='major', linestyle='-', linewidth=2, color='k')  # y坐标轴的网格使用次刻度

		# 刻度线超内
		ax.tick_params(which='both', direction='in')
		# 存储
		plt.savefig(outfile)
		# ax.figure(figsize = (5,5))
		# plt.legend(loc='best')
		plt.show()

"""
		data = np.genfromtxt("151.DAT", skip_header=1, skip_footer=1)
		test = pd.DataFrame(data, columns=self.name1)
		print(test)
		cfd_data_list = os.listdir(self.folder)

		temp = []
		for ifile in cfd_data_list:
			if ifile.split(".")[-1].upper() == "DAT":
				temp.append(ifile)
		cfd_data_list = temp

		for i in range(0, len(cfd_data_list)):
			path = os.path.join(self.folder, cfd_data_list[i])
			if os.path.isfile(path):
                #读取数据时默认去掉第一行和最后一行。
				temp = np.genfromtxt(path, skip_header=1, skip_footer=1)
				if self.coordinate_flag == "EA":
					print(temp[:, 4])
					temp[:, 4] = -temp[:, 4]

				self.cfd_data.append(temp)"""
"""

	def max_min_tick(self, num, tick):

		max, min = self.find_max_min(num)

		if (max - min) // tick > 4:
			max_temp = (max // tick + 1) * tick

			if abs(max - max_temp) < 0.2 * tick:
				max = (max // tick + 2) * tick
			else:
				max = max_temp

			min_temp = (min // tick) * tick

			if abs(min - min_temp) < 0.2 * tick:
				min = (min // tick - 1) * tick
			else:
				min = min_temp

		elif (max - min) // tick < 1:

			tick = 0.2 * tick
			max_temp = (max // tick + 1) * tick
			if abs(max - max_temp) < 0.2 * tick:
				max = (max // tick + 2) * tick
			else:
				max = max_temp

			min_temp = (min // tick) * tick
			if abs(min - min_temp) < 0.2 * tick:
				min = (min // tick - 1) * tick
			else:
				min = min_temp
		else:
			tick = 0.5 * tick
			max_temp = (max // tick + 1) * tick
			if abs(max - max_temp) < 0.2 * tick:
				max = (max // tick + 2) * tick
			else:
				max = max_temp

			min_temp = (min // tick) * tick
			if abs(min - min_temp) < 0.2 * tick:
				min = (min // tick - 1) * tick
			else:
				min = min_temp

		return max, min, tick

	def plot_fun(self, mdict, label_x, label_y, outfile):

		xnum, xxtick, ynum, yytick, legend_location, fig_size = self.mydict[mdict]

		max_x, min_x, xxtick = self.max_min_tick(xnum, xxtick)
		max_y, min_y, yytick = self.max_min_tick(ynum, yytick)

		# 图像定义
		# fig_vn = plt.figure(figsize=((max_x - min_x)*yytick*fig_size, (max_y - min_y)*xxtick*fig_size))
		fig_vn = plt.figure(figsize=(18, 11))
		ax = fig_vn.add_axes([0.06, 0.04, 0.92, 0.94])
		plt.xlim(min_x, max_x)
		plt.ylim(min_y, max_y)

		# 修改主刻度
		xmajorLocator = MultipleLocator(xxtick)  # 将x主刻度标签设置为5的倍数
		xmajorFormatter = FormatStrFormatter('%5.2f')  # 设置x轴标签文本的格式
		ymajorLocator = MultipleLocator(yytick)  # 将y轴主刻度标签设置为0.5的倍数
		ymajorFormatter = FormatStrFormatter('%1.2f')  # 设置y轴标签文本的格式

		# 设置主刻度标签的位置,标签文本的格式
		ax.xaxis.set_major_locator(xmajorLocator)
		ax.xaxis.set_major_formatter(xmajorFormatter)
		ax.yaxis.set_major_locator(ymajorLocator)
		ax.yaxis.set_major_formatter(ymajorFormatter)

		# 修改次刻度
		xminorLocator = MultipleLocator(xxtick/5)  # 将x轴次刻度标签设置为1的倍数
		yminorLocator = MultipleLocator(yytick/5)  # 将此y轴次刻度标签设置为0.1的倍数

		# 设置次刻度标签的位置,没有标签文本格式
		ax.xaxis.set_minor_locator(xminorLocator)
		ax.yaxis.set_minor_locator(yminorLocator)

		# 打开网格
		ax.xaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=1)  # x坐标轴的网格使用主刻度
		ax.yaxis.grid(True, which='minor', color='k', linestyle=':', linewidth=1)  # y坐标轴的网格使用次刻度
		ax.xaxis.grid(True, which='major', linestyle='-', linewidth=2, color='k')  # x坐标轴的网格使用主刻度
		ax.yaxis.grid(True, which='major', linestyle='-', linewidth=2, color='k')  # y坐标轴的网格使用次刻度

		# 刻度线超内
		ax.tick_params(which='both', direction='in')

		# 设置刻度的值
		x_list = np.linspace(min_x, max_x, (max_x - min_x)/xxtick + 1)
		xx_list = []
		for item in x_list:
			xx_list.append(str(item))

		xx_list[-1] = label_x

		y_list = np.linspace(min_y, max_y, (max_y - min_y)/yytick + 1)
		print((max_y - min_y))
		yy_list = []
		for item in y_list:
			yy_list.append(str(round(item, 3)))

		yy_list[-1] = label_y
		# print(yy_list)
		plt.xticks(x_list, xx_list, size=self.font_size)
		plt.yticks(y_list, yy_list, size=self.font_size)

		i = 0
		for idata in self.cfd_data:
			plt.plot(
				idata[:, xnum], idata[:, ynum], linewidth=2, marker=self.marker_list[i],
				markersize=10.0, color='k', label=self.label_list[i])
			i += 1

		# 图例
		plt.legend(prop=self.myfont, loc=legend_location)

		# 存储
		plt.savefig(outfile)



if __name__ == "__main__":
	print("绘制图形")

"""

rx4e = AeroCruve()
rx4e.read_file()
