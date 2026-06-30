igf-ymys-ygc

Marya Tawfik
21:58
for _ in range(int(input())):
    n=int(input())
    old=list(map(int,input().split()))
    new=sorted(old)
    if len(old) == 1:
        print(-1)
    else:
        for i in range(n-2):
            if old[i] == new[i]:
                new[i],new[i+1] = new[i+1],new[i]
        if new[n-2] == old[n-2]:
            new[n-2],new[n-1]=new[n-1],new[n-2]
        elif new[n-1] == old[n-1]:
            new[n-2],new[n-1]=new[n-1],new[n-2]
        print(*new)

# 4-2=2[0,1]    

# 2 3 1 4

# 1 2 3 4
# i=0,1,
            


























# perms = itertools.permutations(data)
# # print(perms)(key,val)

# arr=[]
# for p in perms:
#     arr.append(p)

# arr.sort()
# for i in arr:
#     if i != data:
#         print(i)
#         break
