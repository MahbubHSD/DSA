# Alternate file for pow_x_n.py

from pow_x_n import power as _reference_power

def power(x, n):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_power(x, n)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'pow_x_n.py')
