t = int(input())

for _ in range(t):
    NA, NB, NC = map(int, input().split())
    
    if NA > NB + NC or NB > NA + NC or NC > NA + NB:
        print("YES")
    else:
        print("NO")