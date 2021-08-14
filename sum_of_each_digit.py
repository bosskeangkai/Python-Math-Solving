# find the sum of each digit of variable number
# give number = 6789

# Initial value
number = int(input("Enter the 4 digit number:"))

# Process
digit_one = number % 10
digit_two = (number//10) % 10
digit_three = (number//100) % 10
digit_four = number//1000

# Calculate
sum_of_digit = digit_one + digit_two + digit_three + digit_four

# output
print("digit one is", digit_one)
print("digit two is ", digit_two)
print("digit three is", digit_three)
print("digit four is ", digit_four)

print(f"The all of digit {digit_one,digit_two,digit_three,digit_four}")
print(f"The sum of each digit is {sum_of_digit}")

# Terminal
# Enter the 4 digit number: 6789
# digit one is 9
# digit two is 8
# digit three is 7
# digit four is 6
# The all of digit(9, 8, 7, 6)
# The sum of each digit is 30
