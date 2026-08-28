# Alternate file for asteroid_collision.py

from asteroid_collision import asteroid_collision as _reference_asteroid_collision

def asteroid_collision(asteroids):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_asteroid_collision(asteroids)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'asteroid_collision.py')
