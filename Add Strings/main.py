def addStrings(num1,num2):
    sum=0
    s=''
    z=0
    for i in num1:
        z=str(int(i))
        sum=z+s
    return sum
print(addStrings('11','123'))