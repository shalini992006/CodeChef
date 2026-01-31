t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y >= 3 * x:
        print("YES")
    else:
        print("NO")
