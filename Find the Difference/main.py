def findTheDifference(s,t):
    l1,l2=[],[]
    for i in s:
        l1.append(i)
    for j in t:
        l2.append(j)
    for a in l1:
        if a not in l2:
            return a
    for b in l2:
        if b not in l1:
            return b
print(findTheDifference("abcd","abcde"))
print(findTheDifference("","y"))