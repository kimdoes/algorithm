import sys

A, B, V = map(int, sys.stdin.readline().split())
day = 0
now = 0

Last = ((V-A) // (A-B)) * (A-B)
day = ((V-A) // (A-B))

if (V - Last) > A:
    print(day + 2)
else:
    print(day + 1)