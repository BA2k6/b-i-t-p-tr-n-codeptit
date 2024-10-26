a,b,c = input().split()
if int(a)>0 and int(b)>0:
    cv = (int(a) + int(b)) * 2
    dt = int(a) * int(b)
    print(cv, dt, c.capitalize())
else:
    print("INVALID")
