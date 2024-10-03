#17.	Write a Python program that creates a tuple, accesses its elements, and demonstrates the immutability of tuples.

my_tuple = (1, 2, 3, 4, 5)

print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error:", e)