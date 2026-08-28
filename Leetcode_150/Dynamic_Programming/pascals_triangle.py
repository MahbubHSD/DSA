# Leetcode Problem 118: Pascal's Triangle

rows = 5


def pascals_triangle(rows):
    """Generate the first rows of Pascal's triangle."""
    result = []
    for row in range(rows):
        values = [1] * (row + 1)
        for index in range(1, row):
            values[index] = result[-1][index - 1] + result[-1][index]
        result.append(values)
    return result


if __name__ == "__main__":
    print(f"Pascal's triangle: {pascals_triangle(rows)}")