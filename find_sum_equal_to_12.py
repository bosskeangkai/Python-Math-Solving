# Input 3 digits number and then find that what number has sum of three digits equal to 12 then showed to the answer if don't have any number
# print Sum Digit not qual 12

# initail number 3 numbers
n = 1


# while loop condition
while n <= 4:
    number = int(input("Enter your 3 digit number:"))

    # separate digit
    first_digit = number % 10
    second_digit = (number//10) % 10
    third_digit = number//100

    sum = first_digit + second_digit + third_digit

    # condition
    if sum == 12:
        print(
            f"Each digit of number is {third_digit,second_digit,first_digit}")
        print(f"Total sum is {sum}")
    else:
        print(number)
        print('Sum Digit not equal 12')

# n = n +1 is loop execute
n = n + 1
# Each digit of number is (6, 5, 1)
# Total sum is 12
