for _ in range(int(input())):
    n=int(input())
    s=input()
    ans=0
    see=set()
    for i in range(n):
        if  s[i] in see:
            ans+=1
        else:
            ans+=2
            see.add(s[i])
    print(ans)
