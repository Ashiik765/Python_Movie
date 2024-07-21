import time
import pickle
import random
from datetime import date, datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date.today().strftime("%m/%d/%Y")

# Function to load users from the file
def load_users():
    users = {}
    with open("user.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        username, password, email = line.strip().split("|")
        users[username] = {'password': password, 'email': email}

    return users

# Function to save a new user to the file
def save_user(username, password, email):
    with open('user.txt', 'a') as file:
        file.write(f"{username}|{password}|{email}\n")

# Function to register a new user
def register(users):
    while True:
        username = input("Enter a username: ").strip()
        if username in users:
            print("Username already exists. Try a different one.")
        else:
            break

    password = input("Enter a password: ").strip()

    while True:
        email = input("Enter your Gmail address: ").strip()
        if email.endswith('@gmail.com'):
            break
        else:
            print("Invalid email. Please enter a valid Gmail address (ending with @gmail.com).")

    save_user(username, password, email)
    users[username] = {'password': password, 'email': email}
    print("Registration successful. You can now login.")

# Function to login a user
def login(users):
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users and users[username]['password'] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password. Try again.")
        return False

# Function to load movies from the file
def load_movies():
    movies = []
    with open("movies.txt", 'r') as file:
        for line in file:
            movies.append(line.strip())
    return movies

# Function to view movies
def view_movies():
    movies = load_movies()
    if movies:
        print("Available movies:")
        print("\tMovie - \tShow Times ")
        for movie in movies:
            movie_name, show_times = movie.split('-')
            print(f"{movie_name.strip()} - {show_times.strip()}")
    else:
        print("No movies available.")

# Function to select a movie
def select_movie():
    movies = load_movies()
    if not movies:
        print("No movies available.")
        return None
    print("Available movies:")
    for movie in movies:
        print(movie.split('-')[0].strip())  # Display only movie names

# Function to book a movie
def book_movie():
    view_movies()
    movie_name = input("What movie do you want to watch: ").strip().title()
    num_seats = int(input("Enter the number of seats you want to book: ").strip())
    num_adults = int(input("How many adult tickets (enter 0 if no adult): ").strip() or '0')
    num_seniors = int(input("How many senior tickets (enter 0 if no senior): ").strip() or '0')
    num_children = int(input("How many child tickets (enter 0 if no child): ").strip() or '0')
    show_time = input("Enter the show time (choose from list): ").strip()

    total_tickets = num_adults + num_seniors + num_children

    if total_tickets > num_seats:
        print("Not enough seats available. Try booking fewer tickets.")
        return 0

    available_seats = random.sample(range(1, 25), total_tickets)  # Randomly selecting seats

    cost = (num_adults * 20) + (num_seniors * 15) + (num_children * 10)
    print(" ")
    print(f"Total cost: RM{cost:>15}")

    with open('bookinginfo.txt', 'a') as file:
        file.write(f"{movie_name}|{show_time}|{available_seats}|{cost}\n")

    print("Booking successful!")
    return cost

def load_combos():
    combos = []
    with open('combo.txt', 'r') as file:
        for line in file:
            combo_id, combo_name, price = line.strip().split('-')
            price = price.replace('RM', '').strip()  # Remove 'RM' prefix
            combos.append({'id': combo_id.strip(), 'name': combo_name.strip(), 'price': float(price)})
    return combos

def load_snacks():
    snacks = []
    with open('snaks.txt', 'r') as file:
        for line in file:
            snack_name, price = line.strip().split('-')
            price = price.strip().replace('RM', '').strip()  # Remove 'RM' prefix
            snacks.append({'name': snack_name.strip(), 'price': float(price)})
    return snacks

def load_drinks():
    drinks = []
    with open('drinks.txt', 'r') as file:
        for line in file:
            drink_name, price = line.strip().split('-')
            price = price.strip().replace('RM', '').strip()  # Remove 'RM' prefix
            drinks.append({'name': drink_name.strip(), 'price': float(price)})
    return drinks

def display_combos():
    combos = load_combos()
    print("Available Combos:")
    for combo in combos:
        print(f"{combo['id']} - {combo['name']} - RM {combo['price']}")

def display_snacks():
    snacks = load_snacks()
    print("Available Snacks:")
    for i in range(len(snacks)):
        snack = snacks[i]
        print(f"{i + 1} - {snack['name']} - RM {snack['price']}")

def display_drinks():
    drinks = load_drinks()
    print("Available Drinks:")
    for i in range(len(drinks)):
        drink = drinks[i]
        print(f"{i + 1} - {drink['name']} - RM {drink['price']}")

def add_food():
    order = []

    while True:
        print("\nFood and Beverages:")
        print("1. Combo")
        print("2. Snacks")
        print("3. Drinks")
        print("4. Next (Proceed to payment)")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            display_combos()
            combo_choice = int(input("Select a combo by number: ").strip())
            combos = load_combos()
            if 1 <= combo_choice <= len(combos):
                order.append((combos[combo_choice - 1], 1))  # Assuming quantity of 1 for combos
                print(f"Added {combos[combo_choice - 1]['name']} to your order.")
            else:
                print("Invalid selection")

        elif choice == '2':
            display_snacks()
            snack_choice = int(input("Select snacks by number: ").strip())
            snacks = load_snacks()
            if 1 <= snack_choice <= len(snacks):
                qty = int(input("Enter the quantity: "))
                order.append((snacks[snack_choice - 1], qty))
                print(f"Added {qty} x {snacks[snack_choice - 1]['name']} to your order.")
            else:
                print("Invalid selection")

        elif choice == '3':
            display_drinks()
            drink_choice = int(input("Select drinks by number: ").strip())
            drinks = load_drinks()
            if 1 <= drink_choice <= len(drinks):
                qty = int(input("Enter the quantity: "))
                order.append((drinks[drink_choice - 1], qty))
                print(f"Added {qty} x {drinks[drink_choice - 1]['name']} to your order.")
            else:
                print("Invalid selection")

        elif choice == '4':
            break  # Exit the loop to proceed to payment
        else:
            print("Invalid choice.")

    return order

# Calculating the payment
def calculate_total(order):
    total = 0
    for item, quantity in order:
        total += item['price'] * quantity
    return total

def payment_process(movie_cost, food_order):
    if movie_cost is None:
        movie_cost = 0

    food_total = calculate_total(food_order)
    total_amount = food_total + movie_cost

    print('')
    print("Calculating the Total:")
    print(f"Amount for movie cost: RM {movie_cost:.2f}")
    print(f"Amount for food and beverage cost: RM {food_total:.2f}")
    print(f"Total Cost: RM {total_amount:.2f}")

    print('')

    total_payment = 0

    while total_payment < total_amount:
        amount = float(input("Enter the paymnet amount : ").strip())
        total_payment += amount

        if total_payment <total_amount:
            print(f"insufficient amount . you need to enter RM {total_amount - total_payment:.2f} more")
        else:
            break

    change = total_payment - total_amount
    print(f"Payment successful. Your change is RM {change:.2f}.")

    return total_amount, total_payment, change

def print_receipt(movie_cost, food_order, total_amount, payment_amount, change):
    print("---------------------------------------------------------")
    print("\t\t\tMarwan Movie Ticket Booking System")
    print("---------------------------------------------------------")
    print(f"Date: {current_date:<15} Time: {current_time:<15}")
    print('---------------------------------------------------------')
    print(f"ITEMS                         {'COST':>10}")
    print(f"Movie cost                   : RM {movie_cost:>5.2f}")
    print(f"Food and Beverages Cost      : RM {calculate_total(food_order):<15.2f}")
    print("----------------------------------------------------------")
    print(f"Total Cost                   : RM {total_amount:<15.2f}")
    print(f"Amount Paid                  : RM {payment_amount:<15.2f}")
    print("----------------------------------------------------------")
    print(f"Change                       : RM {change:<15.2f}")
    print("\t\t\tThank From Marwan booking System ")
    print("\t\t\tave a great day!")
    print('')

# Main function to integrate the add_food function into the main workflow
def main():
    users = load_users()
    print("Welcome to the Movie Ticket Booking System!")

    while True:
        print("1. Register")
        print("2. Login")
        choice = int(input("Do you want to login or register? (1. Register / 2. Login): "))
        if choice == 1:
            register(users)
        elif choice == 2:
            if login(users):
                break
        else:
            print("Invalid choice. Please enter '1' for Register or '2' for Login.")

    movie_cost = 0
    print("-------------------------------------")
    print("\nBook your movie here")
    print("------------------------------------")
    while True:
        print("\n1. Show movie details")
        print("2. Book a movie")
        print("3. Next")
        option = input("Enter your choice (type 'back' to exit): ").strip().lower()

        if option == '1':
            view_movies()
        elif option == '2':
            movie_cost = book_movie()
        elif option == '3':
            food_order = add_food()
            total_amount, payment_amount, change = payment_process(movie_cost, food_order)
            print_receipt(movie_cost, food_order, total_amount, payment_amount, change)
            break  # Exit the loop after payment and receipt
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

if __name__ == "__main__":
    main()

