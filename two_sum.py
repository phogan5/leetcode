class Solution:
    def twoSum(nums:list, target: int):
        
        hashset = {}
        for i in range(len(nums)):
            if target - nums[i] in hashset.keys():
                print(i)
                return [i,hashset[target-nums[i]]]

            else:
                hashset[nums[i]]=i
            

    
    result = twoSum(nums=[3,2, 3], target=6)
    print(result)
