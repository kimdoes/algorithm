import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    num = (pow(a,b,10))

    print(num if num != 0 else 10)

N = int(sys.stdin.readline())

for i in range(N):
    main()