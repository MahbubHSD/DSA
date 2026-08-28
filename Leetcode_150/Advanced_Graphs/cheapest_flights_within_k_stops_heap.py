# Alternate file for cheapest_flights_within_k_stops.py

from cheapest_flights_within_k_stops import cheapest_flight as _reference_cheapest_flight

def cheapest_flight(n, flights, source, destination, stops):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_cheapest_flight(n, flights, source, destination, stops)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'cheapest_flights_within_k_stops.py')
