def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) -1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if nums[left] != target:
        return -1
    return left

response = search(nums=[-1,0,3,5,9,12], target = 9)
print(response)