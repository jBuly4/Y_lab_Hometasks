#

from itertools import permutations
from math import sqrt

from points_cls import Points


# first point is always postal office, end point is always postal office
# path calculation: first point + [permutation] + first point

def generate_permutations(points: "Points") -> permutations:
    """
    Generate all possible permutations of given points
    :param points: points to permute
    :return: all possible permutations
    """
    return permutations(points)


def calculate_distance(start: tuple, end: tuple) -> float:
    """
    Calculate distance between start and end points
    :param start: start point
    :param end: end point
    :return: distance between start and end
    """
    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]

    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def path_length(start: tuple, path: "Points") -> float:
    """
    Calculate length of path
    :param start: point of postal office, also the end
    :param path: path (list of points)
    :return: path length
    """
    result = calculate_distance(start, path[0])
    for i in range(1, len(path)):
        result += calculate_distance(path[i - 1], path[i])
    result += calculate_distance(path[len(path) - 1], start)

    return result


def find_min_path(start: tuple, points: "Points") -> tuple:
    """
    Find minimal length of path
    :param start: postal office point
    :param points: initial points
    :return: minimal length and path
    """
    all_paths = generate_permutations(points)
    paths = {}
    for pth in all_paths:
        paths[path_length(start, pth)] = (start,) + pth + (start,)

    return min(paths.keys()), paths[min(paths.keys())]


def results(start: tuple, points: "Points") -> str:
    """
    Print results
    :param start: postal office point
    :param points: initial points
    :return: results to print
    """
    result = find_min_path(start, points)
    path = result[1]  # minimal path
    string_to_print = str(path[0])  # start point
    path_len = calculate_distance(path[0], path[1])
    for idx in range(2, len(path)):  # construction part of resulting string
        string_to_print += ' -> ' + str(path[idx - 1]) + "[" + str(path_len) + "]"
        path_len += calculate_distance(path[idx - 1], path[idx])
    string_to_print += ' -> ' + str(path[len(path) - 1]) + "[" + str(path_len) + "]" + " = " + str(path_len)

    return string_to_print


if __name__ == "__main__":
    some_input_points = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
    start_point = some_input_points[0]
    points = Points(some_input_points[1:])
    print(results(start_point, points))
