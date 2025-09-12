# Q1
# name = input("Enter Name: ");
# print(f"Hello, {name}! Welcome to the Python assignment.")

# String methods
# Print the user’s name in all uppercase letters.
name="Zuraiz Khan"
print(name.upper());

# Print the user’s name in all lowercase letters.
print(name.lower())

# Print the length of the user’s name (number of characters).
print(name.__len__())


# Replace all the spaces in the user’s name with hyphens (-), and print the result.
print(name.replace(' ','-'))

# Bonus: Trim any leading or trailing spaces (if any) from the user’s name using strip().
name=" Zuraiz Khan "
print(name.strip())

# Type casting and numeric operations

# Ask the user to enter their birth year (as input). Convert that input to an integer.
# Calculate the user’s approximate age by subtracting the birth year from the current year. Print the result in a sentence.
# Example output:
by= input("Enter Birthday Year: ");
now = datetime.now();
print(f"Current by is {by}, so you are approximately {24} years old.")

