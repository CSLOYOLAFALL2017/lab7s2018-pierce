#proffesor herve francheschi
#name Nicholas Pierce-Ptak
#lab 7
#date 3/22/18
#cs 151
# Functions's purpose: read in a file name from the user and return it once they give one that exists
# Parameters: None
# Return: file name

def file_val():
    validFileName = True
    while validFileName:
        try:
            filename = input("Enter the name of the file to be read from: ")
            file_object = open(filename, "r")
            validFileName = False
        except FileNotFoundError:
            print("The file does not exist")
            print("Thank you.", filename, "is valid")
    return filename

#filename = file_val()


# Function's purpose: Process the file
# Parameters: file name of file to read from
# Return: The maximum profit

def process_file(filename):
    filename = open ("movies.csv","r")
    max = 0
    max_movie = ""
    max_date = ""
    for line in filename:
        date,movie_name,budget,gross = line.split(",")
        profit = float(gross) - float(budget)
        if max < profit:
            max = profit
            max_movie = movie_name
            max_date = date
        else:
            continue

    max_profit_movie = "The movie with the most profit was: " + str(max_movie)+ ", with a profit of " + str(max) + " and it was released " + str(max_date) + "."
    return max_profit_movie


# Function's purpose: Process the file
# Parameters: file name of file to read from, file name of file to write to
# Return: None

def file_out(filename_out):
    filename = open("movies.csv", "r")
    filefile = open(filename_out, "a")
    for line in filename:
        date, movie_name, budget, gross = line.split(",")
        profit = float(gross) - float(budget)
        profit=str(profit)
        profited = date,movie_name,profit
        profited =str(profited)
        filefile.write(profited)

        # THis ALSO HAS THE EC IN IT
        # EC:extra credit: outputs a list of movie with starting letter given by user
        # functions purpose: ^
        # functions inputs: none
        # return: list printed
def ec():
    choice = input("Would you like to receive a list of all the movies starting with a certain letter?(yes or no):")
    choice = choice.strip().lower()
    if choice == "yes":
        filename = open("movies.csv", "r")
        start_let = input("What starting letter of movies would you like to find?(a, b, c, etc..): ")
        start_let = start_let.strip().upper()
        for line in filename:
            date, movie_name, budget, gross = line.split(",")
            if movie_name[0] == start_let:
                print(movie_name)
            else:
                continue
        print("There's your list of all the movies starting with the letter "+start_let+", have a nice day, goodbye. :)")
    else:
        print("Understandable, have a nice day, goodbye.")
        exit()




# Function's purpose: main
# Parameters: None
# Return: None

#THis ALSO HAS THE EC IN IT
#EC:extra credit: outputs a list of movie with starting letter given by user

def main():



    filename = file_val()
    max_profit_movie = process_file(filename)
    print(max_profit_movie)

    filename_out = input("what would you like the name of the new profit file to be?: ")
    file_out(filename_out)

    ec()

main()

