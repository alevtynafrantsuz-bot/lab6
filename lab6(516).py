str = input()

collection = {}

for symbol in str:
    if symbol in collection:
        collection[symbol] = collection[symbol]+1
    else:
        collection[symbol] = 1

print(collection)

