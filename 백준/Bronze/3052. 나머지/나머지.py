import sys

setting = set()
for _ in range(10):
    setting.add(int(sys.stdin.readline()) % 42)

print(len(setting))