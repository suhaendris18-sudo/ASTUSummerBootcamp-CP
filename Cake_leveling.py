for _ in range(int(input())):
        n=int(input())
        arr=[int(x) for x in input().split()]
        zsum=0
        zmin=float("inf")
        ans=[]
        for i in range(n):
            zsum+=arr[i]
            av=zsum//(i+1)
            zmin=min(zmin,av)
            ans.append(zmin)
        print(*ans)
