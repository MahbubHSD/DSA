# Alternate file for find_the_town_judge.py

from find_the_town_judge import find_judge as _reference_find_judge

def find_judge(n, trust):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_find_judge(n, trust)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'find_the_town_judge.py')
