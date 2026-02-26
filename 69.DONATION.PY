T = int(input())
for i in range(T):
    X = int(input())
    
    if X <= 3:
        print("BRONZE")
    elif X <= 6:
        print("SILVER")
    else:
        print("GOLD")
