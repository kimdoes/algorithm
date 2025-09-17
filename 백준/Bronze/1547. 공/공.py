N = int(input())
ballnum = 1

for i in range(N):
    m, n = map(int,input().split())

    if m == ballnum:
        ballnum = n
    elif n == ballnum:
        ballnum = m

print(ballnum)