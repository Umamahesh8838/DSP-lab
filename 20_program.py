import copy

# Shallow copy example
original_list = [[1, 2], [3, 4]]
shallow_copy = copy.copy(original_list)

# Modify the shallow copy
shallow_copy[0][0] = 99

print("Original list after shallow copy modification:", original_list)
print("Shallow copy:", shallow_copy)

# Deep copy example
original_list = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original_list)

# Modify the deep copy
deep_copy[0][0] = 99

print("Original list after deep copy modification:", original_list)
print("Deep copy:", deep_copy)
