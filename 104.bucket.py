t = int(input())

for _ in range(t):
    w, x, y, z = map(int, input().split())
    
    total = w + y * z
    
    if total > x:
        print("overflow")
    elif total == x:
        print("filled")
    else:
        print("unfilled")