def merge(lis1, lis2):
    for j in range(0, n):
        for k in range(0, m):
            if lis1[j] < lis2[k]:
                print(lis1[j])
                j += 1
            elif lis1[j] > lis2[k]:
                temp = lis1[k]
                lis1[j] = lis2[k]
                lis2 = temp
                print(lis1[k])
                k += 1
            else:
                if lis1[j] == lis2[k]:
                    print(lis1[j])
                    j += 1
                    k += 1


t = int(input())
for i in range(t):
    n = int(input())
    arr1 = [int(x) for x in input().strip().split()]
    m = int(input())
    arr2 = [int(x) for x in input().strip().split()]
    merge(arr1, arr2)