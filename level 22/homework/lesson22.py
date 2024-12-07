
def check_discount(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didnt got discount"


print(check_discount(16)) 
print(check_discount(20))  





def manual_reverse(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string


print(manual_reverse("Hello")) 





some_string = "Hello World"


print(some_string.upper()) 


print(some_string.lower()) 


print(some_string.capitalize()) 


print(some_string.swapcase())


print(some_string.find("World"))
