rr1=float(input())
B1,B2=list(map(int,input().split()))
a=list(input().split())
rr2=float(input())
s=0
b=len(a)
for i in range(b):
    if a[i]!='W':
        s=s+int(a[i])
totalb=round((rr2*b-6*s)/(rr1-rr2))
totalr=round(totalb*rr1/6)

for i in range(b):
    if a[i]!='W':
        B1=B1+int(a[i])
        #print(B1)
        if int(a[i])%2==1:
            temp=B1
            B1=B2
            B2=temp
    else:
        B1=0
    totalb+=1
    if totalb%6==0: 
        temp=B1
        B1=B2
        B2=temp
print(totalr+s,B1,B2)
