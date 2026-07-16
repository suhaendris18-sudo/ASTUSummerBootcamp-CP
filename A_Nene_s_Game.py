t = int(input())
for _ in range(t):
    k, q=map(int, input().split())
    arr=list(map(int, input().split()))
    querie= list(map(int, input().split()))
    minimum=min(arr)
    ans=[]
    for i in querie:
        if i < minimum:
            ans.append(i)
        else:
            ans.append(minimum-1)
    print(*ans) 
