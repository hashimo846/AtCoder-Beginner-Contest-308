temp = [int(s) for s in input().split()]
N, M = temp[0], temp[1]
C = list(input().split())
D = list(input().split())
P = [int(s) for s in input().split()]
other_price = P[0]
price_dict = dict(zip(D, P[1:]))

D = set(D)
ans = 0
for c in C:
    if c in D:
        ans += price_dict[c]
    else:
        ans += other_price

print(ans)