t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    
    total_seats = 10 * x
    passengers = min(total_seats, y)
    
    print(passengers * z)