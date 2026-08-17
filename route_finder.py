import csv

# --- SEARCHING & CHECKING (if existing) ROUTE

def search_route(origin_input, dest_input):
    try:
        with open('community_routes.csv', mode='r') as input_file:
            with open('my_itinerary.txt', 'w') as output_file:
                reader = csv.DictReader(input_file)

                for route_details in reader:
                    if origin_input == route_details['Origin'].lower() and dest_input == route_details['Destination'].lower():
                        output_file.write(f"Take a {route_details['Transport_Type']} to {route_details['Destination']}\nLoading Zone: {route_details['Loading_Zone']}\nPossible Fare: ₱{route_details['Fare']}\n\nTIPS!\n{route_details['Community_Tip']}")
                    else:
                        continue
    except FileNotFoundError:
        print("Database Missing!")


current_location = input("Where you at?").lower()
destination = input("Where to go?").lower()

search_route(current_location, destination)