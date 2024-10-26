def doi(t):
    if 3 <= t and t <=4:
        return 2.5
    if 5 <= t and t <=6:
        return 3.0
    if 7 <= t and t <= 9:
        return 3.5
    if 10 <= t and t <= 12:
        return 4.0
    if 13 <= t and t <=15:
        return 4.5
    if 16 <= t and t <=19:
        return 5.0
    if 20 <= t and t <= 22:
        return 5.5
    if 23 <= t and t <= 26:
        return 6.0
    if 27 <= t and t <=29:
        return 6.5
    if 30 <= t and t <=32:
        return 7.0
    if 33 <= t and t <= 34:
        return 7.5
    if 35<t and t <=36:
        return 8.0
    if 37 <= t and t <= 38:
        return 8.5
    if 39 <= t and t <= 40 :
        return 9.0

for _ in range(int(input())):
    a=input().split()
    x=int(a[0])
    y=int(a[1])
    z=float(a[2])
    t=float(a[3])
    r = doi(y)
    l= doi(x)
    tb = ( r + l + z + t)/4.0
    m = int (tb)
    if tb - m >= 0.75  :
        m += 1.0
    elif tb - m >= 0.25:
        m += 0.5
    print (m)
