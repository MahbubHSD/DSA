# Alternate file for partition_to_k_equal_sum_subsets.py

from partition_to_k_equal_sum_subsets import can_partition_k_subsets as _reference_can_partition_k_subsets

def can_partition_k_subsets(arr, k):
    """
    Alternate solution file for the same problem.
    Kept as a separate file under the same topic folder.
    """
    return _reference_can_partition_k_subsets(arr, k)

if __name__ == '__main__':
    print('Alternate solution file loaded for', 'partition_to_k_equal_sum_subsets.py')
