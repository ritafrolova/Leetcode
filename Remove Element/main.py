def Remove_Element(nums,val):
    counter=len(nums)
    while val in nums:
            nums.remove(val)
            nums.append('_')
            counter-=1
    print(nums)
    return counter
#print(Remove_Element([3,2,2,3],3))
print(Remove_Element([0,1,2,2,3,0,4,2],2))
