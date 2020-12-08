import os
import shutil


def alphadir(folder):
    # 生成文件夹
    folder_list1 = os.listdir(os.getcwd())
    print(folder_list1)
    temp_list = []
    for itemp in folder_list1:
        if "=" not in itemp and "legend" not in folder_list1:
            temp_list.append(itemp)

    folder_list1 =temp_list
    print(folder_list1)



    file_list = os.listdir(os.getcwd()+"\\"+folder_list1[0])
    for ifile in file_list:

        if ("N" not in ifile.split(".")[0][0]) and (not ifile.split(".")[0].isdigit()):

            temp = ifile.split(".")[0].split("_")[-1]
            try:
                os.mkdir(os.getcwd()+"\\"+temp)
            except:
                print("")

    # 文件移动到相应的文件夹
    folder_list2 = os.listdir(os.getcwd())
    temp_list = []
    for itemp in folder_list2:
        if "=" in itemp:
            temp_list.append(itemp)

    folder_list2 = temp_list

    for ifolder in folder_list1:
        temp = os.getcwd() + "\\" + ifolder
        # print(temp)
        # print("========")
        if os.path.isdir(temp):
            file_list = os.listdir(os.getcwd() + "\\" + ifolder)

            for ifile in file_list:

                temp1 = ifile.split(".")[0].split("_")[-1]
                # print(temp1)
                if temp1 in folder_list2:
                    # pass
                    print(os.getcwd() + "\\" +ifolder+ "\\" + ifile)
                    shutil.move(os.getcwd() + "\\" +ifolder+ "\\" + ifile, os.getcwd() + "\\" +temp1)
