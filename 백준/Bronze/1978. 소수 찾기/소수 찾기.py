import sys

N = int(sys.stdin.readline())
numlist = list(map(int,sys.stdin.readline().split()))
result = 0

def isPrime(a):
    if a == 1:
        return False
    
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

for i in numlist:
    if isPrime(i) == True:
        result += 1

print(result)