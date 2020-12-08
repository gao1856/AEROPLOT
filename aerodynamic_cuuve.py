# 对文件夹下的风洞试验数据进行绘图。
# 文件夹构成：
# wind_tunnel---longitudinal---

#            ---lateral-directional
#
# 风洞试验数据：纵向数据（升降舵效率、襟翼、基本状态、升降舵带襟翼、襟翼对比、机翼对比等等）
#            横航向数据（副翼效率、方向舵效率、有无腹鳍、大小垂尾对比等等）
# 主要函数：
# lon2latdir:风洞试验纵向数据转换为横航向数据,并安迎角生成文件夹。
# drawcurve:绘制曲线函数


"""
lon2latdir()
drawcurve()

"""

from loncruve import *
from latcruve import *
from lon2lat import *
from alphadir import *
import os


folder = r"D:\Program\aerodynamic_cruve\wind_tunnel"

# 纵向数据绘图
# 纵向数据文件夹
londir = folder + "\longitudinal"
os.chdir(londir)
londirlist = os.listdir(londir)
for idir in londirlist:
    idirlon = londir + "\\" + idir
    os.chdir(idirlon)
    # 绘制曲线
    # "EA" 表示欧美坐标系，欧美图标；"ZS" 表示中苏坐标系，中苏图标
    loncruve(idirlon, "EA")

# 横航向数据绘图
# 横航向数据文件夹
latdir = folder + "\lateral-directional"
os.chdir(londir)
latdirlist = os.listdir(latdir)
for idir in latdirlist:
    idirlat = latdir + "\\" + idir
    os.chdir(idirlat)
    # 纵向数据转换为横航向数据。
    # for ifile in os.listdir(idirlat):
    #     temp = idirlat+"\\"+ifile
    #     if os.path.isdir(temp):
    #         os.chdir(idirlat+"\\"+ifile)
    #         if "=" not in ifile:
    #             lon2lat(ifile)
    #
    #         os.chdir(idirlat)
    #         # 按照迎角生成文件夹
    #         alphadir(idir)



    # 绘制曲线
    # "EA" 表示欧美坐标系，欧美图标；"ZS" 表示中苏坐标系，中苏图标
    temp_dir_list = []
    for temp_i_dir in os.listdir(idirlat):
        if temp_i_dir.split("=")[-1].isdigit():
            temp_dir_list.append(temp_i_dir)

    for idir_temp in temp_dir_list:
        os.chdir(idirlat + "\\" + idir_temp)
        latcruve(idirlat, "EA")

