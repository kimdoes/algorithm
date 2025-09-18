import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    for j in range(i):
        print("*",end="")
    for k in range(1, N*2 - i*2 + 1):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()

for i in range(1, N+1):
    for j in range(N-i):
        print("*",end="")
    for k in range(2, 2*i + 2):
        print(" ",end="")
    for l in range(N-i):
        print("*",end="")
    print()