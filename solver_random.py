#!/usr/bin/env python3

import math
import sys
sys.path.insert(0, './data')
from common import print_solution, read_input, format_solution


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    # Build a trivial solution.
    # Visit the cities in the order they appear in the input.
    return list(range(len(cities)))

if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input("data/"+sys.argv[1])) #read first argument e.g. solver_random.py input_1.csv 
    print_solution(solution)
    # print solution 
    # print format_solution(solution)


