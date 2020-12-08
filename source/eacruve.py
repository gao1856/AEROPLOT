"""
对风洞试验结果数据进行绘图，主要包括纵向和横航向数据绘图。
所有的计算结果均放在统一文件夹下。
采用欧美坐标系绘图
"""

import matplotlib as plt
import matplotlib.font_manager as fm
from pylab import *
import numpy as np
import os


class PlotAerodynamicProfile(object):
	def __init__(self, folder, plot_flag, label_list, coordinate_flag):
		self.folder = folder
		# 设置曲线标识:
		# lat:表示横航向曲线
		# lon:表示纵向曲线
		self.plot_flag = plot_flag
        # 设置字体大小
		self.font_size = 15
        # 设置图片的大小
		self.figuresize = (1200, 1000)
		self.label_list = label_list
		self.coordinate_flag = coordinate_flag

        # 设置字体, 每次绘图之前，修改图例。最多10条曲线。
		self.myfont = fm.FontProperties(fname=r'C:/Windows/Fonts/simkai.ttf', size=self.font_size)
		self.marker_list = ["o", "s", "^", "*", "D", "H", "<", ">", "V", "X"]
		self.cfd_data = []

		# 定义字典，曲线名对应xy参数，以及xy间隔，CFD计算结果数据
		self.mydict = {
			"cl-a": (7, 5, 0, 0.5, "lower right", 1),
			"cd-a": (7, 5, 1, 0.05, "upper left", 10),
			"cl-cd": (1, 0.05, 0, 0.5, "center right", 100),
			"cm-a": (7, 5, 2, 0.5, "lower left", 1),
			"cm-cl": (0, 0.5, 2, 0.5, "lower left", 10),
			"k-a": (7, 5, 9, 10, "lower right", 0.05),
			"k-cl": (0, 0.5, 9, 10, "lower right", 0.5),
			"cl-b": (8, 5, 3, 0.05, "upper right", 10), #副翼偏度时用
			# "cl-b": (8, 5, 3, 0.01, "upper right", 50), 方向舵偏度时用
			"cn-b": (8, 5, 4, 0.05, "lower center", 10),
			"cy-b": (8, 5, 5, 0.1, "lower right", 5)
			}

	def read_file(self):
		# 列出文件夹下所有的目录与文件，并读取所有数据到列表中
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

				self.cfd_data.append(temp)
		print("55555555555")



	def find_max_min(self, xnum):

		max_x = self.cfd_data[0][0, xnum]
		min_x = self.cfd_data[0][0, xnum]
		for idata in self.cfd_data:
			max_temp = max(idata[:, xnum])
			min_temp = min(idata[:, xnum])
			if max_temp > max_x:
				max_x = max_temp
			if min_temp < min_x:
				min_x = min_temp
		return max_x, min_x

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

	def plot(self):
		# 风洞试验结果，
		# 中苏每列数据依次为：Cy,Cx,mz,mx,my,Cz,q, a, b, k
		# 欧美每列数据依次为：CL,CD,Cm,Cl,Cn,CY,q, a, b, k
		# 欧美坐标系与中苏坐标系，Cn和my符号相反。
		# 对应的列编号为：0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		if self.plot_flag == "lon":
			# 绘制纵向曲线，7条
			# cy-a曲线
			self.plot_fun("cl-a", r"$\alpha$", r"$C_L$", "cl-a.png")
			# cd-a曲线
			self.plot_fun("cd-a", r"$\alpha$", r"$C_D$", "cd-a.png")
			# # cy-cd曲线
			self.plot_fun("cl-cd", r"$C_D$", r"$C_L$", "cl-cd.png")
			# # mz-a曲线
			self.plot_fun("cm-a", r"$\alpha$", r"$C_m$", "cm-a.png")
			# # mz-cy曲线
			self.plot_fun("cm-cl", r"$C_L$", r"$C_m$", "cm-cl.png")
			# # k-a曲线
			self.plot_fun("k-a", r"$\alpha$", r"$K$", "k-a.png")
			# # k-cy曲线
			self.plot_fun("k-cl", r"$C_L$", r"$K$", r"k-cl.png")

		elif self.plot_flag == "lat":
			# 绘制横航向曲线，3条
			# mx-b曲线
			self.plot_fun("cl-b", r"$\beta$", r"$C_l$", r"cl-beta.png")
			# my-b曲线
			self.plot_fun("cn-b", r"$\beta$", r"$C_n$", r"cn-beta.png")
			# cz-b曲线
			self.plot_fun("cy-b", r"$\beta$", r"$C_Y$", r"cy-beta.png")

		else:
			print("绘制nothing！！！")


if __name__ == "__main__":
	print("绘制图形")



