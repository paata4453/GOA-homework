# list
# dict
# set
# aris mutable



# int
# float
# str
# tuple
# immuteble



# Lambda ფუნქციაა anonymous function



# map გამოიყენება ელემენტის ტრანსფორმაციისთვის




# filter არის ისეთი ელემენტების შესარჩევად რომლებიც აკმაყოფილებენ პირობას




# ორი სტრინგის შეერთებას ქვია concatenation





# მაპ


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)






celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)







words = ["hello", "world", "python"]
capitalized_words = list(map(lambda word: word.capitalize(), words))
print(capitalized_words)





# ფილტრები

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)





words = ["cat", "house", "tree", "car"]
long_words = list(filter(lambda word: len(word) >= 4, words))
print(long_words)






numbers = [3, 9, 15, 22, 27, 30]
multiples_of_three = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_three)  