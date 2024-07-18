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
    show_time = input("Enter the show time (choose from list ): ").strip()

    num_adults = int(input("Enter the number of adult tickets: ").strip() or '0')
    num_seniors = int(input("Enter the number of senior tickets: ").strip() or '0')
    num_children = int(input("Enter the number of child tickets: ").strip() or '0')

    total_tickets = num_adults + num_seniors + num_children

    if total_tickets > num_seats:
        print("Not enough seats available. Try booking fewer tickets.")
        return

    available_seats = random.sample(range(1, 101), total_tickets)  # Assuming 100 seats in total
    print("Your seats:", available_seats)

    cost = (num_adults * 20) + (num_seniors * 15) + (num_children * 10)
    print(f"Total cost: RM{cost}")

    with open('bookinginfo.txt', 'a') as file:
        file.write(f"{select_movie}|{show_time}|{available_seats}|{cost}\n")

    print("Booking successful!")

def add_on():

    with open("combo.txt",'r')as file:
        for food in file:
            combo_id , combo  , price = food.split('-')
            print(f"{combo_id.strip()}-{combo.strip()}-{price}")











# Main function to run the system
def main():
    users = load_users()
    print("Welcome to the Movie Ticket Booking System!")

    while True:
        print("1. Register")
        print("2.Login")
        choice = int(input("Do you want to login or register? (1.register/2.Login): "))
        if choice ==1:
            register(users)
        elif choice ==2:
            if login(users):
                break

        else:
            print("Invalid choice. Please enter 'login' or 'register'.")

    while True:
        print("\n1. Show movie details")
        print("2. Book a movie")
        print("3. Next")
        option = input("Enter your choice(type back to exit) : ").strip().lower()

        if option == '1':
            view_movies()
        elif option == '2':
            book_movie()
        elif option == '3':
            print("Moving to next step")
            break
        else:
            print("Invalid choice. Please enter '1', '2' or '3.")

   # while True:
   #     print("\nFood and Beverages :  ")
   #     print("1.Food/snacks")
   #     print("2. NO")
   #     choice = int(input("Anything Extra (food/NO) : "))
   #
   #     if choice =='1':
   #         add_on()
   #     else:
   #         print("thank you")

    while True:
        print("\nFood and Beverages:")
        print("1. Food/snacks")
        print("2. NO")

        choice = int(input("Anything Extra (1 for food/snacks, 2 for NO): ").strip())

        if choice == 1:
            add_on()
        elif choice == 2:
            print("Thank you.")
        break  # Exit the loop if the user chooses '2'
    else:
        print("Invalid choice. Please enter '1' for food/snacks or '2' for NO.")

if __name__ == "__main__":
    main()




