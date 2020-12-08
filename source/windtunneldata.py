#
#
# 风洞试验数据类，并给出静安定度。
import numpy as np


class WTData():
    def __init__(self, filename):
        self.filename = filename
        self.winddata = np.array([])

    def slope(self, x, y):
        # 实现简单线性回归函数，计算斜率。与EXCEL中slope函数功能一样。
        xmean = self.mean(x)
        ymean = self.mean(y)
        sum1 = 0.0
        sum2 = 0.0

        for ix, iy in zip(x, y):
            sum1 = sum1 + (ix - xmean)*(iy - ymean)
            sum2 = sum2 + (ix - xmean)*(ix - xmean)

        return sum1/sum2

    def mean(self, x):
        # 计算数组的平均值
        sum = 0.0
        for i in x:
            sum = sum + i
        return sum/len(x)

    def static_stability(self, n):
        # 计算风洞试验数据的静安定度。
        # n 表示计算静安定度时，选取的点的数量。
        row, col = self.winddata.shape
        static_stab = []

        for i in range(row - n + 1):
            x = []
            y = []
            for j in range(n):
                # 0 列对应升力系数；2 列对应力矩系数
                x.append(self.winddata[i+j, 0])
                y.append(self.winddata[i+j, 2])

            static_stab.append(self.slope(x, y))

        return static_stab

    def input(self):
        # 读入风洞试验数据，默认去掉第一行和最后一行。
        self.winddata = np.genfromtxt(self.filename, skip_header=1, skip_footer=1)


if __name__ == "__main__":
    print("测试数据")


