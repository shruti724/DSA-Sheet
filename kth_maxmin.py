# Printing 2nd largest element (k = 2)

# l = [1, 2, 54, 3, 78]
# inx = l.index(max(l))
# l.pop(inx)
# print(max(l))
# op: 54

t = int(input())
for i in range(t):
    n = int(input())
    p = [int(x) for x in input().strip().split()]
    k = int(input())
    inx = max(p)

    for j in range(1, k+1):
        q = p.index(inx)
        s = p.pop(q)
    print(max(p))

# k = int(input())
#
#
# for j in range(1, k+1):
#
#     print(j, end=" ")

