A, B, X, Y = map(int, input().split())
messi_points = 2 * A + B
ronaldo_points = 2 * X + Y
if messi_points > ronaldo_points:
    print("Messi")
elif ronaldo_points > messi_points:
    print("Ronaldo")
else:
    print("Equal")
