my_list = [10, 20, 30, 40]

# 1. 
print("Length:", len(my_list))  

# 2. 
my_list.append(50)
print("After append:", my_list)  

# 3. 
my_list.insert(2, 25)  
print("After insert:", my_list)  

# 4. 
popped = my_list.pop()
print("Popped element:", popped) 
print("After pop:", my_list)     

# 5. 
my_list.remove(25) 
print("After remove:", my_list) 






my_list = [10, 20, 30, 40, 50]

removed_element = my_list.pop(2)  

print(removed_element)  
print(my_list)           



#pop როდესაც ამოშლის შემდეგ აბრუნებს და remove არ აბრუნებს და იშლება სამუდამოდ




my_list = [10, 20, 30, 40]

my_list.insert(2, 25)  

print( my_list) 
