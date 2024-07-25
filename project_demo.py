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
    print("\nRegistration successful. You can now login.\n")
    return


# Function to login a user
def login(users):
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    if username in users and users[username]['password'] == password:
        print("\nLogin successful.\n")
        return username
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
        print("\nAvailable movies:")
        print("\nIndex - Movie - Show Times")
        for index, movie in enumerate(movies, start=1):
            movie_name, show_times = movie.split('-')
            print(f"{index}. {movie_name.strip()} - {show_times.strip()}")
    else:
        print("No movies available.")


# Function to generate available seats in a 6x8 grid
def generate_seats(rows=8, cols=10):
    seats = [['□' for _ in range(cols)] for _ in range(rows)]
    return seats


# Function to display seats
def display_seats(seats):
    print("Seats (□: Available, ■: Booked):")
    for row in seats:
        print(' '.join(row))
    print()


# Function to book seats
def book_seats(seats, num_seats):
    available_seats = [(r, c) for r in range(len(seats)) for c in range(len(seats[0])) if seats[r][c] == '□']
    if len(available_seats) < num_seats:
        print("Not enough seats available.")
        return False

    selected_seats = available_seats[:num_seats]
    for r, c in selected_seats:
        seats[r][c] = '■'
    return selected_seats


# Function to book a movie
def book_movie(username):
    movies = load_movies()
    view_movies()
    movie_index = int(input("\nEnter the index of the movie you want to watch: ").strip())

    if movie_index < 1 or movie_index > len(movies):
        print("Invalid movie selection.")
        return 0, [], 0, 0, 0, ""

    selected_movie = movies[movie_index - 1]
    movie_name, show_times = selected_movie.split('-')

    num_seats = int(input("\nEnter the number of seats you want to book: ").strip())
    num_adults = int(input("\nHow many adult tickets RM 20 (enter 0 if no adult): ").strip() or '0')
    num_seniors = int(input("How many senior tickets RM 15 (enter 0 if no senior): ").strip() or '0')
    num_children = int(input("How many child tickets RM 10 (enter 0 if no child): ").strip() or '0')

    total_tickets = num_adults + num_seniors + num_children
    if total_tickets > num_seats:
        print("Total tickets exceed the number of seats booked.")
        return 0, [], 0, 0, 0, ""

    seats = generate_seats()
    display_seats(seats)
    booked_seats = book_seats(seats, total_tickets)
    if not booked_seats:
        return 0, [], 0, 0, 0, ""

    show_time = input("\nEnter the show time (choose from list): ").strip()

    cost = (num_adults * 20) + (num_seniors * 15) + (num_children * 10)  # calculating the price for movie
    print(" ")
    print(f"Total cost: RM{cost:.2f}")

    with open('bookinginfo.txt', 'a') as file:  # saving the booking to booking info text file
        file.write(f"{username}|{movie_name}|{show_time}|{booked_seats}|{cost}\n")

    print("Booking successful!")
    display_seats(seats)
    # returning variables
    return cost, booked_seats, num_children, num_seniors, num_adults, movie_name.strip()


# food and beverage part :
def load_combos():
    combos = []
    with open('combo.txt', 'r') as file:
        for line in file:
            combo_id, combo_name, price = line.strip().split('-')
            price = price.replace('RM', '').strip()
            combos.append({'id': combo_id.strip(), 'name': combo_name.strip(), 'price': float(price)})
    return combos


def load_snacks():
    snacks = []
    with open('snaks.txt', 'r') as file:
        for line in file:
            snack_name, price = line.strip().split('-')
            price = price.strip().replace('RM', '').strip()
            snacks.append({'name': snack_name.strip(), 'price': float(price)})
    return snacks


def load_drinks():
    drinks = []
    with open('drinks.txt', 'r') as file:
        for line in file:
            drink_name, price = line.strip().split('-')
            price = price.strip().replace('RM', '').strip()
            drinks.append({'name': drink_name.strip(), 'price': float(price)})
    return drinks


# display 3 food and beverage files

def display_combos():
    combos = load_combos()
    print("\nAvailable Combos:")
    for combo in combos:
        print(f"{combo['id']} - {combo['name']} - RM {combo['price']}")


def display_snacks():
    snacks = load_snacks()
    print("\nAvailable Snacks:")
    for i in range(len(snacks)):
        snack = snacks[i]
        print(f"{i + 1} - {snack['name']} - RM {snack['price']}")


def display_drinks():
    drinks = load_drinks()
    print("\nAvailable Drinks:")
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
            combo_choice = int(input("\nSelect a combo by number: ").strip())
            combos = load_combos()
            if 1 <= combo_choice <= len(combos):
                order.append((combos[combo_choice - 1], 1))  # Assuming quantity of 1 for combos
                print(f"Added {combos[combo_choice - 1]['name']} to your order.")
            else:
                print("Invalid selection")

        elif choice == '2':
            display_snacks()
            snack_choice = int(input("\nSelect snacks by number: ").strip())
            snacks = load_snacks()
            if 1 <= snack_choice <= len(snacks):
                qty = int(input("Enter the quantity: "))
                order.append((snacks[snack_choice - 1], qty))
                print(f"Added {qty} x {snacks[snack_choice - 1]['name']} to your order.")
            else:
                print("Invalid selection")

        elif choice == '3':
            display_drinks()
            drink_choice = int(input("\nSelect drinks by number: ").strip())
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


