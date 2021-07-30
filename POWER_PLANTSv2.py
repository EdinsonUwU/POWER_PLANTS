from typing import Set, Tuple, List, Dict
from itertools import permutations, cycle
from functools import lru_cache
from copy import deepcopy
def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:

    # creating the adjacency lists
    nodesConnections = {}
    all_cities = []
    for i in network:
        for j in range(2):
            if i[j] in nodesConnections.keys():
                if j == 0:
                    nodesConnections[i[j]].append(i[1])
                else:
                    nodesConnections[i[j]].append(i[0])
            else:
                if j == 0:
                    nodesConnections[i[j]] = [i[1]]
                else:
                    nodesConnections[i[j]] = [i[0]]
            if i[j] not in all_cities:
                all_cities.append(i[j])

    # IGNORING THE CEROS BEFORE DOING THE PERMUTATIONS
    leng_of_ranges = len(ranges)
    leng_of_ranges_without_cero = len(list(filter(lambda x: x != 0, ranges)))
    leng_of_ranges_cero = abs(leng_of_ranges-leng_of_ranges_without_cero)
    ranges = list(filter(lambda x: x != 0, ranges))

    # trying to short execution time ordering the cities by connectivity
    all_cities.sort(reverse=True, key=lambda x: len(nodesConnections[x]))
    # all the probabilities
    possible_hosts = permutations(all_cities, len(ranges))
    ranges.sort(reverse=True)
    ranges = cycle(ranges)
    possible_solutions = []
    index = 0
    
    #creating all the possible solutions
    for i in possible_hosts:
        for j in i:
            nextRange = next(ranges)
            try:
                possible_solutions[index][j] = nextRange
            except:
                possible_solutions.append([])
                possible_solutions[index] = {}
                possible_solutions[index][j] = nextRange
        index += 1
        
    # check all the possible_solutions to found a right one
    @lru_cache(maxsize=10000)
    def go_further(current_city, cities_not_reach, deep_path, len_path=0):
        cities_not_reach = list(cities_not_reach)
        cities_not_reach = deepcopy(cities_not_reach)

        def go_further1(current_city, cities_not_reach, deep_path, len_path=0):
            for i in nodesConnections[current_city]:
                if len_path < deep_path:
                    go_further1(i, cities_not_reach, deep_path, len_path+1)
                try:
                    cities_not_reach.remove(current_city)
                except:
                    pass
        go_further1(current_city, cities_not_reach, deep_path, len_path=0)
        return cities_not_reach, len(cities_not_reach)

    for i in possible_solutions:
        all_cities_copy = deepcopy(all_cities)
        for j in i:
            all_cities_copy = go_further(j, tuple(all_cities_copy), i[j], len_path=0)[0]
        #if a solution is found, then add the ceros
        if go_further(j, tuple(all_cities_copy), i[j], len_path=0)[1] == leng_of_ranges_cero:
            for k in all_cities_copy:
                i[k] = 0
            return i
