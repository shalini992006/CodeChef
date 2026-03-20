t = int(input())

for _ in range(t):
    N, X = map(int, input().split())
    
    total_songs = N // X
    result = total_songs // 3
    
    print(result)