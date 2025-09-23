import sys

N = int(sys.stdin.readline())
NList = list(sys.stdin.readline().rstrip())
result = 0

for i in range(len(NList)):
    result += (((ord(NList[i]) - 96) * (31 ** i)) % 1234567891)

print(result)