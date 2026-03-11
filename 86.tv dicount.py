t = int(input())
for i in range(t):
    A, B, C, D = map(int, input().split())
    
    price1 = A - C
    price2 = B - D
    
    if price1 < price2:
        print("First")
    elif price1 > price2:
        print("Second")
    else:
        print("Any")
