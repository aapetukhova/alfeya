abc="abcdefghijklmnopqrstuvwxyz"
bcd="bcdefghijklmnopqrstuvwxyza"
a=list(abc)
m=len(a)
b=list(bcd)
p=len(b)
f=input()
l=list(f)
n=len(l)
for i in range (0, n):
    for j in range (0, m):
        if l[i]==a[j]:
            l[i]=b[j]
            break
l2="".join(l)
print(l2)
