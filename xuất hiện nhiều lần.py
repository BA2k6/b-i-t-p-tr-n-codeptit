for t in range(int(input())):
    n=int(input())
    b=[int(i) for i in input().split()]
    a={}
    for x in b:
        if x in a:
            a[x]+=1
        else :
            a[x]=1
    c = 0
    for i,j in a.items():
        if j > n//2:
            c=1
            print(i)
            break
    if c == 0 : print("NO")

