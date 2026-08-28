# Leetcode Problem 735: Asteroid Collision

asteroids = [5, 10, -5]


def asteroid_collision(asteroids):
    """
    Resolve collisions between asteroids moving in opposite directions.

    Parameters:
    asteroids (list): Signed asteroid sizes; sign indicates direction.

    Returns:
    list: Asteroids remaining after all collisions.
    """
    stack = []
    for asteroid in asteroids:
        alive = True
        while alive and asteroid < 0 and stack and stack[-1] > 0:
            if stack[-1] < -asteroid:
                stack.pop()
            elif stack[-1] == -asteroid:
                stack.pop()
                alive = False
            else:
                alive = False
        if alive:
            stack.append(asteroid)
    return stack


if __name__ == "__main__":
    result = asteroid_collision(asteroids)
    print(f"Remaining asteroids: {result}")