def zeroSum(lis):
    curr = 0
    is_sum_zero = False
    for j in range(0, len(lis)):
        curr = curr + lis[j]
        if curr == 0:
            is_sum_zero = True
        else:
            is_sum_zero = False
    return is_sum_zero


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(zeroSum(arr))

# op:
# 1
# 4
# -1 2 3 -4
# True

# 1
# 4
# 1 2 3 4
# False
