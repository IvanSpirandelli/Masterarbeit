def get_costly_edge_permutation():
    filtration = [[0], [1], [2], [3], [4], [5], [6], [7], [0, 4], [1, 2], [2, 3], [5, 6], [4, 5], [1, 6], [4, 7], [2, 6], [0, 6], [1, 5],
                  [3, 7], [5, 7], [0, 5], [6, 7], [1, 7], [3, 6], [3, 4], [2, 7], [0, 7], [2, 5], [0, 1], [0, 2], [1, 3], [3, 5], [2, 4], [0, 3], [1, 4],
                  [0, 1, 3], [0, 1, 4], [0, 1, 7], [0, 2, 5], [0, 2, 6], [0, 2, 7], [0, 3, 4], [0, 5, 6], [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 5], [1, 3, 6], [1, 3, 7],
                  [1, 6, 7], [2, 3, 4], [2, 4, 7], [3, 4, 5], [4, 5, 7], [5, 6, 7], [0, 3, 7], [1, 3, 4], [2, 5, 6], [3, 6, 7], [1, 2, 3], [1, 5, 6], [2, 3, 5], [3, 5, 6],
                  [2, 4, 5], [2, 5, 7], [0, 5, 7], [0, 6, 7], [0, 1, 6], [0, 1, 2], [0, 2, 4], [0, 4, 7], [3, 4, 7],
                  [0, 1, 3, 4], [0, 1, 3, 7], [0, 2, 5, 6], [1, 3, 6, 7], [1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 5],
                  [1, 3, 5, 6], [2, 3, 4, 5], [2, 4, 5, 7], [0, 2, 5, 7], [0, 5, 6, 7], [0, 1, 6, 7], [0, 1, 2, 6],
                  [0, 1, 2, 4], [0, 2, 4, 7], [0, 3, 4, 7]]

def filtration_given_by_davide():
    return [[0], [1], [2], [3], [4], [5], [6], [7],
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 2], [1, 3],
     [1, 4], [1, 5], [1, 6], [1, 7], [2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [4, 5], [4, 7], [5, 6], [5, 7],
     [6, 7], [2, 3], [3, 6], [3, 7],
            [0, 1, 3], [0, 1, 4], [0, 1, 7], [0, 2, 5],
            [0, 2, 6], [0, 2, 7], [0, 3, 4], [0, 5, 6],
            [1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 5],
            [1, 3, 6], [1, 3, 7], [1, 6, 7], [2, 3, 4],
            [2, 4, 7], [3, 4, 5], [4, 5, 7], [5, 6, 7],
            [0, 3, 7], [1, 3, 4], [2, 5, 6], [3, 6, 7],
            [1, 2, 3], [1, 5, 6], [2, 3, 5], [3, 5, 6],
            [2, 4, 5], [2, 5, 7], [0, 5, 7], [0, 6, 7],
            [0, 1, 6], [0, 1, 2], [0, 2, 4], [0, 4, 7],
            [3, 4, 7],

     [0, 1, 3, 4], [0, 1, 3, 7], [0, 2, 5, 6], [1, 3, 6, 7], [1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 5], [1, 3, 5, 6],
     [2, 3, 4, 5], [2, 4, 5, 7], [0, 2, 5, 7], [0, 5, 6, 7], [0, 1, 6, 7], [0, 1, 2, 6], [0, 1, 2, 4], [0, 2, 4, 7],
     [0, 3, 4, 7]]

def expensive_triange_bla():
    return [[0], [1], [2], [3], [4], [5], [6], [7],
            [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 2], [1, 3],
     [1, 4], [1, 5], [1, 6], [1, 7], [2, 4], [2, 5], [2, 6], [2, 7], [3, 4], [3, 5], [4, 5], [4, 7], [5, 6], [5, 7],
     [6, 7], [2, 3], [3, 6], [3, 7],
            [1, 3, 5], [1, 6, 7], [0, 4, 7], [0, 1, 6], [1, 2, 6], [4, 5, 7], [2, 3, 5],
     [3, 4, 7], [3, 4, 5], [1, 2, 3], [1, 2, 5], [2, 5, 7], [2, 4, 5], [5, 6, 7], [0, 5, 6], [2, 3, 4], [0, 1, 4],
     [1, 3, 6], [0, 2, 4], [1, 3, 7], [0, 2, 7], [1, 2, 4], [0, 1, 3], [0, 3, 7], [2, 4, 7], [3, 5, 6], [2, 5, 6],
     [0, 5, 7], [3, 6, 7], [0, 6, 7], [1, 3, 4], [1, 5, 6], [0, 3, 4], [0, 1, 7], [0, 1, 2], [0, 2, 6], [0, 2, 5],
     [0, 1, 3, 4], [0, 1, 3, 7], [0, 2, 5, 6], [1, 3, 6, 7], [1, 2, 3, 4], [1, 2, 5, 6], [1, 2, 3, 5], [1, 3, 5, 6],
     [2, 3, 4, 5], [2, 4, 5, 7], [0, 2, 5, 7], [0, 5, 6, 7], [0, 1, 6, 7], [0, 1, 2, 6], [0, 1, 2, 4], [0, 2, 4, 7],
     [0, 3, 4, 7]]