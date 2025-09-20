import sys

hour, min = map(int, sys.stdin.readline().split())

if (min - 45) < 0:
    if hour == 0:
        hour = 23
    else:
        hour -= 1

min =  (15 + min) if (min - 45 < 0 ) else min - 45

print(hour,min)