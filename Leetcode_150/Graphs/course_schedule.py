# Leetcode Problem 207: Course Schedule

number_of_courses = 2
prerequisites = [[1, 0]]


def can_finish(number_of_courses, prerequisites):
    """
    Determine whether all courses can be completed.

    Parameters:
    number_of_courses (int): The number of courses.
    prerequisites (list): Pairs [course, prerequisite].

    Returns:
    bool: False when prerequisites contain a cycle; otherwise, True.
    """
    graph = [[] for _ in range(number_of_courses)]
    indegree = [0] * number_of_courses
    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1
    queue = [course for course, degree in enumerate(indegree) if degree == 0]
    completed = 0
    for course in queue:
        completed += 1
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    return completed == number_of_courses


if __name__ == "__main__":
    result = can_finish(number_of_courses, prerequisites)
    print(f"Can finish courses: {result}")