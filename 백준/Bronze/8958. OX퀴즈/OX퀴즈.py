import sys

def main():
    score = 0
    result = 0
    res = list(sys.stdin.readline())

    for i in range(len(res)):
        if res[i] == 'O':
            result += 1 + score
            score += 1
        else:
            score = 0
    
    print(result)

N = int(sys.stdin.readline())

for _ in range(N):
    main()