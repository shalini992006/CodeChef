T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print(max(0, Y - X))
