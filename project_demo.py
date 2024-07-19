import random

# Function to load users from the file
def load_users():
    users = {}

    with open("user.txt",'r') as file:
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
    try:
        with open('movies.txt', 'r') as file:
            for line in file:
                movies.append(line.strip())
    except FileNotFoundError:
        print("No movies available.")
    return movies

# Function to view movies
def view_movies():
    movies = load_movies()
    if movies:
        print("Available movies:")
        print("\tMovie - \tShow Times ")
        for movie in movies:
            movie_name , show_times = movie.split('-')
            print(f"{movie_name.strip()} -{show_times.strip()}")
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
    print("\nyou can select the movie and time From above details")

    select_movie = input(" what movie you want to watch  : ").upper()
    num_seats = int(input("Enter the number of seats you want to book: ").strip())
    num_adults = int(input("How Many adult tickets: ").strip() or '0')
    num_seniors = int(input("How many  senior tickets: ").strip() or '0')
    num_children = int(input("How  Many  child tickets: ").strip() or '0')
    #show_Time
    show_time = input("Enter the show time (choose from list ): ").strip()

    total_tickets = num_adults + num_seniors + num_children

    if total_tickets > num_seats:
        print("Not enough seats available. Try booking fewer tickets.")
        return

    available_seats = random.sample(range(1, 25), total_tickets)  # Randomly selecting seats

    cost = (num_adults * 20) + (num_seniors * 15) + (num_children * 10)
    print(f"Total cost: RM{cost}")

    with open('bookinginfo.txt', 'a') as file:
        file.write(f"{select_movie}|{show_time}|{available_seats}|{cost}\n")

    print("Booking successful!")


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
            price = price.replace('RM', '').strip()  # Remove 'RM' prefix
            snacks.append({'name': snack_name.strip(), 'price': float(price)})
    return snacks


def load_drinks():
    drinks = []
    with open('drinks.txt', 'r') as file:
        for line in file:
            drink_name, price = line.strip().split('-')
            price = price.replace('RM', '').strip()  # Remove 'RM' prefix
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
                quantity = int(input("Enter quantity: ").strip())
                order.append((combos[combo_choice - 1], quantity))
                print(f"Added {quantity} x {combos[combo_choice - 1]['name']} to your order.")
            else:
                print("Invalid choice. Try again.")
        elif choice == '2':
            display_snacks()
            snack_choice = int(input("Select a snack by number: ").strip())
            snacks = load_snacks()
            if 1 <= snack_choice <= len(snacks):
                quantity = int(input("Enter quantity: ").strip())
                order.append((snacks[snack_choice - 1], quantity))
                print(f"Added {quantity} x {snacks[snack_choice - 1]['name']} to your order.")
            else:
                print("Invalid choice. Try again.")
        elif choice == '3':
            display_drinks()
            drink_choice = int(input("Select a drink by number: ").strip())
            drinks = load_drinks()
            if 1 <= drink_choice <= len(drinks):
                quantity = int(input("Enter quantity: ").strip())
                order.append((drinks[drink_choice - 1], quantity))
                print(f"Added {quantity} x {drinks[drink_choice - 1]['name']} to your order.")
            else:
                print("Invalid choice. Try again.")
        elif choice == '4':
            print("Moving to the next step.")
            break
        else:
            print("Invalid user input.")

    return order


# Main function to integrate the add_food function into the main workflow:
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

    while True:
        print("\n1. Show movie details")
        print("2. Book a movie")
        print("3. Next")
        option = input("Enter your choice (type 'back' to exit): ").strip().lower()

        if option == '1':
            view_movies()
        elif option == '2':
            book_movie()
        elif option == '3':
            print("Food and beverages")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")

    order = add_food()

    # You would then continue with the payment process and saving the order details to 'bookinginfo.txt'


if __name__ == "__main__":
    main()




