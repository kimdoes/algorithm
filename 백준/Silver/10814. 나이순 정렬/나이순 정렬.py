import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
memberList = []

for _ in range(N):
    dictionary = {}
    age, name = sys.stdin.readline().split()
    dictionary[name] = int(age)
    memberList.append(dictionary)


def comp(a,b):
    ageA = list(a.items())[0][1]
    ageB = list(b.items())[0][1]

    if ageA > ageB:
        return 1
    elif ageA < ageB:
        return -1
    else:
        nameA = list(a.items())[0][0]
        nameB = list(a.items())[0][0]

        if nameA > nameB:
            return 1
        elif nameA < nameB:
            return -1
        else:
            return 0


memberList = sorted(memberList, key=cmp_to_key(comp))

for i in memberList:
    print(list(i.items())[0][1], list(i.items())[0][0])