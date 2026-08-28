# Leetcode Problem 23: Merge k Sorted Lists


def merge_k_sorted_lists(lists):
    """
    Merge multiple sorted lists into one sorted list.

    Parameters:
    lists (list): Sorted integer lists.

    Returns:
    list: One sorted list containing every value.
    """
    import heapq

    heap = [(values[0], list_index, 0) for list_index, values in enumerate(lists) if values]
    heapq.heapify(heap)
    result = []
    while heap:
        value, list_index, value_index = heapq.heappop(heap)
        result.append(value)
        next_index = value_index + 1
        if next_index < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][next_index], list_index, next_index))
    return result


if __name__ == "__main__":
    result = merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
    print(f"Merged lists: {result}")