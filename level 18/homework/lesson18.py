list1 = [2, 51, 11, 13, 51, 100]


print("პოხიტიური:")
for i in range(len(list1)):
    print(f"Index {i}: {list1[i]}")


print("\nნეგატიური:")
for i in range(-len(list1), 0):
    print(f"Index {i}: {list1[i]}")


list1[-1] = 99  
print("\nList after replacing the last element:", list1)


list1[4] = 77 
print("List after replacing the fifth element:", list1)