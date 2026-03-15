t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    
    if z < y:
        print(0)
    else:
        print((z - y) // x)