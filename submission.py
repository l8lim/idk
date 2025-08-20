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
    '''
    Implement McNaughton function under here and return the optimal schedule.

    Input:
    List P: A vector of processing time of jobs J_1 ,...., J_n 
    int m: number of parallel and identical processors 

    return:
    List[List[Tuple[int, float, float]]] sol: The optimal schedule for each job on each processor.
        The i-th index of the outermost vector must contain the schedule of jobs for the (i+1)-th processor,
        in the form of List[Tuple[int, float, float]]. (Since processors start from 1 and vector indices start from 0).
        Each tuple inside this schedule must contain the following:
            1. index of job (job index starts at 1 NOT 0!) - int
            2. start time of the job on that respective processor - float
            3. end time of the job on that respective processor - float
    
    
    '''
    pass


P = [4, 2, 1, 3]
D = [5, 2, 3, 4]
print(myMoore(P, D))     
print(myMooreLate(P, D)) 
