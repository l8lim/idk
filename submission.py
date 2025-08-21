from copy import copy, deepcopy
import sys, os
import numpy as np

## Name: Lianna
## PID:A18576839

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################
from copy import copy, deepcopy
import sys, os
import numpy as np

def _core_schedule(P, D):
    n = len(P)
    by_deadline = sorted(range(1, n + 1), key=lambda j: D[j - 1])

    t = 0
    kept = []
    dropped = []

    for j in by_deadline:
        kept.append(j)
        t += P[j - 1]

        if t > D[j - 1]:
            worst_idx = 0
            worst_job = kept[0]
            worst_p = P[worst_job - 1]
            for idx, jj in enumerate(kept[1:], 1):
                pj = P[jj - 1]
                if pj > worst_p:
                    worst_p = pj
                    worst_idx = idx
                    worst_job = jj

            kept.pop(worst_idx)
            dropped.append(worst_job)
            t -= worst_p

    return kept + dropped, dropped


def myMoore(P, D):
    order, _ = _core_schedule(P, D)
    t = 0
    out = []
    for j in order:
        t += P[j - 1]
        out.append((j, t))
    return out


def myMooreLate(P, D):
    _, dropped = _core_schedule(P, D)
    return dropped

#######################################################
##############       QUESTION 2 HERE   ################
#######################################################

def myMcNaughton(P, m):
    if m <= 0:
        raise ValueError("m must be positive")
    total = sum(P)
    maxp = max(P) if P else 0
    C = max((total + m - 1) // m, maxp)
    sol = [[] for _ in range(m)]
    if not P:
        return sol
    proc = 0
    used = 0
    rem = C
    for i in range(len(P)):
        job_id = i + 1
        r = P[i]
        while r > 0:
            if rem == 0 and proc + 1 < m:
                proc += 1
                used = 0
                rem = C
            take = r if r <= rem else rem
            start = used
            end = used + take
            sol[proc].append((job_id, start, end))
            used = end
            rem -= take
            r -= take
            if rem == 0 and proc + 1 < m:
                proc += 1
                used = 0
                rem = C
    return sol

