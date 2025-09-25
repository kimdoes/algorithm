import sys

li = []
result = []
N = int(sys.stdin.readline())

for _ in range(N):
    weight, height = map(int,sys.stdin.readline().split())
    li.append((weight, height))
    

for i in range(N):  #나
    count = 0
    for j in range(N):  #상대방
        if i == j:
            continue
        else:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                count += 1
            else:
                count += 0

    result.append(count+1)

for k in result:
    print(k, end=" ")