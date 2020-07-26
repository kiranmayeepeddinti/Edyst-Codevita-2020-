n=int(input())
totaltime=int(input())
allsteps=[]
for i in range(n):
    a=list(map(int,input().strip().split()))
    allsteps.append(a)
    
leadd=[0]*n
added=[[0 for i in range(totaltime)] for i in range(n)]

for i in range(totaltime):
    if i%2==1:
            lis=[]
    for j in range(len(allsteps)):
        time = allsteps[j][-1]
        stps=allsteps[j][i]
        added[j][i] += stps*time + added[j][i-1]
        if i%2==1:
            lis.append(added[j][i])
    if i%2==1:
 
        winner=lis.index(max(lis))
        leadd[winner]+=1
        
print(leadd.index(max(leadd))+1)   
