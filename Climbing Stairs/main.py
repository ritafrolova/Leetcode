def climbStairs(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)    #l=[1,2,3]
    sum=l[0]
    for n in l:
        sum+=n
        if sum>n+1:
            sum=0
            continue
        print(sum)
print(climbStairs(3))