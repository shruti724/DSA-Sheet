def cyclically_rotated(lis):
    for j in range(0, len(lis)):
        print(lis[j - 1], end=" ")


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    cyclically_rotated(arr)

# op:
# 1
# 5
# 2 1 3 4 6
# 6 2 1 3 4
