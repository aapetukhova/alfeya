abc="abcdefghijklmnopqrstuvwxyz"
a=list(abc)
f=input()
l=list(f)
n=len(l)
m=len(a)
for i in range (0, n-1):
    for j in range (0, m-1):
        while l[i]!=a[j]:
            j+=1
        if j == m:
            j=-1
        l[i]=a[j+1]
##l2=" ".join(l)
##print(l2)
