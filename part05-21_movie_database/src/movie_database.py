# ************  Movie database  ************
# Please write a function 
# named add_movie(database: list, name: str, director: str, year: int, runtime: int), 
# which adds a new movie object into a movie database.
# The database is a list, and each movie object in the list is a dictionary. 
# The dictionary should contain the following keys.
# name
# director
# year
# runtime
# The values attached to these keys are given as arguments to the function.

# An example of its use:
# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)
# Sample output
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_directory={}
    movie_directory['name']=name
    movie_directory['director']=director
    movie_directory['year']=year
    movie_directory['runtime']=runtime
    database.append(movie_directory)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)