t = int(input())

for _ in range(t):
    X = int(input())

    if X <= 70:
        print(0)
    elif X <= 100:
        print(500)
    else:
        print(2000)
