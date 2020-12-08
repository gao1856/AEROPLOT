# 计算铰链力矩
# 拟合迎角-4°~8°
import numpy as np
import os


class HingeMoment():
    def __init__(self, path):
        self.path = path

    def getdata(self):
        os.chdir(self.path)
        file_list = os.listdir(self.path)
        # print(file_list)
        i = 0
        b = []
        for ifile in file_list:
            # 去掉数组后5行，尽量拟合线性段。
            data = np.genfromtxt(ifile, skip_header=1, skip_footer=6)
            number = list(filter(str.isdigit, ifile))
            num = "".join(number)
            # print(type(num))
            if "N" in ifile:
                num = -int(num)
            for ii in range(0, data.shape[0]):
                b.append(int(num))
            if i == 0:
                AA = data
            else:
                AA = np.concatenate([AA, data])
            i = i + 1
        return AA, b

    def lstsq(self, flag):
        AA, delta = self.getdata()
        temp = AA.shape[0]
        if flag == "sym":
            A = np.zeros((temp, 2))
            b = np.zeros(temp)
            A[:, 0] = AA[:, 7]
            A[:, 1] = delta
            b[:] = AA[:, 2]
            return np.linalg.lstsq(A, b)[0]
        else:
            A = np.zeros((temp, 3))
            b = np.zeros(temp)
            A[:, 0] = 1
            A[:, 1] = AA[:, 7]
            A[:, 2] = delta
            b[:] = AA[:, 2]
            return np.linalg.lstsq(A, b)[0]


path = r"D:\Program\aerodynamic_cruve\wind_tunnel\hinge-moment\aileron"
rx4e = HingeMoment(path)
temp = rx4e.lstsq("nosym")
print(temp)
