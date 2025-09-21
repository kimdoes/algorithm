import sys

def main():
    number = sys.stdin.readline()

    if int(number) == 0:
        exit()

    renumber = number[::-1]

    if int(number) == int(renumber):
        print("yes")
    else:
        print("no")

while True:
    main()