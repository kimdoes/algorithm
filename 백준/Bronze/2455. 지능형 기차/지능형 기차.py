import sys

now = 0
result = 0

for i in range(4):
    n, m = map(int,sys.stdin.readline().split())
    now -= n
    now += m

    if now > result:
        result = now

print(result)