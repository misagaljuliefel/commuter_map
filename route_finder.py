import csv

current_location = input("Where you at?").lower()
destination = input("Where to go?").lower()

with open('community_routes.csv', mode='r') as file:
    reader = csv.DictReader(file)

    for route_details in reader:
        if current_location == route_details['Origin'].lower() and destination == route_details['Destination'].lower():
            print(route_details)
        else:
            continue