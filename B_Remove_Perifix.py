t = int(input())
for _ in range(t):
    n = int(input())
    arr= list(map(int, input().split()))
    visited = set()
    ans = 0
    i = n - 1
    while i >= 0:
        if arr[i] in visited:
            ans = i + 1
            break
        # else:
        visited.add(arr[i])
        i= i - 1

    print(ans)
    
    # 4
    # 3 1 4 3 
    # i  arr[i] visited
    # 3   3      {}     3
    # 2   4      {3}    4
    # 1   1       {3,4}  1
    # 0   3      {3,4,1} 0+1=1
