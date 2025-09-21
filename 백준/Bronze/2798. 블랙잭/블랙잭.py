import sys

N, M = map(int,sys.stdin.readline().split())
numli = list(map(int,sys.stdin.readline().split()))
result = 0
mediresult = 0
ocha = 0

for i in range(len(numli)-2):
    for j in range(i+1, len(numli)-1):
        for k in range(j+1, len(numli)):
            mediresult = numli[i] + numli[j] + numli[k]
            if mediresult <= M:
                result = max(result,mediresult)

print(result)