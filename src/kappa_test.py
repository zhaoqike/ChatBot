from __future__ import division

from kappa.fleiss import fleissKappa

s1 = [1,2,1,2,1]
s2 = [2,2,2,2,1]

def scorelist_to_metric(sl, n, N, k):
    matrix = [[0 for i in range(k)] for i in range(N)]
    print matrix
    for scos in sl:
        for si in range(len(scos)):
            sco = scos[si]
            matrix[si][sco]+=1

    print matrix
    return matrix

rate = scorelist_to_metric([s1, s2], 2, 5, 3)
kappa = fleissKappa(rate,2)
print kappa

