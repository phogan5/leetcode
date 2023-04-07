'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''
def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, n in enumerate(nums): #value:index
        diff = target - n
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[n] = i

            




response = twoSum(nums=[3,2,3], target=6)

print(response)