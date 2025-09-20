import sys

num = int(sys.stdin.readline())


def main(H, W, N):
    backnum = str((N // H + 1) if N % H != 0 else (N // H))
    floornum = str((N % H) if N % H != 0 else H)

    backnum = backnum if len(backnum) != 1 else '0'+backnum
    room = floornum + backnum
    print(int(room))

for _ in range(num):
    H, W, N = map(int,sys.stdin.readline().split())
    main(H,W,N)