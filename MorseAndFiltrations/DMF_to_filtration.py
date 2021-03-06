from MorseAndFiltrations.gradient_field import gradient_field
from MorseAndFiltrations.toposort import toposort_flatten

def DMF_to_filtration(simplices, pairings):
    gf = gradient_field(simplices, pairings)
    topsort = toposort_flatten(gf.dependencies, simplices)
    dim = len(max(topsort, key = len))
    out = []
    for i in range(1, dim+1):
        for elem in topsort:
            if len(elem) == i:
                out.append(list(elem))

    return out