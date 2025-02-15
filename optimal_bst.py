import numpy as np

def optimal_bst(p, q):
    """This will compute the table of expected cost and the root table which 
    will store the value of key which needs to be at the root between keys i 
    and keys


    Parameters:
    ----------
    p: a list of probabilities of keys
    q: a list of probabilities of dummy keys

    Returns:
    e: expected cost table between ith and jth key
    root: stores the dummy key index that should be placed at the root
    
    """
    if np.sum(p) + np.sum(q) != 1:
        raise ValueError("The sum of p and q is not 1 as required for probability.")
    
    n = len(p)
    
    # stores expected cost
    e = np.zeros((n + 2, n + 1))
    
    # stores probabilities between i and j th key
    w = np.zeros((n + 2, n + 1))

    # root
    root = np.zeros((n+1, n+1))

    for i in range(1, n + 2):
        e[i, i - 1] = q[i - 1]
        w[i, i - 1] = q[i - 1]

    for length in range(1, n+1):
        for start_keys in range(1, n - length + 2):
            end_keys = start_keys + length - 1

            e[start_keys, end_keys] = float('inf')
            w[start_keys, end_keys] = w[start_keys, end_keys - 1] + p[end_keys - 1] + q[end_keys]
            for r in range(start_keys, end_keys + 1):
                min_val = e[start_keys, r-1] + e[r+1, end_keys] + w[start_keys, end_keys]

                if min_val < e[start_keys, end_keys]:
                    e[start_keys, end_keys] = min_val
                    root[start_keys, end_keys] = r
                
    
    return e, root

p = [0.15, 0.10, 0.05, 0.10, 0.20]  # 0, 1, 2, 3, 4
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.1]  # 0, 1, 2, 3, 4, 5
n = len(p)
e, root = optimal_bst(p, q)
print(e, root)

