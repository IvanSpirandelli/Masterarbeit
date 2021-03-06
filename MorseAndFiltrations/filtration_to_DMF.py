import itertools as it

from MorseAndFiltrations.DMF_to_filtration import DMF_to_filtration


def filtration_to_DMF(filtration):
    critical = [0]*len(filtration)
    pairings = []
    indices_for_clearing = []
    for ind,simplex in enumerate(filtration):
        if(len(simplex) == 1):
            critical[ind] = 1
        elif not simplex_in_pairings(simplex, pairings):
            pair = find_youngest_facet(simplex, filtration, pairings)
            if(pair == None):
                critical[ind] = 1
            else:
                tmp = filtration.index(pair)
                if(filtration[find_oldest_cofacet(pair, filtration)]==simplex):
                    pairings.append([list(pair),simplex])
                    critical[tmp] = 0
                else:
                    critical[ind] = 1
                if(len(pair) > 1):
                    indices_for_clearing.append(tmp)
    indices_for_clearing.sort()
    return [filtration[i] for i in range(len(filtration)) if critical[i] == 1], pairings, indices_for_clearing

def filtration_to_emergent_face(filtration):
    pairings = []
    indices_for_clearing = []
    for ind,simplex in enumerate(filtration):
        if(len(simplex) == 1):
            continue
        elif not simplex_in_pairings(simplex, pairings):

            pair = find_youngest_facet(simplex, filtration, pairings)
            tmp = filtration.index(pair)
            if(filtration[find_oldest_cofacet(pair, filtration)]==simplex):
                pairings.append([list(pair),simplex])
            if(len(pair) > 1):
                indices_for_clearing.append(tmp)

    indices_for_clearing.sort()
    return pairings, indices_for_clearing

def simplex_in_pairings(simplex, pairings):
    simplex = list(simplex)
    for pair in pairings:
        if(simplex in pair):
            return True
    return False

def find_oldest_cofacet(simplex, filtration):
    for i,elem in enumerate(filtration):
        if(len(elem) - 1 == len(simplex)):
            if all(s in elem  for s in simplex):
                return i

def find_youngest_facet(simplex, filtration, pairings):
    combis = [comb for comb in it.combinations(simplex, len(simplex)-1)]
    combis.sort()
    curr_max_index = -1

    for combi in combis:
        tmp = filtration.index(list(combi))

        if tmp > curr_max_index:
            curr_max_index = tmp

    if(curr_max_index == -1 or simplex_in_pairings(filtration[curr_max_index], pairings)):
        return None

    return filtration[curr_max_index]
