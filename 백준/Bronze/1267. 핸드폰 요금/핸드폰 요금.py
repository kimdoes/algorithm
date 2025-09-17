def yeong(times):
    if times < 30:
        return 10
    else:
        return (times//30 + 1) * 10

def minsik(times):
    if times < 60:
        return 15
    else:
        return (times//60 + 1) * 15
        
N = int(input())
timelist = list(map(int,input().split()))
minresult = 0
yeongresult = 0

for i in timelist:
    minresult += minsik(i)
    yeongresult += yeong(i)

if minresult > yeongresult:
    print("Y", yeongresult)
elif minresult < yeongresult:
    print("M", minresult)
else:
    print("Y M", yeongresult)