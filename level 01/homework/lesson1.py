# name= "pati"
# #name არის ცვლადი 
# #= არის ცვლადისტვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# # "paata" არის ცვლადისთის მნიშვნელობა

# surname = "cucqa"

# #print(name)
# # პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

# name= "pata" # ეს არის str ტიპის ცვლადი
# age = 13 #ეს არის integer მთელი რიცხვი
# height = 160 # ეს არის float ტიპის ცვლადი 
# #boolean  ტიპის ცვლადი 

# knows_proggraming = True # true  ან  false
# is_ugly=False 




# print(name + " " + surname)


# #name(name + age)

# #print(type(age))
# #print(type(name))
# #print(type(surname))
# #print(type(height))
# #print(type(knows_proggraming))

# print("me var" + " "+ name +" "+surname+" "+ str(age) +" "+ "wlis"+" "+"vcxovrob mukhiansi"+" "+"me var"+" "+str(height) +" " +"santimetri"  )


import os

def get_empty_directories(path):
   empty_dirs = []
   for dirpath, dirnames, filenames in os.walk(path):
      if not dirnames and not filenames:
         empty_dirs.append(dirpath)
   return empty_dirs


path_to_search = 'C:/Users/USER/Desktop/GOA-homework'
empty_directories = get_empty_directories(path_to_search)
print(empty_directories)