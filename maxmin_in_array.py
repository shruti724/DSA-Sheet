# l = [1, 2, 3, 4]
# print("max is:",max(l),'and', end="")
# print(" min is:",min(l))
# op: max is: 4 and min is: 1

def maxmin(s):
    print(max(s), min(s))

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    maxmin(arr)
