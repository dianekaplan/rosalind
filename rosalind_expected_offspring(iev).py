# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: expected offspring (iev)
# http://rosalind.info/problems/iev/
# July 31, 2016

# Rules:
# Given: Six positive integers, each of which does not exceed 20,000. The integers 
# correspond to the number of couples in a population possessing each genotype 
# pairing for a given factor. In order, the six given integers represent the 
# number of couples having the following genotypes: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

# Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
#under the assumption that every couple has exactly two offspring.
    
DEBUG = False


AA_AA = 18160
AA_Aa = 18647
AA_aa = 19102
Aa_Aa = 16533
Aa_aa = 18792
aa_aa = 19322

prob_from_Aa_Aa = .75

   #  A a
   #A x x
   #a x o

prob_from_Aa_aa = .5

   #  A a
   #a x o
   #a x o

offspring_per_couple = 2


if (DEBUG): 
    print "prob_from_Aa_Aa is:", prob_from_Aa_Aa
    print "prob_from_Aa_aa is:", prob_from_Aa_aa
    print "offspring_per_couple is:", offspring_per_couple


def offspring_having_dominant(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, offspring_per_couple):
    
    num_from_couple_with_homo_dom_parent = (AA_AA * offspring_per_couple) + (AA_Aa * offspring_per_couple) + (AA_aa * offspring_per_couple)
    num_from_Aa_Aa = Aa_Aa * offspring_per_couple * prob_from_Aa_Aa
    num_from_Aa_aa = Aa_aa * offspring_per_couple * prob_from_Aa_aa
    
    result = num_from_couple_with_homo_dom_parent + num_from_Aa_Aa + num_from_Aa_aa

    return result


print offspring_having_dominant(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, offspring_per_couple)




