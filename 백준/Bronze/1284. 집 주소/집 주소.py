while True:
    result = 2

    num = int(input())

    if num == 0:
        break

    numstr = str(num)
    length = len(numstr)

    for i in numstr:
        if i == "1":
            result += 2
            length -= 1
        if i == "0":
            result += 4
            length -= 1
    
    result += length * 3
    result += (len(numstr) - 1)
    print(result)