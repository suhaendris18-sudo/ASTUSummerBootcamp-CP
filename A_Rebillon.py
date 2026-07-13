for i  in range(int(input())):
    n=int(input())
    arry=list(map(int,input().split()))
    l=0
    r=n-1
    count=0
    while l<r:
        if arry[l]==1 and arry[r]==0:
            r+l
            count+=1
            l+=1
            r-=1
        elif arry[l] ==0:
            l+=1
        else: r-=1
      
    print(count)
