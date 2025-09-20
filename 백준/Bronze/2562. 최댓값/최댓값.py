import sys

li = []
for _ in range(9):
    num = int(sys.stdin.readline())
    li.append(num)

print(max(li))
print(li.index(max(li))+1)