# Alternate file for daily_temperatures.py

from daily_temperatures import daily_temperatures as _reference_daily_temperatures

def daily_temperatures(temperatures):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_daily_temperatures(temperatures)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'daily_temperatures.py')
