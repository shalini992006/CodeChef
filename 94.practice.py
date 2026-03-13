weeks = list(map(int, input().split()))

count = 0

for problems in weeks:
    if problems >= 10:
        count += 1

print(count)