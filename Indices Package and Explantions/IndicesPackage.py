#This file contains all the indices used in our project.
#More details about each index is found in the file 'Indices_Explained'

import math
import numpy as np


#ONE FUNCTION TO RULE THEM ALL
def indices (sequence, *args):
    """
    This function is called with a given sequence, and index's name that we want to compute.
    The function brings back ONLY the index's value (int)
    
    Indices names you have to use for calling them:
    'shannonDiv', 'brillouinDiv', 'simsponDiv', 'mcintoshDiv',  'simpsonDom', 'shannonEve', 'simpsonEve', 'camargoEve'
    """

    #calcaulating how many actual splice sites in total, meaning sites with readings > 0
    total_ss=0
    for ss_read in sequence:
        if ss_read != 0:
            total_ss += 1
    
    possible_ss = len(sequence) #computing how many POSSIBLE splice sites (including sites with 0 readings)
     
    total_reads = sum(sequence) #computing how many splice sites readings in TOTAL. 
    
 
    
    #DIVERSITY INDICES
    if 'shannonDiv' in args:
        return shannon_diversity (sequence, possible_ss, total_reads, total_ss)
                 
    if 'brillouinDiv' in args:
        return brillouin_d_diversity (sequence, possible_ss, total_reads, total_ss)
                 
    if 'simsponDiv' in args:
        return simspon_diversity (sequence, possible_ss, total_reads, total_ss)
                 
    if 'mcintoshDiv' in args:
        return mcintosh_diversity (sequence, possible_ss, total_reads, total_ss)
        
    
    
    #DOMINANCE INDICES
    if 'simpsonDom' in args:
        return simpson_dominance (sequence, possible_ss, total_reads, total_ss)
    
    
    
    #EVENNESS INDICES
    if 'shannonEve' in args:
        return shannon_evenness (sequence, possible_ss, total_reads, total_ss)

    if 'simpsonEve' in args:
        return simpson_evenness (sequence, possible_ss, total_reads, total_ss)
    
    if 'camargoEve' in args:
        return camargo_evenness (sequence, possible_ss, total_reads, total_ss)



    
    
    
#____________________________DIVERSITY_____________________________
def shannon_diversity (sequence, possible_ss, total_reads, total_ss):
    
    index_value = 0
    
    for splice_site in sequence:
        x = splice_site/total_reads
        if x!=0:
            index_value += (x)*(math.log(x))
    
    return round(-1*index_value, 3)




def brillouin_d_diversity (sequence, possible_ss, total_reads, total_ss):
    
    index_value=0
    
    #calcaulation 1
    index_value = math.log(np.math.factorial(int(total_reads)))
    
    #calcaulation 2
    for splice_site in sequence:
        if splice_site!=0:
            index_value -= math.log(math.factorial(int(splice_site)))
    
    return round(index_value/total_reads, 3)



def mcintosh_diversity (sequence, possible_ss, total_reads, total_ss):
    
    counter=0
    index_value = total_reads
    
    #calculation 1
    for splice_site in sequence:
        counter += math.pow(splice_site, 2)
    
    #calculation 2
    index_value -= math.pow(counter, 0.5)
    
    #calculation 3
    return round(index_value / (total_reads - math.pow(total_reads,0.5)), 3)




def simspon_diversity (sequence, possible_ss, total_reads, total_ss):
    
    index_value = 0
    
    #calcaulation 1
    for splice_site in sequence:
        index_value += splice_site*(splice_site-1)
    
    #calcaulation 2
    index_value /= total_reads*(total_reads-1)
    
    return round(1 - index_value, 3)





#____________________________DOMINANCE___________________________

def simpson_dominance (sequence, possible_ss, total_reads, total_ss):
    
    index_value = 0
    
    for splice_site in sequence:
        index_value += math.pow(splice_site/total_reads,2)
    
    return round(1 - index_value, 3)







#____________________________EVENNESS___________________________

def shannon_evenness (sequence, possible_ss, total_reads, total_ss):

    return (shannon_diversity(sequence, possible_ss, total_reads, total_ss)) / math.log(possible_ss)




def simpson_evenness (sequence, possible_ss, total_reads, total_ss):

    ss = total_ss if actual else possible_ss
        
    return round ((1/simpson_dominance(sequence, possible_ss, total_reads, total_ss)) / ss, 3)




def camargo_evenness (sequence, possible_ss, total_reads, total_ss):
    
    index_value = 0

    ss = total_ss if actual else possible_ss
    
    for i, _ in enumerate(sequence):        
        for j in range(i+1, len(sequence)):
            index_value += abs((sequence[i]/total_reads)-(sequence[j]/total_reads))

    return round(1 - index_value/ss, 3)



