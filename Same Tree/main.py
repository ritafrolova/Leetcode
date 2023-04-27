def func(p,q):
    p=list(p)
    q=list(p)
    p.sort()
    q.sort()
    if p==q:
        return True
    return False
print(func([1,2,3],[1,2,3]))
#не получилось, тип tree node нельзя сравнить как список
