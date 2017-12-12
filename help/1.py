k=0
a_first=int(input())
amin=a_first
amax=a_first
s=a_first
while True:
    a=int(input())
    k+=1
    s=s+a
    if a<amin:
        amin=a
    if a>amax:
        amax=a
    if a==0:
        break
print(s/k)
print(amin)
print(amax)
