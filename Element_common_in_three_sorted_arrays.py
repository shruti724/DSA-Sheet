def commonEle(a, b, c):
    for d in range(0, len(a)):
        for e in range(0, len(b)):
            for f in range(0, len(c)):
                if a[d] == b[e] == c[f]:
                    print(a[d])

t = int(input())
for i in range(t):
    n = int(input())
    arr1 = [int(x) for x in input().strip().split()]
    m = int(input())
    arr2 = [int(x) for x in input().strip().split()]
    o = int(input())
    arr3 = [int(x) for x in input().strip().split()]
    commonEle(arr1, arr2, arr3)

# op:
# 1
# 4
# 1 2 3 4
# 4
# 2 3 4 5
# 4
# 1 3 2 4
# 2
# 3
# 4