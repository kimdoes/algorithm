import sys

N = int(sys.stdin.readline())
li = []

for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    li.append(num)

li.sort()

for i in li:
    print(i)