

import webbrowser

def generate_google_maps_url_with_directions(places):
    """
    Generates a Google Maps URL to display driving directions between multiple places.

    Args:
        places: A list of strings, where the first is the origin, the last is the
                destination, and any in between are waypoints.

    Returns:
        A string containing the Google Maps URL for directions, or None if
        the input list has fewer than two places.
    """
    if len(places) < 2:
        print("Please provide at least two places for directions.")
        return None

    base_url = "https://www.google.com/maps/dir/"
    origin = places[0].replace(" ", "+")
    destination = places[-1].replace(" ", "+")
    waypoints = "/".join([place.replace(" ", "+") for place in places[1:-1]])

    url = f"{base_url}{origin}/{waypoints}/{destination}"
    if waypoints:
        url = f"{base_url}{origin}/{waypoints}/{destination}"
    else:
        url = f"{base_url}{origin}/{destination}"

    return url

if __name__ == "__main__":
    num_places = 0
    while num_places < 2:
        try:
            num_places = int(input("Enter the number of places for directions (at least 2): "))
            if num_places < 2:
                print("Please enter a number greater than or equal to 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    places_for_directions = []
    print("Enter the places in the order you want to travel (starting with the origin).")
    for i in range(num_places):
        place = input(f"Enter place {i+1}: ")
        places_for_directions.append(place)

    google_maps_url = generate_google_maps_url_with_directions(places_for_directions)

    if google_maps_url:
        print(f"\nOpening Google Maps in your default web browser with driving directions from:")
        print(f"- Origin: {places_for_directions[0]}")
        if len(places_for_directions) > 2:
            print("- Waypoints:")
            for place in places_for_directions[1:-1]:
                print(f"  - {place}")
        print(f"- Destination: {places_for_directions[-1]}")
        webbrowser.open(google_maps_url)
