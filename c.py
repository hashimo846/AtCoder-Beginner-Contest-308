from functools import cmp_to_key

N = int(input())
P = []
for i in range(N):
    a, b = map(int, input().split())
    P.append([a/(a+b), i+1])

def compare_func(x1, x2):
    if x1[0] != x2[0]:
        return 1 if x1[0] < x2[0] else -1
    else:
        return -1 if x1[1] < x2[1] else 1

P.sort(key = cmp_to_key(compare_func))

ans = [str(p[1]) for p in P]
print(' '.join(ans))