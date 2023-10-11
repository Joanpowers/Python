#write a python program to reverse a string
[1,2,3,4,"a","b","c","d"]
input_string = "a","b","c","d"

reversed_string = input_string[::-1]

print(reversed_string)

#write a python function to multiply all the numbers in a list
x=[8,2,3,-1,7]

def product_of_list(numbers):
    # Initialize the product to 1
    product = 1

    # Iterate through the list and multiply each number with the product
    for n in numbers:
        product *= n

    return product

x = [8, 2, 3, -1, 7]
result = product_of_list(x)
print(f"The product of the numbers in the list is: {result}")

#write a python program to print the even numbers from the list
x = [1,2,3,4,5,6,7,8,9]
for even_numbers in x:
    if even_numbers % 2 == 0:
        print(even_numbers)