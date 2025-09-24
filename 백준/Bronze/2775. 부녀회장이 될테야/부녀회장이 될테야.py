import sys

def main():
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    top = []
    floor = []
    result = []

    for i in range(1, n+1):
        floor.append(i)
    
    result.append(floor)

    for i in range(k):
        for j in range(n):
            top.append(listSummation(floor[0:j+1]))
        
        result.append(top)
        floor = result[-1]
        top = []

    print(result[k][-1])

def listSummation(li):
    result = 0
    for i in li:
        result += i
    
    return result

N = int(sys.stdin.readline())

for _ in range(N):
    main()

