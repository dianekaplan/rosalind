# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: finding a shared motif (lcsm) - aka repeat_new.py
# http://rosalind.info/problems/lcsm/
# July 31, 2016, but taking a bunch from repeat.py that I wrote Feb 28, 2015 for CSCI E-58
# Citations: This makes use of Jeff Parker's cs58FileUtil.py for reading file and doing cleanup

# Rules:
# Given: A collection of kk (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.

# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# Usage:
#     % python repeat_new.py <filename> [<minimal ORF length>]

    
DEBUG = False


import string
import sys

from cs58FileUtil import prepare, readMultiFastaFile

DEBUG = False

#make/return a list of the strings of this size
def make_strings_of_length (text, size):  
    length = len(text)
    result_list = []
    cursor = 0
    
    while cursor < length-size+1: 
        this_snippet = text[cursor:cursor+size]
        result_list.append(this_snippet)
        if (DEBUG):
            print this_snippet
        cursor +=1
        
    return result_list
    
#for a sequence, return the size of the longest repeat and the string (#NOTE: we don't return all if there are multiples)
def find_biggest_repeat (array):
    
    # First, determine the shortest sequence in the list (we'll look through that one) 
    shortest_seq = ''
    shortest_seq_length = ''
    
    for seq in array:
        if (shortest_seq == ''):
            shortest_seq = seq
            shortest_seq_length = len(seq)
        else:
            if shortest_seq_length > len(seq): 
                shortest_seq = seq
                shortest_seq_length = len(seq)              
    
    # for each size, make the combos, then check each in the other strings, until we have one hit for the size
    attempting_length = 2
    
    biggest_repeat_length = 0
    biggest_repeat = ''
    reached_longest_common_motif = False  #keep increasing size until we no longer have one in common at that length
    nmer_still_in_common = True

    
            
    while not (reached_longest_common_motif):
        if (DEBUG):
            print "Try for length: ", attempting_length
        
        # first, make the combos of this length
        possible_nmers = make_strings_of_length (shortest_seq, attempting_length)
            
        # then check each nmer in the other strings, until we have one in all of them (a hit for that size) 
        for nmer in possible_nmers:
            #print "Trying nmer: " , nmer
            nmer_still_in_common = True
            
            # for each nmer, check it in the strings until you have 1 miss (break)
            for seq in seqArray:
                if ( seq.find(nmer) < 0 ):
                    nmer_still_in_common = False
                    #print "Didn't find ", nmer, " in ", seq
                    break
    
            # if we made it through all sequences without a miss, save it as a winner 
            if ( nmer_still_in_common ):
                biggest_repeat_length = len(biggest_repeat)
                biggest_repeat = nmer
         
        # if you made it here, you finished going through each nmer for that length 
        
        # if you didn't find one in common, update not_done to false
        if (biggest_repeat_length < attempting_length):
            reached_longest_common_motif = True
            
        # if you found one in common for this length, try the next length          
        attempting_length +=1

#        
    if (DEBUG):
        return biggest_repeat, possible_nmers
                
    return biggest_repeat



if ((len(sys.argv) < 2) or (len(sys.argv) > 3)):
    print "Usage: python", sys.argv[0], "<filename>"
else:
    fileName = sys.argv[1]
    if (len(sys.argv) > 2):             # This should be an integer
        try:
            limit = int(sys.argv[2])    # Convert string to integer
        except ValueError:              # try-except catches errors
            print "\n\tExpecting an integer to define min ORF length, found",
            print sys.argv[2]
            exit()
    
    cleanedArray = []
        
    # instead of just one seq we'll have mutliple, need function to return an array of strings
    seqArray = readMultiFastaFile(fileName)
    if (DEBUG):
        print "We got back: ", seqArray
    
    for seq in seqArray:
        seq = prepare(seq)
        cleanedArray.append(seq)
        # not sure how to save back to seqArray, so saving into cleanedArray
            
    if (DEBUG):
        print "We'll be comparing: ", cleanedArray
    
    print "The biggest repeat in this sequence is: ", find_biggest_repeat(cleanedArray)


