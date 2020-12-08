a = ['FLAP0-L', 'FLAP10-L', 'FLAP20-L','FLAP0-L-A', 'FLAP10-L-A', 'FLAP20-L-A']
afilter = filter(lambda i: "-A" not in i, a)
# aa = list(afilter)
for i in list(afilter):
    print(i)

for ee in list(afilter):
    print(ee)
