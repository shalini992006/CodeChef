import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num % k == 0:
        count += 1

print(count)   