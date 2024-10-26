from math import *
a,b= map(int,input().split())
x= gcd(a,b)
tu = a//x
mau = b//x
print(f"{tu}/{mau}")