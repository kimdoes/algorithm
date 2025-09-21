import sys

N = int(sys.stdin.readline())
sizelist = list(map(int, sys.stdin.readline().split()))
T, P = map(int,sys.stdin.readline().split())
result = 0

for i in sizelist:
    result += (i//T) if (i % T == 0) else ((i//T) + 1)

penMTE = N // P
pennotMTE = N % P

print(result)
print(penMTE, pennotMTE)