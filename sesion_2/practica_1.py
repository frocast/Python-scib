A = [1,5,8,0,1,2,4,3]
B = []

for i in range(len(A)):
    B.append(min(A))
    A.remove(min(A))
print B