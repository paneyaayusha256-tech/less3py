# 1. You have a list containing mixed data types represented as strings. Write a Python
# program using a filter() and lambda function to keep only the alphabetic items
# (letters only) and remove any numeric strings from the list."
# items = ['sql', '123', 'python']
items = ['sql', '123', 'python']
alpha_items = list(filter(lambda x: x.isalpha(), items))
print("1.", alpha_items)


# 2. You are managing an e-commerce inventory database. Given a list of product
# dictionaries, write a Python program using a filter() and lambda function to
# extract and display only the products that are currently in stock (instock: True)
# products = [
#  {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
#  {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock':
# False}
# ]
products = [
    {'id': 1, 'name': 'laptop', 'category': 'electronics', 'price': 1200, 'instock': True},
    {'id': 2, 'name': 'smartphone', 'category': 'electronics', 'price': 800, 'instock': False}
]

instock_products = list(filter(lambda p: p['instock'], products))
print(instock_products)



# 3. Given a list of course dictionaries, write a Python program using a lambda function
# to filter and display only those courses that belong to the 'history' genre.
# course = [ {'title': 'Ancient Civilizations', 'genre': 'history'}, {'title': 'Corporate
# Finance', 'genre': 'commerce'}, {'title': 'Modern World History', 'genre': 'history'} ]
courses = [
    {'title': 'Ancient Civilizations', 'genre': 'history'},
    {'title': 'Corporate Finance', 'genre': 'commerce'},
    {'title': 'Modern World History', 'genre': 'history'}
]

history_courses = list(filter(lambda c: c['genre'] == 'history', courses))
print(history_courses)



# 4. You have a list of blacklisted domains. Write a Python program using a lambda
# function to filter a list of emails and return only the ones that are considered spam
# those that match any domain in the blacklist.
# emails = ['ram.sharma@gmail.com', 'spam@hooya.com', 'virus@malware.net',
# ‘shyam.kumar@workcorp.com’]
# blacklist = ('@hooya.com', '@malware.net')
emails = [
    'ram.sharma@gmail.com',
    'spam@hooya.com',
    'virus@malware.net',
    'shyam.kumar@workcorp.com'
]

blacklist = ('@hooya.com', '@malware.net')

spam_emails = list(filter(lambda e: e.endswith(blacklist), emails))
print(spam_emails)



# 5. Applying a 20% discount to all items in a shopping cart:
# price = [100, 50, 200, 75] implement using lambda function
price = [100, 50, 200, 75]

discounted_price = list(map(lambda p: p * 0.8, price))
print(discounted_price)



# 6. Create a function, skip_two that takes a list as input, and returns a list that: Starts
# with the second element of the input. While skipping every two elements. Does
# not keep any element whose index is greater than 11
def skip_two(lst):
    return [lst[i] for i in range(1, min(len(lst), 12), 3)]

print(skip_two([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))



# 7. Create a function, remove_at_idx, with the following features:
#  Takes a list as its first argument.
#  Takes a positive index as its second argument.
#  Removes the element at the given index and decreases the index of all
# subsequent elements by one.
#  Returns a new list.
def remove_at_idx(lst, idx):
    if idx < 0 or idx >= len(lst):
        return lst
    return lst[:idx] + lst[idx+1:]

print(remove_at_idx([10, 20, 30, 40, 50], 2))



# 8. You are developing a data-cleaning tool for a messaging application. The
# application collects user input which may contain special characters like @, #, !,
# %, etc., which could be problematic during processing or searching. To sanitize
# this input, your task is to replace all special characters with a # symbol, while
# keeping letters and digits unchanged. Write a Python program that:
#  Accepts a string input from the user.
#  Replaces all non-alphanumeric characters (special characters) with #.
#  Prints the cleaned string
text = input("Enter a string: ")
cleaned_text = ''.join(ch if ch.isalnum() else '#' for ch in text)
print(cleaned_text)


# 9. Write a Python program that implements a simple user registration and login
# system with the following requirements:
# Create a global dictionary called users_db to store user information. Implement a
# register_user(username, password, email) function that:
#  Checks if the username already exists and returns ‘Username
# already exists’ if it does
#  Stores the user's password and email in the database
#  Returns a success message in the format: Registration successful for
# {username}
# Implement a login_user(username, password) function that:
#  Returns ‘User not found’ if the username doesn't exist
#  Returns ‘Incorrect password’ if the password is wrong
#  Returns ‘Welcome back, {username}’ if login is successful
#  Test the program by registering three users:
#  ram with password ‘ram123’ and email ‘ram@email.com’
#  shyam with password ‘shyam456’ and email ‘shyam@email.com’
#  hari with password ‘hari231’ and email ‘hari@email.com’
users_db = {}

def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username] = {'password': password, 'email': email}
    return f"Registration successful for {username}"

