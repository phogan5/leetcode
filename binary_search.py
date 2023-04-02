'''
704. Binary Search
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''

def search(nums: list[int], target: int, low, high) -> int:
    #Get the midpoint of the list
    if high >= low:
        mid = (high + low) // 2

        #Check if element is present at the middle itself
        if nums[mid] == target:
            return mid

        #If the target is less than the one at the mid, it must be in the first half of the list
        elif nums[mid] > target:
            #Do the search again, but with the max set as 1 less than the halfway point, effectively searching the first half of the list
            return search(nums, target, low, mid - 1)
    
        #If the target is greater than the one at the mid, it must be in the second hald of the list
        else:
            #Do the search again, but with the min set as 1 greater than the midpoint, effectively searching through the second half of the list.
            return search(nums, target, mid + 1, high)
    #If the target is not present in the list, return
    else:
        return -1




nums=[-1,0,3,5,9,12]
target = 12
response = search(nums, target, low = 0, high = len(nums)-1)
print(response)
