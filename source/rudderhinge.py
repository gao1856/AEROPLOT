# 方向舵铰链力矩系数计算。
# 并对方向舵数据处理
import os
import numpy as np

path = r"D:\Program\aerodynamic_cruve\wind_tunnel\hinge-moment\rudder-L"

rudder_list = os.listdir(path)
for ilist in rudder_list:
    path1 = path+"\\"+ilist
    os.chdir(path1)
    file_list = os.listdir(path1)
    newtemp = []
    for ifile in file_list:
        print(ifile)
        temp1 = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
        newtemp.append(temp1)

    row = newtemp[0].shape[0]
    # print(row)
    for i in range(0, row):
        tt = []
        for ia in newtemp:

            # print(ia)
            if round(ia[i, 7]) == round(newtemp[0][i, 7]):
                tt.append(ia[i,:])

        np.savetxt("A=%s.dat" % round(newtemp[0][i, 7]), tt, fmt='%.5f')
