def get10(num):
    if num % 4 == 0:
        return num // 4
    else:
        return (num // 4) + 1

def getheng(num):
    return num % 4 if num % 4 != 0 else 4

n, m = map(int,input().split())

yeoln = get10(n)
hengn = getheng(n)

yeolm = get10(m)
hengm = getheng(m)

print(abs(yeoln - yeolm) + abs(hengn - hengm))