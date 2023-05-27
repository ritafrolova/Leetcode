def plusOne(digits):
    string=''
    l=[]
    number=0
    for i in digits:
        string=string+str(i)
    number=int(string)+1
    for j in str(number):
        l.append(int(j))
    return l
print(plusOne([1,2,3]))

