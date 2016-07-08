#!/usr/bin/env python3
import sys
import math
sys.path.insert(0, './data')
from common import print_solution, read_input

def distance(city1, city2):
    # city1, city2 = xy_list[city1], xy_list[city2] #city index to coordinate
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def solve(cities,dist_sum = 0):
    N = len(cities)
    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    current_city = 0
    last_city_pos = 0  
    unvisited_cities = set(range(1, N))
    best_route = [current_city]

    def distance_from_current_city(to):
        return dist[current_city][to]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=distance_from_current_city) 
        dist_sum += dist[current_city][next_city]
        unvisited_cities.remove(next_city)
        best_route.append(next_city)
        current_city = next_city

    opt = opt_2(best_route,dist)
    result = or_opt(opt,dist)

    return result

def total_distance(result, total_dist = 0 ): 
    i,j= 0, 1
    while i < (len(result)-1) and j < len(result):
        total_dist += distance(xy_list[result[i]], xy_list[result[j]])
        i+= 1
        j+=1 
    return total_dist

def opt_2(best_route,dist):
    N = len(best_route)
    total = 0
    rev_best_route=[]
    while True:
        count = 0
        for a1 in range(N-2):
            a2 = a1 + 1
            for b1 in range(a1+2,N):
                if b1 == N - 1:
                    b2 = 0
                else:
                    b2 = b1 + 1
                if  a1!=0 or b2 != 0:
                    c1 = dist[best_route[a1]][best_route[a2]]
                    c2 = dist[best_route[b1]][best_route[b2]]
                    c3 = dist[best_route[a1]][best_route[b1]]
                    c4 = dist[best_route[a2]][best_route[b2]]
                    if c1+c2 > c3+c4:
                        rev_best_route = best_route[a2:b1+1]
                        best_route[a2:b1+1] = rev_best_route[::-1] 
                        count += 1
                    else:
                        rev_best_route = best_route
        total += count
        if count == 0:break
    return best_route

def or_opt(opt2,dist):
    N = len(opt2)
    total = 0
    while True:
        count = 0
        for i in xrange(N):
            i0 = i - 1
            i1 = i + 1
            if i0 < 0: i0 = N - 1
            if i1 == N: i1 = 0
            for j in xrange(N):
                j1 = j + 1
                if j1 == N: j1 = 0
                if j != i and j1 != i:
                    l1 = dist[opt2[i0]][opt2[i]] 
                    l2 = dist[opt2[i]][opt2[i1]]
                    l3 = dist[opt2[j]][opt2[j1]] 
                    l4 = dist[opt2[i0]][opt2[i1]]
                    l5 = dist[opt2[j]][opt2[i]]  
                    l6 = dist[opt2[i]][opt2[j1]] 
                    if l1 + l2 + l3 > l4 + l5 + l6:
                        p = opt2[i]
                        opt2[i:i + 1] = []
                        if i < j:
                            opt2[j:j] = [p]
                        else:
                            opt2[j1:j1] = [p]
                        count += 1
        total += count
        if count == 0: break
    return opt2        

if __name__ == '__main__':
    assert len(sys.argv) > 1
    xy_list = read_input("data/"+sys.argv[1])
    best_route= solve(xy_list)
    print total_distance(best_route)
    print_solution(best_route)