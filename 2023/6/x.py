from math import sqrt,ceil,floor

time = 30
target = 200

a,b,c = -1, time, -target

disc = b*b - 4*a*c

x = (-b + sqrt(disc)) / 2 / a

xb = ceil(x)
if x == xb:
    xb = xb+1

ans = 1+time - xb*2
print(ans)
