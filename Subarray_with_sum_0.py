def zeroSum(lis):
    initialsum = 0
    curr = 0
    is_sum_zero = False
    for j in range(0, len(lis)):
        initialsum = curr
        for k in range(0, len(lis)):
            if curr == 0:
                is_sum_zero = True
            else:
                is_sum_zero = False
    print(is_sum_zero)


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    zeroSum(arr)

# op:
# 1
# 5
# -1 1 2 3 4
# True
