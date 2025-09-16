li = []

for i in range(3):
    num = int(input())
    result = 0

    for j in range(num):
        number = int(input())
        result += number

    if (result > 0):
        li.append("+")
    elif (result < 0):
        li.append("-")
    else:
        li.append(0)

for k in li:
    print(k)