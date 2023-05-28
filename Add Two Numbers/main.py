def addTwoNumbers(l1,l2): 
    string1,string2='',''
    for i in l1:
        string1=(string1+str(i))
        reversed_str1 = "".join(reversed(list(string1)))
    for j in l2:   
        string2=(string2+str(j))
        reversed_str2 = "".join(reversed(list(string2)))
    summ=int(reversed_str1)+int(reversed_str2)    #807
    result_list=[]
    for alpha in str(summ):
        result_list.append(alpha)
    return result_list[::-1]
    
print(addTwoNumbers([2,4,3],[5,6,4]))  #решение правильное, не прошло в Leetcode