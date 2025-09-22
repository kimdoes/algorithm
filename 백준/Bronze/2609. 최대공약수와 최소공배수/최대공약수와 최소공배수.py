import sys

def yak(N,M):
    for i in range(min([N,M]),0,-1):
        if N % i == 0 and M % i == 0:
            return i

def bae(N,M):
    for i in range(max([N,M]),M*N+1):
        if i % N == 0 and i % M == 0:
            return i
        
N, M = map(int,sys.stdin.readline().split())
print(yak(N,M))
print(bae(N,M))