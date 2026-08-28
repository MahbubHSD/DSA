# Alternate file for car_fleet.py

from car_fleet import car_fleet as _reference_car_fleet

def car_fleet(target, positions, speeds):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_car_fleet(target, positions, speeds)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'car_fleet.py')
