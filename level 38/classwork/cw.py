number =[ i for i in range(1, 101)]
print(number)



number1 =[ i for i in range(1, 101, 2)]
print(number1)



names = ["Anna", "Michael", "Laura", "John", "Alice"]
diffenrent_names = [f"#{name}" for name in names if "a" not in name.lower()]
print(diffenrent_names)
