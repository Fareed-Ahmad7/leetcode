a = 544938
b = 7

product = f"{a*b}"
num_of_digits = 0
for i in product:
    num_of_digits += 1
print(num_of_digits)

# status : failed! cuz it also counts '-' symbol in the product of negative numbers