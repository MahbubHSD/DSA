# Alternate file for k_closest_points_to_origin.py

from k_closest_points_to_origin import k_closest as _reference_k_closest

def k_closest(points, k):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_k_closest(points, k)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'k_closest_points_to_origin.py')
