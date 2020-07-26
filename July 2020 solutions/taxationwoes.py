slabs=list(map(int,input().strip().split()))
taxrates=list(map(int,input().strip().split()))
rebate=int(input())
taxespaid=list(map(int,input().strip().split()))
num_employees=len(taxespaid)
salaries=[0]*num_employees
for i in range(num_employees):
    curr_emppaid=taxespaid[i]
    #print(curr_emp)
    salaries[i]+=slabs[0]
    for j in range(1,len(slabs)):
        max_curr_slab=taxrates[j-1]*(slabs[j]-slabs[j-1])/100
        if max_curr_slab<=curr_emppaid:
            salaries[i]+=(slabs[j]-slabs[j-1])
            curr_emppaid-=max_curr_slab
        else:
            paid_in_slab=(curr_emppaid*100)/taxrates[j-1]
            salaries[i]+= paid_in_slab
            curr_emppaid-= curr_emppaid
    if curr_emppaid>0:
        salaries[i]+= ((curr_emppaid*100)/taxrates[-1])
    salaries[i]+=rebate
    
print(int(sum(salaries)))
