T = int(input())
for _ in range(T):
    N, X, K = map(int, input().split())
    if K >= N * X:
        print("YES")
    else:
        print("NO")

