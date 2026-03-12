T = int(input())

for _ in range(T):
    N = input().strip()
    print(sum(int(d) for d in N))