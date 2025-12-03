# 1. Find the largest of three numbers
num1 = int(input("Halnu hos first number: "))
num2 = int(input("Halnu hos second number: "))
num3 = int(input("Halnu hos third number: "))

max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3

print("Largest number is:", max_num)


# 2. Month number to month name
month_input = int(input("Month ko number halnu hos (1-12): "))

if month_input == 1:
    print("January")
elif month_input == 2:
    print("February")
elif month_input == 3:
    print("March")
elif month_input == 4:
    print("April")
elif month_input == 5:
    print("May")
elif month_input == 6:
    print("June")
elif month_input == 7:
    print("July")
elif month_input == 8:
    print("August")
elif month_input == 9:
    print("September")
elif month_input == 10:
    print("October")
elif month_input == 11:
    print("November")
elif month_input == 12:
    print("December")
else:
    print("Invalid month number")


# 3. Swap two values
val1 = input("Enter first value: ")
val2 = input("Enter second value: ")
print("Before swap: val1 =", val1, "val2 =", val2)
temp = val1
val1 = val2
val2 = temp
print("After swap: val1 =", val1, "val2 =", val2)


# 4. Movie ticket system
age_person = int(input("Tapaiko age halnu hos: "))
member_card = input("Membership cha? (yes/no): ").lower()

if age_person < 12:
    print("Ticket free")  # child free
elif 12 <= age_person <= 60:
    if member_card == "yes":
        print("Ticket cost: Rs 150")
    else:
        print("Ticket cost: Rs 200")
else:
    print("Ticket cost: Rs 100")  # senior citizen


# 5. Electricity billing
units = int(input("Enter electricity usage (units): "))

if units < 100:
    cost = units * 5
elif units <= 300:
    cost = 100 * 5 + (units - 100) * 8
else:
    cost = 100 * 5 + 200 * 8 + (units - 300) * 10

print("Total electricity bill: Rs", cost)


# 6. Rock, Paper, Scissors
player1 = input("Player1 move: rock/paper/scissors ").lower()
player2 = input("Player2 move: rock/paper/scissors ").lower()

if player1 == player2:
    print("Match Tie")
elif (player1 == "rock" and player2 == "scissors") or \
     (player1 == "paper" and player2 == "rock") or \
     (player1 == "scissors" and player2 == "paper"):
    print("Player1 Wins")
else:
    print("Player2 Wins")


# 7. Minimum desks needed
stu1 = int(input("Class1 students kati cha?: "))
stu2 = int(input("Class2 students kati cha?: "))
stu3 = int(input("Class3 students kati cha?: "))

desk1 = (stu1 + 1) // 2
desk2 = (stu2 + 1) // 2
desk3 = (stu3 + 1) // 2

total_desk = desk1 + desk2 + desk3
print("Minimum desks required:", total_desk)


# 8. Lift system
lift_floor = 5
user_floor = int(input("Kun floor chahiyo?: "))

if user_floor > lift_floor:
    print("Lift is going up")
elif user_floor < lift_floor:
    print("Lift is going down")
else:
    print("Lift already yahi floor ma cha")


# 9. Positive and Even/Odd check
number = int(input("Enter a number: "))

if number > 0:
    print("Number is positive")
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is not positive")


# 10. Greater number or positive/negative/zero check
n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))

if n1 > n2:
    print("Greater number is", n1)
elif n2 > n1:
    print("Greater number is", n2)
else:
    print("Numbers are equal")
    if n1 > 0:
        print("Number is positive")
    elif n1 < 0:
        print("Number is negative")
    else:
        print("Number is zero")


# 11. FizzBuzz
num_input = int(input("Enter number: "))

if num_input % 3 == 0 and num_input % 5 == 0:
    print("FizzBuzz")
elif num_input % 3 == 0:
    print("Fizz")
elif num_input % 5 == 0:
    print("Buzz")
else:
    print(num_input)


# 12. Random Snapple facts
import random
rand_num = random.randint(0, 5)

if rand_num == 0:
    print("Flamingos turn pink from eating shrimp.")
elif rand_num == 1:
    print("Honey never spoils.")
elif rand_num == 2:
    print("Shrimp can swim only backwards.")
elif rand_num == 3:
    print("Taste bud lives about 10 days.")
elif rand_num == 4:
    print("Cannot sneeze while sleeping.")
else:
    print("Singing off-key illegal in North Carolina.")


# 13. Store discount
purchase = float(input("Enter total purchase amount: "))
member = input("Are you member? (True/False): ").title() == "True"

if purchase > 1000 and member:
    final = purchase * 0.8
elif purchase > 1000 and not member:
    final = purchase * 0.9
else:
    final = purchase

print("Final amount to pay: Rs", final)


# 14. Weight on planets
earth_wt = float(input("Earth weight kg: "))
planet_num = int(input("Planet number 1-7: "))

if planet_num == 1:
    wt = earth_wt * 0.38
elif planet_num == 2:
    wt = earth_wt * 0.91
