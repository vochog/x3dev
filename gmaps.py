import webbrowser
import urllib.parse

def create_google_maps_route(locations):
    """
    Creates a Google Maps URL with a route through multiple locations.
    Opens the route in the default web browser.
    
    Args:
        locations (list): List of location strings in order of visit
    """
    if len(locations) < 2:
        print("You need at least 2 locations to plot a route.")
        return
    
    # Create the Google Maps URL
    base_url = "https://www.google.com/maps/dir/"
    
    # URL-encode each location and join with forward slashes
    encoded_locations = []
    for loc in locations:
        # Remove any existing URL encoding to avoid double-encoding
        cleaned_loc = urllib.parse.unquote(loc)
        encoded_loc = urllib.parse.quote(cleaned_loc)
        encoded_locations.append(encoded_loc)
    
    route_url = base_url + '/'.join(encoded_locations) + '/'
    
    # Print summary
    print("\nRoute Summary:")
    for i, loc in enumerate(locations):
        print(f"{i+1}. {loc}")
    
    print(f"\nOpening route in browser: {route_url}")
    
    # Open in web browser
    webbrowser.open(route_url)

if __name__ == "__main__":
    print("Google Maps Route Plotter (No API Key Needed)")
    print("Enter your locations one by one (press Enter without typing to finish):")
    
    locations = []
    while True:
        location = input(f"Location {len(locations)+1}: ").strip()
        if not location:
            if len(locations) >= 2:
                break
            else:
                print("You need at least 2 locations to plot a route.")
                continue
        locations.append(location)
    
    # Create and open the route
    create_google_maps_route(locations)