t=int(iinput())
for_in range(t):
x, y=map(int,input().split())
if(x > y):
print("LOSS")
if(x == y):
print("NEUTRAL")
if(x < y):
print("PROFIT")