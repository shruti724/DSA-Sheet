# li = [1, 2, 3, 4]
# print(li[::-1])
# op: [4, 3, 2, 1]

def reverse(y):
    print(y[::-1])


t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    reverse(arr)
# But if do print(reverse(arr)), it will reverse the list but in addition None will be also returned.
# because reverse() is not retuning anything and we are just print the result.
# op:
# 1
# 3
# 1 2 3
# [3, 2, 1]
