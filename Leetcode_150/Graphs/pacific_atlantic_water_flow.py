# Leetcode Problem 417: Pacific Atlantic Water Flow

heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]


def pacific_atlantic(heights):
    """
    Find cells from which water can reach both oceans.

    Parameters:
    heights (list): A grid of terrain heights.

    Returns:
    list: Coordinates that can flow to both borders.
    """
    rows, columns = len(heights), len(heights[0])

    def reachable(starts):
        seen = set(starts)
        stack = list(starts)
        while stack:
            row, column = stack.pop()
            for next_row, next_column in ((row + 1, column), (row - 1, column), (row, column + 1), (row, column - 1)):
                if 0 <= next_row < rows and 0 <= next_column < columns and (next_row, next_column) not in seen and heights[next_row][next_column] >= heights[row][column]:
                    seen.add((next_row, next_column))
                    stack.append((next_row, next_column))
        return seen

    pacific = [(row, 0) for row in range(rows)] + [(0, column) for column in range(columns)]
    atlantic = [(row, columns - 1) for row in range(rows)] + [(rows - 1, column) for column in range(columns)]
    return [list(cell) for cell in reachable(pacific) & reachable(atlantic)]


if __name__ == "__main__":
    result = pacific_atlantic(heights)
    print(f"Cells reaching both oceans: {result}")