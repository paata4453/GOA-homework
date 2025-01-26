numbers = [10, 35, 50, 42, 25, 60, 30, 40]
numbers_40= (list(filter(lambda num: num >= 40, numbers)))
print(numbers_40)


numbers = [2, 4, 6, 8, 10]
numbers1 = (list(map(lambda num: num ** 2, numbers)))
print(numbers1)


word1 = ["appla", "banana", "gio", "ka", "mango", "jopa"]
word2 = filter(lambda word: word[-1] == 'a', word1)
print(list(word2))

