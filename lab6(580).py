def search (List1, List2):
    result = {}
    for number in List1:
        if number in  List2:
            result[number] = False
        else:
            result[number] = True

    return result

numbers1 = input().split()
numbers2 = input().split()

list1 = search(numbers1, numbers2)
list2 = search(numbers2, numbers1)

arr1 = []
arr2 = []

for number, state in list1.items():
    if state == True:
        arr1.append(number)

for number, state in list2.items():
    if state == True:
        arr2.append(number)

print(*arr1)
print(*arr2)