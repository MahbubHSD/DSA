# Alternate file for car_pooling.py

from car_pooling import can_carpool as _reference_can_carpool

def can_carpool(trips, capacity):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_carpool(trips, capacity)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'car_pooling.py')
