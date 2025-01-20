# ******* Find movies *******
# Please write a function named find_movies(database: list, search_term: str), 
# which processes the movie database created in the previous exercise. 
# The function should formulate a new list, which contains only the movies 
# whose title includes the word searched for. Capitalisation is irrelevant here. 
# A search for ana should return a list containing both Anaconda and Management.

# An example of its use:

# database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
# {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
# {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

# my_movies = find_movies(database, "python")
# print(my_movies)
# Sample output
# [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116}, {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94}]

# Write your solution here
def find_movies(database: list, search_term: str):
    new_list=[]
    for movies in database:
        for keys, value in movies.items():
            if keys == 'name':
                value=str(value)
                value=value.lower()
                search_term=str(search_term)
                search_term=search_term.lower()
                is_there_python=value.find(search_term.lower())
                if is_there_python!=-1:
                    new_list.append(movies)
                    break
    return new_list


if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)

    database = [{'name': 'The Birds 4', 'director': 'James Hitchcock', 'year': 2003, 'runtime': 119}, 
                {'name': 'The Godfather 4', 'director': 'Antero Coppola', 'year': 2022, 'runtime': 83}, 
                {'name': 'Jaws', 'director': 'Steven Spielberg', 'year': 1975, 'runtime': 124}, 
                {'name': 'Star Wars', 'director': 'George Lucas', 'year': 1977, 'runtime': 121}, 
                {'name': 'Lost in Translation 4', 'director': 'Soena Coppola', 'year': 2032, 'runtime': 120}]
    my_movies = find_movies(database, "4")
    print(my_movies)