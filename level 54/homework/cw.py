numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda num: num * 2, numbers))
print((doubled_numbers))



names = ["Alice", "Bob", "Charlie"]
greeted_names = list(map(lambda name: "Hello, " + name, names))
print(greeted_names)





fruits = ["apple", "banana", "kiwi"]
lengths = (list(map(len, fruits)))
print(lengths)





numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = (list(filter(lambda num: num > 0, numbers)))
print(positive_numbers)






words = ["pear", "apple", "peach", "grape"]
p_words = (list(filter(lambda word: word.startswith('p'), words)))
print(p_words)

