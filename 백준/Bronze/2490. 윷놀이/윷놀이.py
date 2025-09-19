import sys

for _ in range(3):
    li = list(map(int,sys.stdin.readline().split()))

    k = li.count(0)
    if k == 0:
        print("E")
    elif k == 1:
        print("A")
    elif k == 2:
        print("B")
    elif k == 3:
        print("C")
    elif k == 4:
        print("D")