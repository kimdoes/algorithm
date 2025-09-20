import sys

String = list(sys.stdin.readline())
result = ''

for i in range(97,123):
    if chr(i) not in String:
        result += '-1 '
    else:
        result += str(String.index(chr(i)))+" "
    
    
print(result)