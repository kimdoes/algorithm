import sys

N = int(sys.stdin.readline())
result = 1

for _ in range(N):
    num = int(sys.stdin.readline())
    result += num - 1

print(result)