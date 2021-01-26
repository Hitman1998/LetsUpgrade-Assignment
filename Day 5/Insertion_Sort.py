lst = [int(i) for i in input().split()]
n = len(lst)
for j in range(1, n):
    key = lst[j]
    i = j - 1
    while i >= 0 and lst[i] > key:
        lst[i + 1] = lst[i]
        i = i - 1
    lst[i + 1] = key

print(lst)