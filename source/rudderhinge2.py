import os
import numpy as np


path =r"D:\Program\aerodynamic_cruve\wind_tunnel\hinge-moment\rudder-L"
os.chdir(path+"\\"+"R0")
data0 = np.genfromtxt("A=0.0.dat", skip_footer=2, skip_header=0)
print(data0)
os.chdir(path)
rudder_list = os.listdir(path)
for ir in rudder_list:
    path1 = path+"\\"+ir
    os.chdir(path1)
    data = np.genfromtxt("A=-4.0.dat", skip_footer=0, skip_header=0)
    print(data)
    temp0=[]
    for i in data:
        temp = i - data0
        temp0.append(temp)
    np.savetxt("RA=-4.0.dat", temp0, fmt='%.5f')

