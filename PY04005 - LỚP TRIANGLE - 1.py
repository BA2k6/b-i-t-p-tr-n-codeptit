from math import sqrt

def kt(c1,c2,c3):
    if c1 +c2 <= c3 or c1+c3 <= c2 or c3 +c1 <= c2:
        return False
    return True
for _ in range(int(input())):
    a,b,c,d,m,n=map(float,input().split())
    c1 = sqrt((a-c)**2+(b-d)**2)
    c2 = sqrt((a-m)**2 + (b-n)**2)
    c3 = sqrt((c-m)**2 + (d-n)**2)
    if kt(c1, c2, c3):
        t = c1 + c2 + c3
        print(f"{t:.3f}")
    else:
        print("INVALID")




