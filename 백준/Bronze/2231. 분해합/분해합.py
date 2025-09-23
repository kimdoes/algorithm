import sys

N = sys.stdin.readline().rstrip()
count = 0

def saeng(N):
    N = str(N)
    result = 0

    for i in N:
        result += int(i)
    
    return result + int(N)

for i in range(int(N)):
    num = saeng(i)

    if num == int(N):
        result = i
        count += 1
        break

if count != 0:
    print(result)
else:
    print(0)