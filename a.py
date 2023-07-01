S = [int(s) for s in input().split()]

ans = 'Yes'
for i in range(len(S)):
    if i == len(S) - 1:
        condition1 = True
    else:
        condition1 =  S[i] <= S[i+1]
    
    condition2 = 100 <= S[i] <= 675

    condition3 = S[i] % 25 == 0

    if condition1 and condition2 and condition3:
        continue
    else:
        ans = 'No'

print(ans)