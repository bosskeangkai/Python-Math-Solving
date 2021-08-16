# input three number and then check what is the max or min number and then finally show on your screen
# while loop 5 time

# คำสั่ง if เเบบ 1 ทางเลือก
# do only if for check

# initail
max = 0
min = 0
n = 1

# process

# while loop check if n <= 5 loop
while n <= 5:
    x = int(input("Enter your X number:"))
    y = int(input("Enter your Y number:"))
    z = int(input("Enter your Z number:"))

    # if-else condition
    if(x > y and x > z):
        max = x
    if(x < y and x < z):
        min = x
    if(y > x and y > z):
        max = y
    if(y < x and y < z):
        min = y
    if(z > x and z > y):
        max = z
    if(z < x and z < y):
        min = z

    # output
    print(
        f"The number that I had to input was {x,y,z} and the max and min number is {max,min}")

    # input 4 5 6
    # The number that I had to input was (4, 5, 6) and the max and min number is (6, 4)

    # loop until n > 5
    n = n+1

print("End")
