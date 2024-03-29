# Create a list of variables + define the range
start = 1 
end = 100 

# Define a variable to hold an empty number as a "string" - thanks Network Chuck.
number = ""

# Loop through each number in the range
for number in range(start, end + 1):
    # Checking divisibility and print functions
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
