import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
setting = set()

def comp(a, b):
    if len(a) < len(b):
        return -11
    elif len(a) > len(b):
        return 1
    else:
        for i in range(len(a)):
            if a[i] > b[i]:
                return 1
            elif a[i] < b[i]:
                return -1
            else:
                continue
        return 0

for _ in range(N):
    String = sys.stdin.readline().rstrip()
    setting.add(String)

set2 = sorted(setting,key=cmp_to_key(comp))
set2 = list(set2)

for i in set2:
    print(i)