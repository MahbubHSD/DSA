# Leetcode Problem 997: Find the Town Judge

n = 3
trust = [[1, 3], [2, 3]]


def find_judge(n, trust):
    """Find the person trusted by everyone who trusts nobody."""
    scores = [0] * (n + 1)
    for person, judge in trust:
        scores[person] -= 1
        scores[judge] += 1
    for person in range(1, n + 1):
        if scores[person] == n - 1:
            return person
    return -1


if __name__ == "__main__":
    print(f"Town judge: {find_judge(n, trust)}")