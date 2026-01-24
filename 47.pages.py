t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    if x * y >= n:
        print("YES")
    else:
        print("NO")
