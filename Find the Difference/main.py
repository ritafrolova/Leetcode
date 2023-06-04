def findTheDifference(s,t):
    l1,l2=[],[]
    for i in s:
        l1.append(i)
    for j in t:
        l2.append(j)
    print(l1,l2)
    for n in l2:
        if n in l2:
            l2.remove(n)
            l1.remove(n)
    return l1,l2
print(findTheDifference("abcd","abcde"))
#print(findTheDifference("","y"))