# Alternate file for game_of_life.py

from game_of_life import game_of_life as _reference_game_of_life

def game_of_life(board):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_game_of_life(board)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'game_of_life.py')
