import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

strint = list(str(A*B*C))

for i in range(10):
    print(strint.count(str(i)))