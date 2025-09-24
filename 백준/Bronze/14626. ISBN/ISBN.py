import sys

li = list(sys.stdin.readline().rstrip())
result = 0

for i in range(len(li)):
    num = li[i]

    if num == "*":
        isin2 = (True) if i % 2 == 1 else (False)
        continue
    else:
        result += (int(num)) if i % 2 == 0 else (int(num)*3)


if isin2:
    for i in range(0,10):
        medi = 3 * i

        if (result + medi) % 10 == 0:
            print(i)
            break
else:    
    if int(str(result)[-1]) != 0:
        print(10-(int(str(result)[-1])))
    else:
        print(0)