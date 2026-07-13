t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    diff = []
    for i in range(n // 2):
      # s=101100
      # i=0  5
      # i=1  4  
        if s[i] != s[n - 1 - i]:
             diff.append(i)
#           s = 101001
#      0-5
# 1-4
# 2-3
    if not diff:
        print("Yes")
#       diff =[2 3 4]
# diff[-1]=4

#   4-1=1=4
# len(diff)=3
    elif diff[-1] - diff[0] + 1 == len(diff):
      # print("yes")
        print("Yes")
    else:
        print("No")
