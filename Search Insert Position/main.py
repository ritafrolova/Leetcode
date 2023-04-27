def func(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums=sorted(nums)
        return nums.index(target)
print(func([1,3,5,6],5)) 
print(func([1,3,5,6],2))
print(func([1,3,5,6],7))