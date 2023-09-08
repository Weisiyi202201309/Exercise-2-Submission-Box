import sqlite3

# Read the file and copy its content to a list
with open('/Users/wsy_956559_/Desktop/软件工程专题/python/exercise 2/stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.read().splitlines()

# Establish a connection with the SQLite database
conn = sqlite3.connect('stephen_king_adaptations.db')
c = conn.cursor()

# Create a table in the database
c.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
             (movieID INTEGER PRIMARY KEY AUTOINCREMENT,
              movieName TEXT,
              movieYear INTEGER,
              imdbRating REAL)''')

# Insert data from the list into the table
for adaptation in stephen_king_adaptations_list:
    movie_info = adaptation.split(',')
    c.execute("INSERT INTO stephen_king_adaptations_table (movieName, movieYear, imdbRating) VALUES (?, ?, ?)",
              (movie_info[1], int(movie_info[2]), float(movie_info[3])))

# Commit the changes to the database
conn.commit()

# Function to search for movies in the database
def search_movies():
    while True:
        print("Options:")
        print("1. Search by movie name")
        print("2. Search by movie year")
        print("3. Search by movie rating")
        print("4. STOP")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            movie_name = input("Enter the movie name to search: ")
            c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieName=?", (movie_name,))
            result = c.fetchall()

            if result:
                print("Movie details:")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No such movie exists in our database")

        elif choice == 2:
            movie_year = int(input("Enter the movie year to search: "))
            c.execute("SELECT * FROM stephen_king_adaptations_table WHERE movieYear=?", (movie_year,))
            result = c.fetchall()

            if result:
                print("Movie details:")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies were found for that year in our database.")

        elif choice == 3:
            rating = float(input("Enter the minimum rating: "))
            c.execute("SELECT * FROM stephen_king_adaptations_table WHERE imdbRating >= ?", (rating,))
            result = c.fetchall()

            if result:
                print("Movie details:")
                for row in result:
                    print("Movie Name:", row[1])
                    print("Movie Year:", row[2])
                    print("IMDB Rating:", row[3])
            else:
                print("No movies at or above that rating were found in the database.")

        elif choice == 4:
            break

        else:
            print("Invalid choice! Please enter a valid option.")

# Call the search_movies function
search_movies()

# Close the database connection
conn.close()
