from collections import Counter

a = list(map(int, input().split()))
MOD = 10**9 + 7
f = [1, 2]
while f[-1] <= 2 * max(a):
    f.append(f[-1] + f[-2])

freq = Counter()
ans = 0

for x in a:
    for v in f:
        y = v - x
        if y in freq:
            ans += freq[y]
    freq[x] += 1

print(ans % MOD)
