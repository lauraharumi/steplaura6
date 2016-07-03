#!/usr/bin/env python3

import sys
import math
sys.path.insert(0, './data')
# from common import print_solution, read_input, format_solution

from common import print_solution, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    last_city_pos = 0  
    sum = 0
    unvisited_cities = set(range(1, N))
    solution = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city) 
        sum += dist[current_city][next_city]
        unvisited_cities.remove(next_city)
        solution.append(next_city)
        current_city = next_city

    sum += dist[current_city][last_city_pos]
    print sum
    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input("data/"+sys.argv[1]))
    print_solution(solution)
