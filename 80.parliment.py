T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    if 2 * X >= N:
        print("YES")
    else:
        print("NO")
