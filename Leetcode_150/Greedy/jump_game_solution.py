# Alternate file for jump_game.py

from jump_game import can_jump as _reference_can_jump

def can_jump(arr):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_jump(arr)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'jump_game.py')
