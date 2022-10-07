def largestSum(lis):
    prev, curr = 0, i
    for j in range(0, len(lis)):
        curr = curr + lis[j]
        if curr < prev:
            curr = prev
        if prev < 0:
            prev == 0
    return curr


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    largestSum(arr)

# lis = [1, 2, 3, 4, 5]
# for i in range(0, len(lis)):
#     for j in range(i + 1, len(lis)):
#         s = int(lis[i]) + int(lis[j])
#         print(s, end=' ')
# op: 6 7 8 9 9

# lis = [1, 2, 3, 4, 5]
# for i in range(0, len(lis)):
#     print(int(lis[i]) + 1, end=' ')
# op: 2 3 4 5 6


