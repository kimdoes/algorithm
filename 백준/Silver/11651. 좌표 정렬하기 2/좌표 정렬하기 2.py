import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
locali = []

def comp(a,b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1
    else:
        if a[0] > b[0]:
            return 1
        elif a[0] < b[0]:
            return -1
        else:
            return 0

for _ in range(N):
    x, y = map(int,sys.stdin.readline().split())
    locali.append((x,y))

locali = sorted(locali, key=cmp_to_key(comp))

for i in locali:
    print(i[0], i[1])