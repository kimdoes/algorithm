import sys

T = int(sys.stdin.readline())

for _ in range(T):
    sys.stdin.readline()  # 빈 줄 무시 (문제 입력 형식상 존재)
    N = int(sys.stdin.readline())
    total = 0
    for _ in range(N):
        num = int(sys.stdin.readline())
        total = (total + num) % N   # 합 대신 나머지만 관리
    print("YES" if total % N == 0 else "NO")
