# repeat.py        This proram finds the longest repeat in a sequnce
# Diane Kaplan        February 28,2015
#
# Usage:
#     % python repeat.py <filename> [<minimal ORF length>]

#Assumptions & Limitations: 
# Citations: This makes use of Jeff Parker's cs58FileUtil.py for reading file and doing cleanup

import string
import sys
#import cs58FileUtil  #doing the whole thing didn't work; prepare was considered undefined
from cs58FileUtil import prepare, readFastaFile

DEBUG = False

#make/return a dictionary of the strings of this length, with the count of each instance
def make_strings_of_length (text, size):  
    length = len(text)
    result_dictionary = {}
    cursor = 0
    
    while cursor < length-size+1: 
        this_snippet = text[cursor:cursor+size]
        
        # if it's already in the dictionary increment the count, otherwise add it
        if result_dictionary.get(this_snippet): 
            result_dictionary[this_snippet] +=1
        else:
            result_dictionary[this_snippet] = 1	
        cursor +=1

    return result_dictionary

#for a sequence, return the size of the longest repeat and the string (#NOTE: we don't return all if there are multiples)
def find_biggest_repeat (text):
    seq_length = len(text)
    
    if (DEBUG):
        seq_length = 30
        
    attempting_length = 1
    biggest_repeat_length = 0
    biggest_repeat = ''
    not_stumped = True  #keep increasing size until there's one where we're stumped
    best_result = {}
    while (attempting_length < seq_length/2 and not_stumped): #stop at seq_length/2 because best case for a long repeat is two long ones back to back 
        this_result = make_strings_of_length (seq, attempting_length)
        winner = max(this_result, key=this_result.get) 

        if this_result[winner] > 1:
            biggest_repeat_length =  attempting_length 
            biggest_repeat = winner
            best_result = this_result
        else: 
            not_stumped = False
        attempting_length +=1 
        
    if (DEBUG):
        return biggest_repeat_length, biggest_repeat, best_result 
                
    return biggest_repeat_length, biggest_repeat



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
    
    
    seq = readFastaFile(fileName) 
    seq = prepare(seq)
    print "The biggest repeat in this sequence is: ",find_biggest_repeat(seq)