import sys

A, B = map(int, sys.stdin.readline().split())
C, D = map(int, sys.stdin.readline().split())

result1 = (A / C) + (B / D)
result2 = (C / D) + (A / B)
result3 = (D / B) + (C / A)
result4 = (B / A) + (D / C)
li = [result1, result2, result3, result4]

print(li.index(max(li)))