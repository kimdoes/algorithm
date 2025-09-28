import sys

result = 0

for _ in range(7):
    num = int(sys.stdin.readline())

    if (num % 2 == 1):

        if result != 0:
            if num < mini:
                mini = num
        else:
            mini = num

            
        result += num
    else:
        continue

if result == 0:
    print(-1)
else:
    print(result)
    print(mini)