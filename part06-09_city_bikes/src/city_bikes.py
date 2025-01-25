# NB: Some exercises have multiple parts, and you can receive points for the different parts 
# separately. You can submit a partially completed exercise by choosing 'Submit Solution' from 
# the menu next to the button for executing tests .

# In this exercise we will write some functions for working on a file containing location data 
# from the stations for city bikes in Helsinki.

# Each file will follow this format:

# Longitude;Latitude;FID;name;total_slot;operative;id
# 24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001
# 24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002
# 24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003
# Each station has a single line in the file. The line contains the coordinates, name, and 
# other identifying information for the station.

# Distance between stations
# First, write a function named get_station_data(filename: str). This function should read 
# the names and locations of all the stations in the file, and return them in a dictionary with 
# the following format:

# Sample output
# {
#   "Kaivopuisto": (24.950292890004903, 60.155444793742276),
#   "Laivasillankatu": (24.956347471358754, 60.160959093887129),
#   "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673)
# }
# Dictionary keys are the names of the stations, and the value attached is a tuple containing 
# the location coordinates of the station. The first element in the tuple is the Longitude field, 
# and the second is the Latitude field.

# Next, write a function named distance(stations: dict, station1: str, station2: str), which 
# returns the distance between the two stations given as arguments.

# The distance is calculated using the Pythagorean theorem. The multiplication factors below 
# are approximate values for converting latitudes and longitudes to distances in kilometres in 
# the Helsinki region.

# # we will need the function sqrt from the math module 
# import math

# x_km = (longitude1 - longitude2) * 55.26
# y_km = (latitude1 - latitude2) * 111.2
# distance_km = math.sqrt(x_km**2 + y_km**2)
# Some examples of the function in action:

# stations = get_station_data('stations1.csv')
# d = distance(stations, "Designmuseo", "Hietalahdentori")
# print(d)
# d = distance(stations, "Viiskulma", "Kaivopuisto")
# print(d)
# Sample output
# 0.9032737292463177
# 0.7753594392019532

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, 
# take a look at these instructions.

# The greatest distance
# Please write a function named greatest_distance(stations: dict), which works out the two stations 
# on the list with the greatest distance from each other. The function should return a tuple, where 
# the first two elements are the names of the two stations, and the third element is the distance 
# between the two.

# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
# Sample output
# Laivasillankatu Hietalahdentori 1.478708873076181


# tee ratkaisu tänne
# Write your solution here
# we will need the function sqrt from the math module 
import math

#*******************************************************
#*********  Convertir un archivo a diccionario  ********
#*******************************************************

def get_station_data(fle_name:str)->dict:
    file_info = {} #Abre un diccionario vacio
    with open(fle_name) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == "Longitude": # Obvia la cabecera
                continue
            arg_list=[]
            for arg in parts: # Evaluamos si los argimentos son numeros y los evaluamos como numeros si son cadenas los evaluamos como cadenas
                try:
                    arg_list.append(float(arg)) # 
                except:
                    arg_list.append(arg.strip())
            arg_tuple=(arg_list[0],arg_list[1])
            file_info[parts[3]] = arg_tuple # Crear el diccionario de estudiantes la primera columba como Key y el resto como lista
    return file_info
#*******************************************************
#********  Calcular distancia entre estaciones  ********
#*******************************************************
def distance(stations: dict, station1: str, station2: str)-> int:
    coord1=stations[station1]
    coord2=stations[station2]
    # longitude1=float(coord1[0])
    # longitude2=float(coord2[0])
    # latitude1=float(coord1[1])
    # latitude2=float(coord2[1])
    x_km = (float(coord1[0]) - float(coord2[0])) * 55.26
    y_km = (float(coord1[1]) - float(coord2[1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
#*******************************************************
#*********   Calcular la distancia mas larga    ********
#*******************************************************
def greatest_distance(stations: dict):
    station_distances={}
    distance_pair=0
    station_key_list=list(stations.keys())
    for station1 in stations.keys():
        for station2 in station_key_list:
            if station1 == station2:
                continue
            else:
                distance_pair=distance(stations,station1,station2)
                station_distances[distance_pair]=[station1,station2]
        station_key_list.pop(0)
    max_distance=max(list(station_distances.keys()))
    return (station_distances[max_distance][0],station_distances[max_distance][1],max_distance)





# You can test your function by calling it within the following block
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data('stations3.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)