
def myPow(x: float, n: int) -> float:

    print((n//2) * (n//2) * (n%2))
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == -1:
        return 1/x
    return myPow(x, n//2) * myPow(x, n//2) * myPow(x, n%2)

x = 2
n = 24

answer = myPow(x,n)
print(answer)
