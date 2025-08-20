from copy import copy, deepcopy
import sys, os
import numpy as np

## Name:
## PID:

#######################################################
##############       QUESTION 1 HERE   ################
#######################################################

def myScheduleHelper(P, D):
  '''
    NOTE: YOU WILL NOT BE TESTED ON THIS FUNCTION. This is an optional helper function that may help with your implementation

    Input:
    List P, List D
        List P: A list of processing time of job J_1, ... J_n
        List D: A list of due dates of each job, J_1, ... J_n

    Return:
      List sol: A list containing the schedule after applying Moore's algorithm. i.e. from the write up: [2,3,4,1]
    '''

def myMoore(P, D):
  '''
    TODO:
    
    Implement Moore's algorithm and return the optimal schedule, along with the end times of the corresponding jobs.

    Input:
    List P, List D
        List P: A list of processing time of job J_1, ... J_n
        List D: A list of due dates of each job, J_1, ... J_n
 
    Return:
      List[Tuple[int, int]] sol: List containing optimal schedule of jobs, where in each tuple,
        where the first int refers to the job, and the second int corresponds to the end time of said job.
      Thus each tuple contains the following:
        1. The current job in the optimal order
        2. The end time of this job
      
      Remember, jobs start at 1 (ie. J_1 ... J_N)
      Remember, you start processing your jobs at time 0.
      Hint: Call myScheduleHelper from this function if you need to
 
  '''

def myMooreLate(P, D):
  '''
    TODO:
    
    Apply Moore's algorithm, and then return the late jobs in order

    Input:
    List P, List D
        List P: A list of processing time of job J_1, ... J_n 
        List D: A list of due dates of each job, J_1, ... J_n

    Return:
    List sol: a list of the late jobs in order, after performing Moore's algorithm

    Remember, jobs start at 1 (ie. J_1 ... J_N)
    Hint: Call myScheduleHelper from this function if you need to


  '''

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
