def func(nums1,m,nums2,n):
    nums=nums1+nums2
    while 0 in nums:
        nums.remove(0)
    return sorted(nums)
print(func([1,2,3,0,0,0],3,[2,5,6],3)) #[1,2,2,3,5,6]