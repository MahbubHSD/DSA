# Alternate file for partition_labels.py

from partition_labels import partition_labels as _reference_partition_labels

def partition_labels(text):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_partition_labels(text)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'partition_labels.py')
