def duplicates(lis):
    for j in range(0, len(lis)):
        for k in range(j + 1, len(lis)):
            if lis[j] == lis[k]:
                print(lis[k], end=" ")


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    duplicates(arr)
# op:
# 1
# 5
# 4 1 1 5 4
# 4 1
#