elif planet_num == 3:
    wt = earth_wt * 0.38
elif planet_num == 4:
    wt = earth_wt * 2.53
elif planet_num == 5:
    wt = earth_wt * 1.07
elif planet_num == 6:
    wt = earth_wt * 0.89
elif planet_num == 7:
    wt = earth_wt * 1.14
else:
    wt = None

if wt is not None:
    print("Your weight on planet", planet_num, "is:", wt)
else:
    print("Invalid planet number")


# 15. Marks, percentage, grade
m1 = float(input("Subject1 marks: "))
m2 = float(input("Subject2 marks: "))
m3 = float(input("Subject3 marks: "))
m4 = float(input("Subject4 marks: "))

total_marks = m1 + m2 + m3 + m4
perc = (total_marks / 400) * 100

if perc > 70:
    grd = "Distinction"
elif perc > 60:
    grd = "First"
elif perc > 40:
    grd = "Pass"
else:
    grd = "Fail"

print("Total:", total_marks, "Percentage:", perc, "Grade:", grd)


# 16. Bike road tax
bike_price = float(input("Bike cost (Rs): "))

if bike_price > 100000:
    tax = bike_price * 0.15
elif bike_price > 50000:
    tax = bike_price * 0.1
else:
    tax = bike_price * 0.05

print("Road tax Rs", tax)


# 17. Employee bonus
yrs = float(input("Years of service: "))

if yrs > 10:
    bonus_percent = 10
elif yrs >= 6:
    bonus_percent = 8
else:
    bonus_percent = 5

print("Bonus %:", bonus_percent)


# 18. Subject score advice
sub_score = float(input("Subject score: "))

if sub_score > 90:
    print("Excellent! Congratulations")
elif sub_score >= 50:
    print("Good, but improve")
else:
    print("Retake the course")


# 19. Job eligibility
age_candidate = int(input("Candidate age: "))
deg = input("Degree cha? (Yes/No): ").title() == "Yes"
exp = float(input("Work experience (yrs): "))

if age_candidate >= 18:
    if deg:
        if exp > 3:
            print("Highly Eligible")
        elif exp >= 1:
            print("Eligible")
        else:
            print("Under Review")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")


# 20. Wages based on age/gender/days
emp_age = int(input("Age: "))
emp_gender = input("Gender (M/F): ").upper()
emp_days = int(input("Days worked: "))

if emp_age >= 18 and emp_age < 30:
    wage_day = 700 if emp_gender == "M" else 750
elif emp_age >= 30 and emp_age <= 40:
    wage_day = 800 if emp_gender == "M" else 850
else:
    wage_day = 0

total_wage = wage_day * emp_days
if wage_day > 0:
    print("Total wages Rs", total_wage)
else:
    print("Age not eligible for wages")


# 21. Simple ATM
atm_valid = True
balance_amt = 50000
atm_pin = 123

if atm_valid:
    pin_input = int(input("Enter ATM PIN: "))
    if pin_input == atm_pin:
        print("1. Withdraw\n2. Check Balance\n3. Exit")
        opt = int(input("Choose option: "))
        if opt == 1:
            amt = float(input("Amount to withdraw: "))
            if amt <= balance_amt:
                balance_amt -= amt
                print("Withdraw success, balance Rs", balance_amt)
            else:
                print("Insufficient balance")
        elif opt == 2:
            print("Current balance Rs", balance_amt)
        elif opt == 3:
            print("Thank you for visiting")
        else:
            print("Invalid option")
    else:
        print("Wrong PIN")
else:
    print("Card invalid")


# 22. Magic Forest Game
print("Welcome to the Magic Forest")
dir1 = input("Go 'north' or 'south'? ").lower()

if dir1 == "south":
    print("Game Over")
elif dir1 == "north":
    dir2 = input("Cross river or follow path? ").lower()
    if dir2 == "cross river":
        print("Game Over")
    elif dir2 == "follow path":
        dir3 = input("Choose 'fairy','ogre','elf': ").lower()
        if dir3 in ["ogre","fairy"]:
            print("Game Over")
        elif dir3 == "elf":
            print("You Win")
        else:
            print("Invalid choice, Game Over")
    else:
        print("Invalid choice, Game Over")
else:
    print("Invalid choice, Game Over")


# 23. Haunted House Game
print("Welcome to the Haunted House")
floor1 = input("Go 'upstairs' or 'downstairs'? ").lower()

if floor1 == "downstairs":
    print("Game Over")
elif floor1 == "upstairs":
    floor2 = input("Enter room or stay outside? ").lower()
    if floor2 == "enter room":
        print("Game Over")
    elif floor2 == "stay outside":
        floor3 = input("Choose 'ghost','vampire','werewolf': ").lower()
        if floor3 in ["ghost","vampire"]:
            print("Game Over")
        elif floor3 == "werewolf":
            print("You Win")
        else:
            print("Invalid choice, Game Over")
    else:
        print("Invalid choice, Game Over")
else:
    print("Invalid choice, Game Over")
