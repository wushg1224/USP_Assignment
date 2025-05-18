import sys
import os
import re


# check argv number is right: option and file exsits
if len(sys.argv) < 3:
    print('It misses the argument file')
    sys.exit()


#check file if exsit and readable
argument_file = sys.argv[-1]
if os.path.isfile(argument_file):
    pass
else:
    print(f'{argument_file} is not a file or {argument_file} does not exist.')
    sys.exit(1)


#check if file is readable
if os.access(argument_file, os.R_OK):
    pass
else:
    print(f'{argument_file} does not have read access')
    sys.exit(1)


#A function to open and read file and create segment divided by ,
def parse_file(argument_file):
    segments = []
    with open(argument_file, 'r') as f:
        for line in f:
            line = line.strip()
            segment = line.split(',')
            segments.append(segment)
        return segments

#call function to save lists in a list
data = parse_file(argument_file)



#function for option -a 
#list origin-destination cities
def option_a(data):
    if not data:
        print('No distance information in this file')
    else:
        print('Origin-destination cities:')
        for record in data:
            origin = record[0]
            destination = record[1]
            print(f"{origin}-{destination}")



#function for option -o
#search origin and output destination & distance
def option_o(data, origin):
    matches =[]
    for record in data:
        if record[0] == origin:
            matches.append((record[1], record[2]))

    if not matches:
        print(f"No known destinations from {origin}")
    else:
        print(f'Destinations from {origin}:')
        for match in matches:
            print(f'City: {match[0]}\nDistance: {match[1]}')



#function for option -d
#search max distance and output destination & distance
def option_d(data, max_distance):
    matches =[]
    for record in data:
        if int(record[2]) <= max_distance:
            matches.append(record)

    if not matches:
        print(f"No cities within {max_distance} Km")
    else:
        print(f"Cities within {max_distance} Km distance:")
        for record in matches:
                origin, destination, distance = record
                print(f"{origin}-{destination}")
                print(f"Distance: {distance}")

#function for -v
#print student info
def option_v():
    print("Name: Wushuang Gao")
    print("Student ID: 25454152")
    print("Completed on: 18/05/2025")


#main controll
def main():
    arg_option = sys.argv[1]
    match arg_option:  
        case "-a":
                option_a(data)
        case "-o":
                origin = sys.argv[2]
                option_o(data, origin)
        case "-d":
                if len(sys.argv) != 4:
                     print('It misses the distance argument')
                else:
                    max_distance = int(sys.argv[2])
                    option_d(data, max_distance)
        case "-v":
                if len(sys.argv) != 3:
                    print("Usage: python travelhelper.py -v argument_file")
                else:
                    option_v()
    
        case _:
                print("this option doesn't exist")


if __name__ == "__main__":
    main()


