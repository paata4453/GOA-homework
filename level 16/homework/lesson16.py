

# 2
produqti = 1
for i in range(1, 11):
    produqti *= i
print("ნამრავლი 1დან 10(for loop):", produqti)

# 3
product = 1
i = 1
while i <= 10:
    product *= i
    i += 1
print("ნამრავლი 1დან 10(while loop):", product)

# 4
number = int(input("input number: "))
if number % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")

# 5
score = int(input("შეიყვანე score (0-100): "))
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")


