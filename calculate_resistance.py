# calculate the resistance series and parallel
# input 3 float numbers and then code = 1 for series, code =2 parallel
# count that how many of series and parallel circuit
# input 10 set


# initial var
n = 1
p = 0
s = 0

# process
while n <= 10:
    # input data
    resistance_first = float(input("Enter first resistance:"))
    resistance_second = float(input("Enter second resistance:"))
    resistance_third = float(input("Enter third resistance:"))
    code = int(input("Enter code (series = 1 / parallel = 2):"))

    # condition for code
    if code == 1:
        total_series = resistance_first + resistance_second + resistance_third
        print(f"Total series resistance is {total_series}")
        s = s+1
    else:
        total_parallel = (1/resistance_first + 1 /
                          resistance_second + 1/resistance_third)**(-1)
        print(f"Total parallel resistance is {total_parallel}")
        p = p+1

    n = n+1
print(
    f"Total series circuit are {s} circuit and total parallel circuit are {p} circuit")
