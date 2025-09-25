import sys

def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N * factorial(N-1)

N = int(sys.stdin.readline().rstrip())
num = str(factorial(N))[::-1]

for i in range(len(num)):
    if num[i] != "0":
        print(int(i))
        exit()

print(0)