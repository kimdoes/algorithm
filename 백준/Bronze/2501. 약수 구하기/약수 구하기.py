import sys

N, K = map(int,sys.stdin.readline().split())
li = []

for i in range(1, N+1):
    if N % i == 0:
        li.append(i)

if (K) <= len(li):
    print(li[K-1])
else:
    print(0)