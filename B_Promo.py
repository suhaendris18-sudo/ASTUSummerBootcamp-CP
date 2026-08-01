n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort(reverse=True)
pref = [0] * (n + 1)
for i in range(n):
    pref[i + 1] = pref[i] + p[i]
for _ in range(q):
    x, y = map(int, input().split())
    ans = pref[x] - pref[x - y]
    print(ans)
