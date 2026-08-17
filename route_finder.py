import csv

current_location = input("Where you at? ").lower()
destination = input("Where to go? ").lower()

def search_route(origin_input, dest_input):

    with open('community_routes.csv', mode='r') as file:
        reader = csv.DictReader(file)

        for route_details in reader:
            if origin_input == route_details['Origin'].lower() and dest_input == route_details['Destination'].lower():
                print(route_details)
            else:
                continue

search_route(current_location, destination)