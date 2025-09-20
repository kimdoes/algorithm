import sys

li = list(map(int,sys.stdin.readline().split()))
lili = sorted(li)
reli = sorted(li,reverse=True)

if li == lili:
    print("ascending")
elif li == reli:
    print("descending")
else:
    print("mixed")