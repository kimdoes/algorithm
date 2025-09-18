import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(" "*i, end="")
    print("*"*((2*N)-(1+(2*i))))