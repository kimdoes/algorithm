import sys

result = 0
score = 0
N = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

for i in range(len(li)):
    if li[i] == 1:
        if i == 0 or li[i-1] == 0:
            result += 1
            score += 1
        elif li[i-1] == 1:
            result += score+1
            score += 1
    else:
        score = 0

print(result)