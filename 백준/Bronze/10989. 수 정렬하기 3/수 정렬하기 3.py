import sys

N = int(sys.stdin.readline())
countList = [0] * (10001)

for _ in range(N):
    num = int(sys.stdin.readline())
    countList[num] += 1

for i in range(len(countList)):
    if countList[i] == 0:
        continue
    for k in range(countList[i]):
        print(i)