def login_user(username, password):
    if username not in users_db:
        return "User not found"
    if users_db[username]['password'] != password:
        return "Incorrect password"
    return f"Welcome back, {username}"


print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))

print(login_user("ram", "ram123"))



# 10. Develop a Python program for managing product inventory using a dictionary
# stored in a list.
# 1. Initialize inventory as a list of dictionaries: [{'name': 'Laptop', 'price': 50000,
# 'quantity': 5}]
# 2. Menu options:
#  Add new product (name, price, quantity)
#  View all products in a formatted table
#  Update product details (by product name)
#  Delete a product
#  Calculate total inventory value
#  Exit
#  3. Ensure price and quantity are positive numbers
#  4. Prevent duplicate product names
#  5. Show confirmation messages for all operations
inventory = [{'name': 'Laptop', 'price': 50000, 'quantity': 5}]

def add_product():
    name = input("Product name: ")
    for p in inventory:
        if p['name'].lower() == name.lower():
            print("Product already exists")
            return

    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    if price > 0 and quantity > 0:
        inventory.append({'name': name, 'price': price, 'quantity': quantity})
        print("Product added successfully")

def view_products():
    print("\nName\tPrice\tQuantity")
    for p in inventory:
        print(f"{p['name']}\t{p['price']}\t{p['quantity']}")

def update_product():
    name = input("Enter product name to update: ")
    for p in inventory:
        if p['name'].lower() == name.lower():
            p['price'] = float(input("New price: "))
            p['quantity'] = int(input("New quantity: "))
            print("Product updated")
            return
    print("Product not found")

def delete_product():
    name = input("Enter product name to delete: ")
    for p in inventory:
        if p['name'].lower() == name.lower():
            inventory.remove(p)
            print("Product deleted")
            return
    print("Product not found")

def total_value():
    total = sum(p['price'] * p['quantity'] for p in inventory)
    print("Total inventory value:", total)

while True:
    print("\n1.Add 2.View 3.Update 4.Delete 5.Total Value 6.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_product()
    elif choice == '2':
        view_products()
    elif choice == '3':
        update_product()
    elif choice == '4':
        delete_product()
    elif choice == '5':
        total_value()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice")



# 11. Build a contact management system using nested data structures.
# 1. Initialize contacts as: [{'name': ’Ram kc’, 'phone': '9801234567', 'email':
# 'ram@email.com'}]
# 2. Menu features:
#  Add contact (name, phone, email)
#  Display all contacts
#  Search contact by name
#  Update contact information
#  Delete contact
#  Sort contacts alphabetically
#  Exit
# 3. Validate phone number format (10 digits)
# 4. Validate email format (contains @ and.)
# 5. Prevent duplicate contacts
contacts = [{'name': 'Ram kc', 'phone': '9801234567', 'email': 'ram@email.com'}]

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def valid_email(email):
    return '@' in email and '.' in email

def add_contact():
    name = input("Name: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact already exists")
            return

    phone = input("Phone: ")
    email = input("Email: ")

    if valid_phone(phone) and valid_email(email):
        contacts.append({'name': name, 'phone': phone, 'email': email})
        print("Contact added")
    else:
        print("Invalid phone or email")

def display_contacts():
    for c in contacts:
        print(c)

def search_contact():
    name = input("Search name: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            print(c)
            return
    print("Contact not found")

def update_contact():
    name = input("Name to update: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            c['phone'] = input("New phone: ")
            c['email'] = input("New email: ")
            print("Contact updated")
            return
    print("Contact not found")

def delete_contact():
    name = input("Name to delete: ")
    for c in contacts:
        if c['name'].lower() == name.lower():
            contacts.remove(c)
            print("Contact deleted")
            return
    print("Contact not found")

def sort_contacts():
    contacts.sort(key=lambda x: x['name'])
    print("Contacts sorted")

while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Sort 7.Exit")
    choice = input("Choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        display_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        sort_contacts()
    elif choice == '7':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
