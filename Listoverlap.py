set1 = []
set2 = []
n = int(input("Enter number of elements you want in list 1: "))
x = int(input("Enter number of elements you want in list 2: "))
# iterating till the range
for i in range(0, n):
    ele1 = int(input("Enter elements for list 1: "))
    set1.append(ele1)
for j in range(0, x):
    ele2 = int(input("Enter elements for list 2: "))
    set2.append(ele2)

repeat = set1[0]
subset = []
for number in set1:
    if number not in set2:
        subset.append(number)
print(f'The numbers that are not present from list 1 in list 2 are {subset}')
