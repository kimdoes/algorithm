import sys
import math

D, H, W = map(int,sys.stdin.readline().split())

real = math.sqrt(D**2 / (W**2 + H**2))
print(int(real * H), int(real * W))