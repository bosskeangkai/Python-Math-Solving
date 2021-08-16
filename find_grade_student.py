# input id score Thai Eng Math then find summation if scores and Avarage score
# check if avg score more than 60 and eng score more than or equal to 70 give pass then keep in grade var or not give fail

# initial
n = 1
grade = 0
sum = 0

# Process
while n <= 5:
    # input var
    id = int(input("Enter your id:"))
    score_thai = int(input("Enter your Thai score:"))
    score_Eng = int(input("Enter your English score:"))
    score_math = int(input("Enter your Math score:"))

    # calculate sum and avg
    sum = score_thai + score_Eng + score_Eng
    avg = int(sum/3)

    # condition
    if avg > 60 and score_Eng >= 70:
        grade = "PASS"
    else:
        grade = "Fail"

    # Show data
    print(f"id{id} Thai score {score_thai} English score {score_Eng} Math score {score_math} Total scores {sum} Average score {avg} and Grade {grade} ")

    # loop while
    n = n + 1


else:
    print("End Thank you")
