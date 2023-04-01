#Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x: int) -> bool:
    rightlist = []
    leftlist = []
    x = str(x)
    left, right = 0, len(str((x))) - 1
    while left < right:
        rightlist.append(x[right])
        leftlist.append(x[left])
        left += 1
        right -= 1

    if rightlist == leftlist:
        return True
    else:
        return False


response = isPalindrome(-121)
print(response)

