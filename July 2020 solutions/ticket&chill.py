t=int(input())

for _ in range(t):

  n,k=list(map(int,input().split()))

  a=list(map(int,input().split()))

  for i in range(1,n):

    if(a[i-1]<a[i]):

      continue

    else:

      count=1

      while((a[i-1]>a[i]) & (count<=k)):

        a[i]+=1

        a[i-1]-=1

        count+=1

  print(max(a))
