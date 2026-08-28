# Leetcode Problem 698: Partition to K Equal Sum Subsets

arr = [4, 3, 2, 3, 5, 2, 1]
k = 4


def can_partition_k_subsets(arr, k):
    """Determine whether values can form k subsets with equal sums."""
    total = sum(arr)
    if total % k:
        return False
    target = total // k
    arr.sort(reverse=True)
    buckets = [0] * k

    def search(index):
        if index == len(arr):
            return True
        for bucket in range(k):
            if buckets[bucket] + arr[index] <= target:
                buckets[bucket] += arr[index]
                if search(index + 1):
                    return True
                buckets[bucket] -= arr[index]
            if buckets[bucket] == 0:
                break
        return False

    return search(0)


if __name__ == "__main__":
    print(f"Can partition into {k}: {can_partition_k_subsets(arr, k)}")