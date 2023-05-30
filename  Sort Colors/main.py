def sortColors(nums):
    new_nums=nums.copy()
    nums.clear()
    while len(new_nums)!=0:
        nums.append(min(new_nums))
        new_nums.remove(min(new_nums))
    return nums
print(sortColors([2,0,2,1,1,0]))