def area(side_length):
    # Calculate the area of the square
    square_area = side_length ** 2
    return square_area

# Input: Get the side length from the user
side_length = int(input("Enter the side length of the square: "))

# Calculate the area using the area() function
square_area = area(side_length)

# Display the result
print(f"The area of the square with side length {side_length} is {square_area}.")
