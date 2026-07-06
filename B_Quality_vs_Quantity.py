for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()

    blue=a[0]
    red=0
    j=n-1
    flag=False
    
    for i in range(1,n):
        if i>=j:
            break
        blue += a[i]
        red += a[j]
        if red>blue:
            flag=True
            break
        j-=1

    print("YES" if flag else "NO")
