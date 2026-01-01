# 1
"""
Create a Python program that prompts the user to enter their age. 
If the age is less than 18, print "You are a minor." 
If the age is between 18 and 60, print "You are an adult." 
For ages over 60, print "You are a senior citizen." 
The program should continue until the user inputs "stop."
"""
while True:
    age = input("enter age (or stop): ")
    if age.lower() == "stop":
        break
    age = int(age)
    if age < 18:
        print("you are a minor")
    elif age <= 60:
        print("you are an adult")
    else:
        print("you are a senior citizen")


# 2
"""
Write a Python program that simulates waiting for a specific vehicle, such as a "bus". 
The program should repeatedly prompt the user to input the name of a vehicle. 
If the input is not "bus", the program should print "waiting" and continue. 
Once the user inputs "bus", the program should print "finally the wait is over" and terminate the loop.
"""
while True:
    vehicle = input("enter vehicle: ")
    if vehicle.lower() == "bus":
        print("finally the wait is over")
        break
    else:
        print("waiting")


# 3
"""
Write a Python program that continuously prompts the user to input a fruit name. 
If the input is "apple," the program should print "You got it!" and stop. 
Otherwise, it should display "Try again" and continue.
"""
while True:
    fruit = input("enter fruit name: ")
    if fruit.lower() == "apple":
        print("you got it")
        break
    else:
        print("try again")


# 4
"""
Create a Python program that asks the user to guess the password "open sesame". 
Keep asking until correct. For each incorrect guess, print "Wrong password, try again." 
When the correct password is entered, print "Access granted!"
"""
while True:
    pwd = input("enter password: ")
    if pwd.lower() == "open sesame":
        print("access granted")
        break
    else:
        print("wrong password, try again")


# 5
"""
Generate a frequency table for the ratings list which is initialized below:
Ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
Start by creating an empty dictionary named content_ratings.
Loop through the ratings list. For each iteration:
If the rating is already in content_ratings then increment the frequency of that rating by 1.
Else, initialize the rating with a value of 1 inside the content_ratings dictionary.
"""
ratings = ['4+', '9+', '12+', '17+', '4+', '12+', '4+', '9+', '17+', '12+', '4+', '17+']
content_ratings = {}
i = 0
while i < len(ratings):
    r = ratings[i]
    if r in content_ratings:
        content_ratings[r] = content_ratings[r] + 1
    else:
        content_ratings[r] = 1
    i = i + 1
print(content_ratings)


# 6
"""
Write a Python program that generates a random number between 1 and 10 and prompts the user to guess the number. 
The program should provide hints such as "guess higher" or "guess lower" based on the user's input. 
Once the user guesses the correct number, the program should display the number of attempts it took to guess the correct number.
"""
import random
number = random.randint(1, 10)
tries = 0
while True:
    guess = int(input("guess number 1-10: "))
    tries = tries + 1
    if guess < number:
        print("guess higher")
    elif guess > number:
        print("guess lower")
    else:
        print("you guessed right in", tries, "tries")
        break


# 7
"""
Write a Python program that simulates a login system. 
The program should prompt the user to enter a username and password. 
If both are correct (username = "admin", password = "1234"), print "Login successful" and exit. 
If either is incorrect, print "Invalid credentials, try again." 
Allow the user up to 3 attempts before locking them out with the message "Too many failed attempts."
"""
right_user = "admin"
right_pass = "1234"
count = 0
while count < 3:
    u = input("enter username: ")
    p = input("enter password: ")
    count = count + 1
    if u == right_user and p == right_pass:
        print("login successful")
        break
    else:
        if count == 3:
            print("too many failed attempts")
        else:
            print("invalid, try again")


# 8
"""
Write a Python program that simulates a basic arithmetic quiz. 
Generate two random numbers between 1 and 30 and ask the user to provide the result of their multiplication. 
If the answer is correct, print "Correct!" and generate a new question. 
If the answer is wrong, print "Incorrect, try again." 
Allow the user to stop the quiz when the user enters "exit".
"""
import random
while True:
    x = random.randint(1, 30)
    y = random.randint(1, 30)
    ans = input(f"{x} * {y} = ")
    if ans.lower() == "exit":
        print("quiz ended")
        break
    if int(ans) == x * y:
        print("correct")
    else:
        print("incorrect, try again")


# 9
"""
Write a Python program that prompts the user to enter a number. 
The program should determine whether the number is prime or not. 
If the number is prime, print "The number is prime." Otherwise, print "The number is not prime." 
Continue prompting the user until they enter "exit."
"""
while True:
    n = input("enter number (exit to stop): ")
    if n.lower() == "exit":
        print("program ended")
        break
    n = int(n)
    if n < 2:
        print("not prime")
    else:
        for i in range(2, n):
            if n % i == 0:
                print("not prime")
                break
        else:
            print("prime")


# 10
"""
Write a Python program that asks the user to guess a pre-defined secret word (e.g., "python"). 
Provide feedback like "Incorrect, try again" if the guess is wrong. 
When the user guesses correctly, print "Congratulations, you guessed the word!" 
Allow the user to exit the program by typing "quit."
"""
secret = "python"
tries = 0
while True:
    guess = input("guess the word: ")
    tries = tries + 1
    if guess.lower() == "quit":
        print("program ended")
        break
    if guess.lower() == secret:
        print("you guessed in", tries, "attempts")
        break
    else:
        print("wrong, try again")


# 11
"""
Write a Python program that prompts the user to repeatedly enter a name. 
If the user enters the phrase "good luck," the program keeps track of how many times the phrase has been entered. 
When the phrase has been entered three times, the program should display a message stating "You typed good luck three times." 
For each entry of "good luck" before the third occurrence, display the message "You typed the same word [count] times." 
Continue this process until the phrase has been entered three times.
"""
count = 0
while True:
    word = input("enter something: ")
    if word.lower() == "good luck":
        count = count + 1
        if count == 3:
            print("you typed good luck three times")
            break
        else:
            print("you typed the same word", count, "times")


# 12
"""
Write a Python program that simulates a basic elevator system. 
The program should keep track of the elevator's current position and allow a user to travel to different floors until they choose to exit. 
Starting State: The elevator should start on floor 1. 
Continuous Loop: Use a while loop to repeatedly ask the user for a destination floor. 
Input Handling: If the user enters 0, the program should print a goodbye message and terminate. 
If the user enters something that isn't a number, handle the error gracefully so the program doesn't crash. 
Logic: If the target floor is higher than the current floor, print "Going up" message. 
If the target floor is lower than the current floor, print "Going down" message. 
If the user is already on the requested floor, inform them of that. 
State Update: After moving, update the current floor to the target floor.
"""
current = 1
while True:
    floor = input("enter floor (0 to exit): ")
    if not floor.isdigit():
        print("invalid input")
        continue
    floor = int(floor)
    if floor == 0:
        print("goodbye")
        break
    if floor > current:
        print("going up")
    elif floor < current:
        print("going down")
    else:
        print("you are already here")
    current = floor
