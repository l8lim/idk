from copy import copy, deepcopy
import sys, os
import numpy as np

## Name: Lianna
## PID:A18576839

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################

def myScheduleHelper(P, D):
    n = len(P)
    jobs = sorted([(i + 1, P[i], D[i]) for i in range(n)], key=lambda x: x[2])
    T = 0
    on_time = []
    removed = []
    for j, p, d in jobs:
        on_time.append((j, p, d))
        T += p
        if T > d:
            j_drop, p_drop, d_drop = max(on_time, key=lambda x: x[1])
            on_time.remove((j_drop, p_drop, d_drop))
            removed.append(j_drop)
            T -= p_drop
    final_order = [jj for (jj, _, _) in on_time] + removed
    return final_order, removed

def myMoore(P, D):
    order, _removed = myScheduleHelper(P, D)
    p_by_id = {i + 1: P[i] for i in range(len(P))}
    t = 0
    schedule_with_end = []
    for j in order:
        t += p_by_id[j]
        schedule_with_end.append((j, t))
    return schedule_with_end

def myMooreLate(P, D):
    _order, removed = myScheduleHelper(P, D)
    return removed

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
