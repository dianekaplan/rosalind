# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: inheritance (iprb)
# http://rosalind.info/problems/iprb/
# Aug 2, 2015 

# Rules:
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
# (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# That's the same as the probability that we got a dominant allele from one of the two parents
    
DEBUG = False


def prob_of_offspring_having_dominant(k, m, n):
    # k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

    homo_dom_count = k * 1.0 # multiplying by 1.0 to keep these as floats
    hetero_count = m * 1.0
    homo_rec_count = n * 1.0
    total_count = homo_dom_count + hetero_count + homo_rec_count
    
    # Calc the odds of getting a dominant letter from one of the two chosen parents
    


    
    #0) Summary text shows adding the probabilities for the different ways it can happen
    #a) first is homo dom (TBD%), second is anything (100%)    
    P_homo_dom_first = homo_dom_count/total_count
    
    #b) first is hetero, then...
    P_hetero_first = hetero_count/total_count #won't add directly
    
    #b1)...second is homo dom
    P_hetero_then_homo_dom = P_hetero_first * (homo_dom_count/(total_count-1))
    #b2) ...second is hetero, and their offspring gets one of the dominant alleles
    P_hetero_hetero_special = P_hetero_first * ((hetero_count-1)/(total_count-1))*(0.75)
    
  
    #c) first is homo rec, then...
    P_homo_rec_first = homo_rec_count/total_count  
    
        #c1) ...second is homo dominant
    P_homo_rec_then_homo_dom = P_homo_rec_first * (homo_dom_count/(total_count-1))
        #c2) ...second is hetero 
    P_homo_rec_then_hetero = P_homo_rec_first * (hetero_count/(total_count-1))       
        
    prob_one_parent_homo_dom = P_homo_dom_first + P_hetero_then_homo_dom + P_hetero_hetero_special + P_homo_rec_then_homo_dom + P_homo_rec_then_hetero
 
            
    if (DEBUG): 
        print "P_homo_dom_first:", P_homo_dom_first 
        print "P_hetero_then_homo_dom: ", P_hetero_then_homo_dom 
        print "P_hetero_hetero_special: ", P_hetero_hetero_special
        print "P_homo_rec_then_homo_dom: ",  P_homo_rec_then_homo_dom
        print "P_homo_rec_then_hetero: ", P_homo_rec_then_hetero

    return prob_one_parent_homo_dom


homo_dom = 15
hetero = 17
homo_rec = 25

print prob_of_offspring_having_dominant(homo_dom, hetero, homo_rec)



