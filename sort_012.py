# l = [0, 2, 1, 0, 0, 1]
# l.sort()
# print(l)
# op: [0, 0, 0, 1, 1, 2]


def sorting(lis):
    for i in range(0, len(lis)):
        if lis[i] >= lis[i + 1]:
            temp = lis[i]
            lis[i] = lis[i + 1]
            lis[i + 1] = temp
        print(lis)

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    sorting(arr)

# op:
# 1
# 2
# 4 1
# Traceback (most recent call last):
#   File "C:\Users\91912\PycharmProjects\array_36\sort_012.py", line 19, in <module>
#     sorting(arr)
#   File "C:\Users\91912\PycharmProjects\array_36\sort_012.py", line 9, in sorting
#     if lis[i] >= lis[i + 1]:
# IndexError: list index out of range
# [1, 4]

# swapping
# num1 = 5
# num2 = 1
# temp = num1
# num1 = num2
# num2 = temp
# print(num1, num2)
# op: 1, 5


# lis = [5, 4, 3, 2, 1]
# for i in lis:
#      if i > i + 1:
#         print("yes")
#      print("no")
#
# op:
# no
# no
# no
# no
# no


# def sorting(lis):
#     for i in range(0, len(lis)):
#         for j in range(i + 1, len(lis)):
#             if lis[i] > lis[j]:
#                 temp = lis[i]
#                 lis[i] = lis[j]
#                 lis[j] = temp
#     print(lis)
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = [int(x) for x in input().strip().split()]
#     sorting(arr)
#
# op:
# 1
# 4
# 0 2 1 0
# [0, 0, 1, 2]


# lis = [5, 4, 3, 2, 1]
# print(lis[0])
# op: 5

# lis = [5, 1, 3, 2, 1]
# for i in lis:
#      print(lis[i - 1], end=" ")
# op: 1 5 3 1 5


