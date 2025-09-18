import sys

N = int(sys.stdin.readline())

for i in range(N):
    for j in range(N-i-1, 0, -1):
        print(" ",end="")
    for k in range(1, 2*i + 2):
        print("*",end="")
    print()

for i in range(1, N):
    for j in range(i):
        print(" ",end="")
    for k in range(2*N - 3, 2*i-2, -1):
        print("*",end="")
    print()