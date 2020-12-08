aa = ['A=-4', 'A=0', 'A=10', 'A=12', 'A=14', 'A=15', 'A=16', 'A=2', 'A=4', 'A=6', 'A=8', 'AILERON0-L', 'AILERON10-L', 'AILERON20-L', 'ea.legend', 'zs.legend']
cc = []
for i in aa:

    if "legend" not in i and "=" not in i:

        cc.append(i)

print(cc)
