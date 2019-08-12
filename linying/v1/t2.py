l_a = None
#print(len(l_a))

l_b = [1,2,3]
for i in range(len(l_b)):
    if(l_b[i]==3):
        del(l_b[i])
print(l_b)

l_c = [2,3,5,4,6,2,3]
for i in l_c:
    if(i==2):
        del(l_c[l_c.index(i)])
print(l_c)