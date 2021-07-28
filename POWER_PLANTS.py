from typing import Set, Tuple, List, Dict
from itertools import permutations, cycle

def power_plants(network: Set[Tuple[str, str]], ranges: List[int]) -> Dict[str, int]:

    #creating the adjacency lists
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

    #all the probabilities
    possible_hosts = permutations(all_cities,len(ranges))

    #to found all the neighboors
    def go_further(current_city,cities_powered_up,deep_path,len_path = 0):
          cities_powered_up.append(current_city)
          for i in nodesConnections[current_city]:
              if (len_path != deep_path) and (i not in cities_powered_up):
                  go_further(i,cities_powered_up,deep_path,len_path+1)
              
    cities_powered_up = []
    possible_result = {}
    ranges = cycle(ranges)
    all_cities = set(all_cities)
    #to found the exact combination of letters (cities)
    while all_cities != cities_powered_up:
        possible_result = {}
        cities_powered_up = []
        city_hosts = next(possible_hosts)
        for i in city_hosts:
            nextRange = next(ranges)
            possible_result[i] = nextRange
            go_further(i,cities_powered_up,nextRange)
        cities_powered_up = set(cities_powered_up)

    return possible_result


if __name__ == '__main__':
    """
    print(power_plants([["A","B"],["B","C"],["C","D"],["D","E"],["F","G"],["G","H"],["H","I"],["I","J"],["K","L"],["L","M"],["M","N"],["N","O"],["P","Q"],["Q","R"],["R","S"],["S","T"],["U","V"],["V","W"],["W","X"],["X","Y"],["A","F"],["B","G"],["C","H"],["D","I"],["E","J"],["F","K"],["G","L"],["H","M"],["I","N"],["J","O"],["K","P"],["L","Q"],["M","R"],["N","S"],["O","T"],["P","U"],["Q","V"],["R","W"],["S","X"],["T","Y"]],[4]))

    print(power_plants([["A","B"],["B","C"],["C","D"],["D","E"],["F","G"],["G","H"],["H","I"],["I","J"],["K","L"],["L","M"],["M","N"],["N","O"],["P","Q"],["Q","R"],["R","S"],["S","T"],["U","V"],["V","W"],["W","X"],["X","Y"],["A","F"],["B","G"],["C","H"],["D","I"],["E","J"],["F","K"],["G","L"],["H","M"],["I","N"],["J","O"],["K","P"],["L","Q"],["M","R"],["N","S"],["O","T"],["P","U"],["Q","V"],["R","W"],["S","X"],["T","Y"]],[4]))
    """

    print(power_plants([["A","B"],["B","C"],["C","D"],["D","E"],["F","G"],["G","H"],["H","I"],["I","J"],["K","L"],["L","M"],["M","N"],["N","O"],["P","Q"],["Q","R"],["R","S"],["S","T"],["U","V"],["V","W"],["W","X"],["X","Y"],["A","F"],["B","G"],["C","H"],["D","I"],["E","J"],["F","K"],["G","L"],["H","M"],["I","N"],["J","O"],["K","P"],["L","Q"],["M","R"],["N","S"],["O","T"],["P","U"],["Q","V"],["R","W"],["S","X"],["T","Y"]],[3,1,1]))
