import sys

num = int(sys.stdin.readline())
k = int(sys.stdin.readline())

num = num - (num % 100)

for i in range(100):

    if num % k == 0:
        print(str(num)[-2:])
        exit()

    num += 1

print("no")