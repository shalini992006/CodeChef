t = int(input())

for _ in range(t):
    n = int(input())
    
    last_digit = n % 10
    
    # Find first digit
    while n >= 10:
        n //= 10
    first_digit = n
    
    print(first_digit + last_digit)