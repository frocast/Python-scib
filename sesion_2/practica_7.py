f = open("num.txt", "w")
for i in range(1,501):
    f.write("%d, " % (i))
f.close()