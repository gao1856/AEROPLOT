# 对风洞试验数据进行处理，将准纵向数据转换为横航向数据。
# 将原先固定侧滑角变迎角数据改为固定迎角变侧滑角。

import numpy as np
import os
import shutil
import plotfun



# 修改文件内容，legend文件，将迎角或者舵面偏角改为相对应值。
def alter(file, old_str, new_str):
     
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)

    return



def lon2lat(path):
    os.chdir(path)
    file_list = os.listdir(path)
    temp_list = []

    for ifile in file_list:
        if ifile.split(".")[0].isdigit():
            temp_list.append(ifile)
    file_list = temp_list
    # print(file_list)
    wind_data = []
    for ifile in file_list:
        temp = np.genfromtxt(ifile, skip_header=1, skip_footer=1)
        wind_data.append(temp)

    x = 0
    for i in wind_data[0][:, 7]:
        print(len(wind_data[0][0,:]))
        test = np.zeros(len(wind_data[0][0,:]))
        temp = []
        for idata in wind_data:
            temp.append(idata[x, :])

        #开头插入一行，末尾插入一行
        temp = np.insert(temp, [0], values = test, axis=0)
        temp = np.vstack([temp, test])
        np.savetxt("%s_A=%s.DAT" % (os.path.basename(path), int(i)), temp, fmt='%.5f')
        x = x + 1

    return


def mkdir(path):
    os.chdir(path)

    folder_list = os.listdir()
    folder_list = filter(lambda ifolde:
                         "A=" not in ifolde and
                         "-A" not in ifolde and
                         "a=" not in ifolde and
                         "legend" not in ifolde,
                         folder_list)

    for ifolder in list(folder_list):

        os.chdir(path + "\\" + ifolder)

        lon2lat(path + "\\" + ifolder)

        file_list0 = os.listdir()
        print(file_list0)
        file_list = filter(lambda ifile: not ifile.split(".")[0].isdigit(), file_list0)

        file_list = list(file_list)
        # 所有文件按照迎角放到一个文件夹中。
        for ifile in file_list:
            temp = ifile.split(".")[0]
            temp1 = temp.split("_")[-1]
            sfile = ifile
            # sfile = path + "\\" + ifile
            mfile = path + "\\" + temp1
            mfile1 = path + "\\" + temp1

            if not os.path.exists(mfile):
                os.mkdir(mfile)

            if os.path.exists(mfile):
                # os.chdir(mfile)
                path1 = os.getcwd()
                shutil.copy(sfile, mfile)
                os.chdir(path)
                shutil.copy("zs.legend", mfile)
                os.chdir(mfile)
                alter("zs.legend", "alpha=0", "alpha=%d" % int(temp1.split("=")[-1]))
                os.chdir(path1)


        # 生成文件夹，并把所有迎角文件放置到同一文件夹内。
        path2 = path + "\\" + ifolder + "-A"
        if not os.path.exists(path2):
            os.mkdir(path2)

        if os.path.exists(path2):
            for ifile in file_list:

                shutil.copy(ifile, path2)

            os.chdir(path)
            shutil.copy("zs1.legend", path2)
            os.chdir(path2)
            os.rename("zs1.legend", "zs.legend")

            temp2 = filter(lambda ss: ss.isdigit(), ifolder)
            temp3 =list(temp2)
            alter("zs.legend", "x=0", "x=%d" % int("".join(temp3)))


    return

path = r"D:\Program\aerodynamic_cruve\new\lateral-directional\AILERON-L"
mkdir(path)
folder_list = os.listdir(path)
folder_list = filter(lambda ifolder: "A=" in ifolder or "-A" in ifolder, folder_list)
# print(list(folder_list))
# breakpoint()
for ifolder in list(folder_list):
    print(ifolder)
    os.chdir(path + "\\" + ifolder)
    plotfun.wt_plot("lat")

