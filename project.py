#hey wassupp
name = []
time = []
price = []
seats = []



def display():
    with open("movies.txt",'r',) as file:
        lines = file.readline()
    file.close()


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



print("helo")
# here we are doing assignment
print("-----------------------")
print("\t\t\tHiii there")
print("----------------------")



def entry() :
    print("GYM MEMBERSHITP FILE")
    print('choose the option :')
    print("1.login")
    print("2.Register")
    print("3.quit")

    option = int(input("enter what you to do  in this systen : "))

    if option == 1:
        print("hii actually i dont know how to do the coding for read the file")
    elif option == 2:
        print("hello ")
    elif option == 3:
        print("Thank you ")



display()

