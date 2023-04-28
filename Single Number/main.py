def singleNumber(nums):
        my_dict={}
        for elem in nums:
            if elem not in my_dict:
                  my_dict[elem]=1
            else:
                  my_dict[elem]+=1
        for val in my_dict.values():
            if val ==1:
                  for k,v in my_dict.items():
                        if v==val:
                         return k                  
                  
print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))