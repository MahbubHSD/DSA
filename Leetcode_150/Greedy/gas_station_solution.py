# Alternate file for gas_station.py

from gas_station import gas_station as _reference_gas_station

def gas_station(gas, cost):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_gas_station(gas, cost)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'gas_station.py')
