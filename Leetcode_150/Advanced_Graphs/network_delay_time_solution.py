# Alternate file for network_delay_time.py

from network_delay_time import network_delay_time as _reference_network_delay_time

def network_delay_time(times, n, k):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_network_delay_time(times, n, k)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'network_delay_time.py')
