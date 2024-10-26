from math import sqrt
def nt(n):
    for i in range(2,int(sqrt(n))+1):
        if n %i == 0:
            return False
    return n >1
for _ in range(int(input())):
    m = input()
    t = 0
    for i in m:
        t += int(i)
    if nt(t):
            print("YES")
    else:
            print("NO")
