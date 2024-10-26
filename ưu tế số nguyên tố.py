from math import sqrt
def nt(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i ==0:
            return False
    return n > 1
for _ in range (int(input())):
    x = input()
    d=0
    for i in x:
        if nt(int(i)):
            d +=1
    if nt(len(x)) and d > len(x)-d:
            print("YES")
    else:
            print("NO")


