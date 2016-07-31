# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: fib (Rabbits and Recurrence Relations)
# May 23, 2015

#Rules:
#The population begins in the first month with a pair of newborn rabbits.
#Rabbits reach reproductive age after one month.
#In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
#Exactly one month after two rabbits mate, they produce one male and one female rabbit.
#Rabbits never die or stop reproducing.

#Given: Positive integers n≤40 and k≤5.
#
#Return: The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, 
#every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

    
DEBUG = True

def get_rabbit_pairs(num_of_months, rabbit_pairs_per_litter):

    current_month = 1
    waiting_rabbit_pairs = 1
    eligible_rabbit_pairs = 0
    total_rabbit_pairs = 1 #always start with 1 pair in the first month
    
# Mating happens on the first day of the month, they're born on the last   
    while current_month <= num_of_months:
            if (DEBUG):
                print "=====MONTH:" , current_month
                print "On the morning of day one:"
                print "eligible_rabbit_pairs:" , eligible_rabbit_pairs
                print "waiting_rabbit_pairs:" , waiting_rabbit_pairs            

            pairs_of_new_babies= (eligible_rabbit_pairs)*rabbit_pairs_per_litter
            if (DEBUG):     
                print "Then eligible rabbits copulate, and on the last day of the month this many pairs of babies are born:", pairs_of_new_babies

            # At the end of the month: waiting pairs become eligible, and waiting pairs gets replaced with the number of new babies
            eligible_rabbit_pairs += waiting_rabbit_pairs 
            waiting_rabbit_pairs = pairs_of_new_babies
            
            if (DEBUG): 
                print "And at the very end of the month:"
                print "eligible_rabbits_pairs:" , eligible_rabbit_pairs
            #print "new_babies (will wait next month):" , new_babies
                print "waiting_rabbit_pairs:" , waiting_rabbit_pairs            

            current_month +=1
    rabbit_pairs_before_babies_are_born = eligible_rabbit_pairs
    total_rabbit_pairs = eligible_rabbit_pairs + waiting_rabbit_pairs
    return rabbit_pairs_before_babies_are_born, total_rabbit_pairs


months = 33
rabbit_pairs_per_litter = 4

print get_rabbit_pairs(months, rabbit_pairs_per_litter)

