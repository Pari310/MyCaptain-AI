# Function to print all positive numbers in a list
def print_positive_num(numbers):
    # Initialize an empty list to store positive numbers
    positive_numbers = []

    # Loop through each number in the input list
    for num in numbers:
        # Check if the number is positive
        if num > 0:
            # Add the positive number to the list
            positive_numbers.append(num)

    # Return the list of positive numbers
    return positive_numbers


# Example usage:
l1 = [12, -7, 5, 64, -14]
l2 = [12, 14, -95, 3]

# Get positive numbers from list1
positive_numbers_l1 = print_positive_num(l1)
print("Input: list1 =", l1)
print("Output:", positive_numbers_l1)

# Get positive numbers from list2
positive_numbers_l2 = print_positive_num(l2)
print("Input: list2 =", l2)
print("Output:", positive_numbers_l2)
