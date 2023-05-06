def kthFactor(n,k):
    factors_list=[]
    for i in range(1,n+1):
        if n%i==0:
            factors_list.append(i)
    print(factors_list)      
    if k>len(factors_list):
        return -1
    return factors_list[k-1]
    
    
print(kthFactor(12,3)) 
print(kthFactor(7,2))
print(kthFactor(4,4))
print(kthFactor(1,1))
