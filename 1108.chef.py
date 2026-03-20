t = int(input())

for _ in range(t):
    C, X, Y = map(int, input().split())
    
    chocolates_to_buy = C - X
    money = chocolates_to_buy * Y
    
    print(money)