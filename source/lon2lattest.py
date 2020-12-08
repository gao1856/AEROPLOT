"""
对风洞试验结果数据结果进行转换，主要包括将纵向数据转换为横航向数据。
所有的计算结果均放在统一文件夹下。
"""

import numpy as np
import os

cfd_data = []

def lon2lat(folder):
	# 列出文件夹下所有的目录与文件
	cfd_data_list = os.listdir(folder)
	for i in range(0, len(cfd_data_list)):
		path = os.path.join(folder, cfd_data_list[i])
		if os.path.isfile(path):
			cfd_data.append(np.genfromtxt(path, skip_header=1, skip_footer=2))

	print(cfd_data)

	for i in range(0, 10):
		filename = str("a=" + str(int(cfd_data[0][i, 7])) + ".dat")
		new_data = []
		for j in range(0, len(cfd_data_list)):
			new_data.append(cfd_data[j][i, :])

		np.savetxt(filename, new_data)



def main():
	folder = r"D:\Program\aerodynamic_cruve\SMALL-TAIL-FLAP0-FIN"
	lon2lat(folder)


if __name__ == "__main__":
	main()



