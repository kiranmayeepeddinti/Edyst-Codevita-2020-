n=int(input())
times=[]
for i in range(n):
    x,y,velocity=map(int,input().strip().split())
    distance=((x*x)+(y*y))**(0.5)
    time=distance/velocity
    times.append(time)
collisions=0   
for t in range(n):
    individual_collisions=times[t+1:].count(times[t])
    collisions += individual_collisions
print(collisions)
