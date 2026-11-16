
# Define two vectors
vector_a = [6, 4]
vector_b = [2, 3]

# Display the original vectors
print("Vector A:", vector_a)
print("Vector B:", vector_b)

# Subtract X components (index 0): 6 - 2 = 4
x_difference = vector_a[0] - vector_b[0]
print("Difference of X components:", x_difference)

# Subtract Y components (index 1): 4 - 3 = 1
y_difference = vector_a[1] - vector_b[1]
print("Difference of Y components:", y_difference)

# Combine X and Y differences into a resultant vector
result_vector = [x_difference, y_difference]
print("Resultant vector (A - B):", result_vector)
