# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: fibd (mortal fibonacci rabbits)
# (starts with the fib problem, plus rabbits die after a certain number of months)
# May 30, 2015

#Rules:
#The population begins in the first month with a pair of newborn rabbits.
#Rabbits reach reproductive age after one month.
#In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
#Exactly one month after two rabbits mate, they produce one male and one female rabbit.
#Now rabbits live for m months

# NEW PART:
#Given: Positive integers n≤100 and m≤20.  
#
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months

#Second parameter used to be k (rabbit pairs per litter)- is this now a set number?  1 pair?

    
DEBUG = True

def get_rabbit_pairs(num_of_months, rabbit_pairs_per_litter, lifespan_months):

    current_month = 1
    waiting_rabbit_pairs = 1
    eligible_rabbit_pairs = 0
    total_rabbit_pairs = 1 #always start with 1 pair in the first month
    birth_log = {0:1} # Initialize with the two newborns as month 0
    
# First approach: if I track the newborn_pairs, I can just subtract the right number at the end of each month
    
# Mating happens on the first day of the month, they're born on the last   
    while current_month <= num_of_months:
            if (DEBUG):
                print "=====MONTH:" , current_month
                print "On the morning of day one:"
                print "eligible_rabbit_pairs:" , eligible_rabbit_pairs
                print "waiting_rabbit_pairs:" , waiting_rabbit_pairs            

            rabbit_pairs_before_birth_and_death = eligible_rabbit_pairs + waiting_rabbit_pairs 
            pairs_of_new_babies= (eligible_rabbit_pairs)*rabbit_pairs_per_litter
            birth_log[current_month] = pairs_of_new_babies
            
            
            if current_month >= lifespan_months:
                dying_this_month = birth_log[current_month-lifespan_months]
            else: 
                dying_this_month = 0
            
            if (DEBUG):     
                print "The eligible rabbits copulate, and at the very end of the month this many pairs of babies are born:", pairs_of_new_babies
                print birth_log
            # At the end of the month: waiting pairs become eligible
            # waiting pairs gets replaced with the number of new babies
            # dying ones are removed from eligible_rabbit_pairs
            eligible_rabbit_pairs += waiting_rabbit_pairs 
            eligible_rabbit_pairs -= dying_this_month
            waiting_rabbit_pairs = pairs_of_new_babies
            
            if (DEBUG): 
                print "When the month ends:"
                print "This many pairs died:", dying_this_month
                print "eligible_rabbits_pairs:" , eligible_rabbit_pairs
            #print "new_babies (will wait next month):" , new_babies
                print "waiting_rabbit_pairs:" , waiting_rabbit_pairs            

            current_month +=1

    rabbit_pairs_after_birth_and_death = eligible_rabbit_pairs + waiting_rabbit_pairs
    return rabbit_pairs_before_birth_and_death, rabbit_pairs_after_birth_and_death


months = 97
rabbit_pairs_per_litter = 1
lifespan_months = 20

print get_rabbit_pairs(months, rabbit_pairs_per_litter, lifespan_months)

