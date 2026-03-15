t = int(input())

for _ in range(t):
    w, x, y, z = map(int, input().split())
    
    final_balance = w + (x - y) * z
    
    print(final_balance)