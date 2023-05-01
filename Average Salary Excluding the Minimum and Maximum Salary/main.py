def average(salary):
    salary.remove(min(salary))
    salary.remove(max(salary))
    res=0
    for sal in salary:
        res+=sal
    return res/len(salary)
print(average([4000,3000,1000,2000]))