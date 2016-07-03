#!/usr/bin/env python3
import itertools
import math
import sys
sys.path.insert(0, './data')
from common import print_solution, read_input
import time
start_time = time.time()

def calc_distance(city1, city2):
    city1, city2 = xy_list[city1], xy_list[city2] #city index to coordinate
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def try_everything(xy_list):
    shortest_dist= 100000000000000
    first_last = 0
    perms = itertools.permutations(range(1,len(xy_list)), len(xy_list)-1)
    for perm in perms:
        first_step =  calc_distance(first_last, perm[0])
        last_step = calc_distance(perm[len(perm)-1], first_last)
        i,j = 0, 1 
        in_between = 0 
        while i < (len(perm)-1) and j < len(perm):
            in_between += calc_distance(perm[i], perm[j])
            i+= 1
            j+=1 
        total_dist = first_step+in_between+last_step
        if total_dist < shortest_dist:
            shortest_dist, best_route = total_dist, perm
    return best_route, shortest_dist

if __name__ == '__main__':
    assert len(sys.argv) > 1
    xy_list = read_input("data/"+sys.argv[1])
    print try_everything(xy_list)
    print("RunTime: %s seconds" % (time.time() - start_time))
