import sqlite3

def get_movie_by_name(title):
    with sqlite3.connect('netflix.db') as connection:       #connect to database
        cursor = connection.cursor()        #start cursor to get data from the database
        cursor.execute(
            f"""SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{title}%'
                ORDER BY release_year DESC"""
        )       #perform the SQL query - can be splitted to two operations query = "" + cursor.execute(query)

        data = cursor.fetchone() #get the result of the query normally as a list of tuples (fetchall список кортежей)

        film = {"title": data[0],
		    "country": data[1],
		    "release_year": data[2],
		    "genre": data[3],
		    "description": data[4]}

        return film
'''This function returns the data about the movie in json format by getting the name of the movie'''

def get_movie_by_years(year_start,year_end):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, release_year
            FROM netflix
            WHERE release_year BETWEEN {year_start} AND {year_end}
            LIMIT 100         
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "release_year": i[1]}
            film_list.append(film)
        return film_list
'''This function takes two arguments - from_to years, selects 100 movies which comply with years, creates the list of dictionaries title+release_year'''


def get_movies_for_children():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
           f"""SELECT title, rating, description 
           FROM netflix
           WHERE rating='G'
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title":i[0], "rating":i[1], "description":i[2]}
            film_list.append(film)
        return film_list
'''This function returns the list of dictionaries with all the movies marked as movies for children'''


def get_movies_for_family():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
           f"""SELECT title, rating, description 
           FROM netflix
           WHERE rating='G' OR rating='PG' OR rating='PG-13' 
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title":i[0], "rating":i[1], "description":i[2]}
            film_list.append(film)
        return film_list
'''This function returns the list of dictionaries with all the movies marked as movies for family'''


def get_movies_for_adults():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
           f"""SELECT title, rating, description 
           FROM netflix
           WHERE rating='R' OR rating='NC-17'
           LIMIT 100
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title":i[0], "rating":i[1], "description":i[2]}
            film_list.append(film)
        return film_list
'''This function returns the list of dictionaries with all the movies marked as movies for adults'''


def get_movie_by_genre(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
            FROM netflix
            WHERE listed_in LIKE '%{genre}%'
            ORDER BY release_year DESC 
            LIMIT 10
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title": i[0], "description": i[1]}
            film_list.append(film)

        return film_list
'''This function performs the SQL search by genre and returns the list of movies with description'''


def get_movie_by_cast(actor_1, actor_2):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT COUNT(`cast`), `cast`
            FROM netflix
            WHERE `cast` LIKE '%{actor_1}%' AND `cast` LIKE '%{actor_2}%'
            ORDER BY `cast`
            LIMIT 10
            """)
        return cursor.fetchall()


def find_movie(type, release_year, genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"""SELECT title, description
            FROM netflix
            WHERE type LIKE '%{type}%' AND release_year = {release_year} AND listed_in LIKE '%{genre}%'
            LIMIT 10
        """)

        data = cursor.fetchall()
        film_list = []
        for i in data:
            film = {"title":i[0], "description":i[1]}
            film_list.append(film)

        return film_list

