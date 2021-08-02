t  = int(input())
for i in range(t):
    m = 0
    n,d,h = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(n):
        if l[i]>0:
            m += l[i]
        else:
            if m<d:
                m = 0
            else:
                m = m - d
        if m>h:
            print("YES")
            break
    else:
        print("NO")
