list1 = []
n = int(input("Enter number of elements:"))
for i in range(0,n):
    element = int(input())
    list1.append(element)
list2 = []
for i in list1:
    if i%2 == 0:
        list2.append(i)
print(list2)