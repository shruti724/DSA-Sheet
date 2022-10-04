def negSort(lis):
    for i in range(0, len(lis)):
        for j in range(i + 1, len(lis)):
            if lis[j] < 0:
                temp = lis[j]
                lis[j] = lis[i]
                lis[i] = temp
    print(lis)

t = int(input())
for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().strip().split()]
    negSort(arr)