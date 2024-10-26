from math import gcd
a,b,x,y=map(int, input().split())
t = a*y+x*b
m=b*y
k = gcd(t,m)
print(f"{t//k}/{m//k}")