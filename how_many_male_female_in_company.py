# calculate how many male and female in the company
# give male code =1 and female code = 2
# id name sex code and amount of there male and female

# initail
f = 0
m = 0
n = 0

# process
while n <= 5:
    # input var
    id = int(input("Enter your id:"))
    name = input("Enter your name:")
    code = input("Enter your sex (1 = male / 2 = female):")

    # condition
    if code == 1:
        m = m + 1
    else:
        f = f + 1

    # show data
    print(f"id {id} name {name} sex {code} ")

    # while loop
    n = n+1

else:
    print(f"male {m} person female {f} person")
