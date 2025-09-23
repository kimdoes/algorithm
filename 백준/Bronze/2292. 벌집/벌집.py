import sys

num = int(sys.stdin.readline())
i = 1
count = 1
while True:
    i = i + 6 * count

    if num <= i:
        if num == 1:
            print(1)
        else:
            print(count+1)
        break

    else:
        count += 1
        continue