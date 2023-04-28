def func(x):
    if x<0:
        x*=-1
        
    x=str(x)
    if x[-1]==0:
        x=x.replace('0','')
    if int(x)<0:
        x(str).insert(-1,'-')
    
    return x[::-1]
print(func(123)) #321
print(func(-123)) #-321
print(func(120)) #21