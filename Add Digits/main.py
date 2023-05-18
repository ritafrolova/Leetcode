def addDigits(num):
    while len(str(num))>9:
        if num<10:
            return num
        sum=0
        while num:
            sum+=num%10
            num=num//10
        return sum
    
print(addDigits(38))    