# Calculate the total cost of the order
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
        amount = float(input("Enter the paymnet amount(only accept 20,50,100 notes): ").strip())
        total_payment += amount

        if total_payment < total_amount:
            print(f"insufficient amount . you need to enter RM {total_amount - total_payment:.2f} more")
        else:
            break

    change = total_payment - total_amount
    print(f"Payment successful. Your change is RM {change:.2f}.")

    return total_amount, total_payment, change


# Printing receipt
def print_receipt(movie_cost, food_order, total_amount, payment_amount, change, available_seats, num_children,
                  num_seniors, num_adults, username, order, movie_name):
    # Determine the width of the receipt
    receipt_width = 60

    # Define a function to center-align text
    def center_text(text, width):
        return text.center(width)

    # Print the receipt
    print("\n" + center_text("---------------------------------------------------------", receipt_width))
    print(center_text("Marwan Movie Ticket Booking System", receipt_width))
    print(center_text("---------------------------------------------------------", receipt_width))
    print(center_text(f"Date: {current_date}  Time: {current_time}", receipt_width))
    print(center_text("---------------------------------------------------------", receipt_width))
    print(f"{'ITEMS':<30} {'QTY':<10} {'COST':>7}")
    print(center_text("---------------------------------------------------------", receipt_width))
    if movie_name:
        print(center_text(f"Movie:  {movie_name}", receipt_width))
        if num_adults > 0:
            print(f"{'Adult Tickets':<30} {num_adults:<10} RM {num_adults * 20:.2f}")
        if num_seniors > 0:
            print(f"{'Senior Tickets':<30} {num_seniors:<10} RM {num_seniors * 15:.2f}")
        if num_children > 0:
            print(f"{'Child Tickets':<30} {num_children:<10} RM {num_children * 10:.2f}")
    print(f"{'Total Movie Cost':<30} {' ':<10} RM {movie_cost:.2f}")
    print(center_text("---------------------------------------------------------", receipt_width))
    print(center_text("Selected seats:", receipt_width))

    # Print the seats horizontally
    seats_per_line = 8
    formatted_seats = [f"R{r + 1}-C{c + 1}" for r, c in available_seats]
    for i in range(0, len(formatted_seats), seats_per_line):
        print(center_text("  ".join(formatted_seats[i:i + seats_per_line]), receipt_width))

    print(center_text("---------------------------------------------------------", receipt_width))
    print("Food and Beverages:")
    for item, qty in food_order:
        print(f"{item['name']:<30} {qty:<10} RM {item['price'] * qty:.2f}")
    print(center_text("----------------------------------------------------------", receipt_width))
    print(f"{'Total Food & Beverage Cost':<30} {' ':<10} RM {calculate_total(food_order):.2f}")
    print(center_text("----------------------------------------------------------", receipt_width))
    print(f"{'Total Cost':<30} {' ':<10} RM {total_amount:.2f}")
    print(f"{'Amount Paid':<30} {' ':<10} RM {payment_amount:.2f}")
    print(center_text("----------------------------------------------------------", receipt_width))
    print(f"{'Change':<30} {' ':<10} RM {change:.2f}")
    print('')
    print(center_text(f"Thank you {username} for booking your movie with us!", receipt_width))
    print(center_text("have a great day!", receipt_width))
    print('')

    view = input("Do you want to see your booking information (y/n): ").upper()

    if view == 'Y':
        with open("bookinginfo.txt", 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                print("\n------ Your Booking Info ------")
                print(last_line)
                print("------------------------------")
                print("Thank you!\n")
            else:
                print("No booking information found.")
    else:
        print("Have a great day!")


# Main function to integrate the add_food function into the main workflow
def main():
    # Load user from text file
    users = load_users()
    print("Welcome to the Movie Ticket Booking System!")
    username = []

    while True:
        print("1. Register")
        print("2. Login\n")

        choice = int(input("Do you want to login or register? (1. Register / 2. Login): "))
        if choice == 1:
            register(users)
        elif choice == 2:
            username = login(users)
            if username:
                break  # Login user and break the loop if successful
        else:
            print("Invalid choice. Please enter '1' for Register or '2' for Login.")

    movie_cost = 0
    available_seats = []  # Initialize available seats
    num_children = num_seniors = num_adults = 0  # Initialize ticket counts
    movie_name = ""
    print("-------------------------------------")
    print("Book your movie here")
    print("------------------------------------")
    while True:
        print("\n1. Show movie details")
        print("2. Book a movie")
        print("3. Next")
        option = input("\nEnter your choice (type 'back' to exit): ").strip().lower()

        if option == '1':
            view_movies()  # show movie details
        elif option == '2':
            movie_cost, available_seats, num_children, num_seniors, num_adults, movie_name = book_movie(
                username)  # Book a movie and get details
        elif option == '3':
            food_order = add_food()  # adding food and beverages
            total_amount, payment_amount, change = payment_process(movie_cost, food_order)  # for payment process
            print_receipt(movie_cost, food_order, total_amount, payment_amount, change, available_seats, num_children,
                          num_seniors, num_adults, username, food_order, movie_name)  # print reciept
            break  # Exit the loop after payment and receipt
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.")  # invalid choice


if __name__ == "__main__":
    main()
