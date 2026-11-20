words1 = input().split()
words2 = input().split()

first_words = {}
for word in words1:
    first_words[word] = True
result = ""

common_words = {}
for word in words2:
    if word in first_words:
        common_words[word] = True

print(*sorted(common_words, reverse=True))