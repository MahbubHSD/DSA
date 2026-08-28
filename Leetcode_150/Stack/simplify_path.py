# Leetcode Problem 71: Simplify Path

path = "/home//foo/"


def simplify_path(path):
    """
    Convert a Unix-style path to its canonical representation.

    Parameters:
    path (str): An absolute Unix path.

    Returns:
    str: The simplified absolute path.
    """
    stack = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return "/" + "/".join(stack)


if __name__ == "__main__":
    result = simplify_path(path)
    print(f"Simplified path: {result}")