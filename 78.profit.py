T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    new_profit = Y + (X // 10)
    print(new_profit)
