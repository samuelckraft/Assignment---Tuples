#Task 1
def add_itinerary(schedule):
    name = input("Enter traveler name: ")
    origin = input("Enter city of origin: ")
    destination = input("Enter destination: ")
    schedule.append((name.capitalize(), origin.capitalize(), destination.capitalize()))

def display_itinerary(schedule):
    for traveler in schedule:
        name, origin, destination = traveler
        print(f"Itinerary {schedule.index(traveler) + 1}: {name} - From {origin} to {destination}")

schedule = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

add_itinerary(schedule)
display_itinerary(schedule)