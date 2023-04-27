def func(list1,list2):
    result_list=list1+list2
    return sorted(result_list)
print(func([1,2,4],[1,3,4]))
print(func([],[]))
print(func([],[0]))