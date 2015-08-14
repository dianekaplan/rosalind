# -*- coding: utf-8 -*-
# Diane Kaplan
# give next one
# Aug 10, 2015

# Rules:
# Given: a string
# Return: the next one: 
    #next("AAAA") should be "AAAC".
    #next("AAAC") should be "AAAG"
    #next("AAAG") should be "AAAT".
    #next("AAAT") should be "AACA"

    #Also, it wraps around. So, next ("TTTT") should be "AAAA"

DEBUG = False

def next(string):
    this_string= string
    length = len(this_string)

    next_base = {"A":"C", "C":"G", "G":"T", "T":"A"} 
    next_string=''
    
    cursor=0
    current_base=''
    looking_for_T_start = True
    digits_changing = 0
    old_ending=''
    new_ending_string=''
    
    # Start at the end of the sequence- easy if it's not T; just return the string with the last base advanced
    current_base = this_string[length-cursor-1]
    if current_base in ['A', 'C', 'G']: #we're only updating the last base
        next_string= this_string[:length-1]
        next_string+=next_base[current_base]
        
        
    # If there's a T at the end, we're rolling over multiple columns, so check how many and update the ending chunk      
    elif current_base == 'T':  
  
        while cursor < length and looking_for_T_start: #we're changing one more columns than the # of T's
            current_base = this_string[length-cursor-1]
            if current_base == 'T':
                cursor += 1
            else: # we found where it's no longer T's
                looking_for_T_start = False
                digits_changing = cursor +1
                
        if looking_for_T_start: #if we never saw the end of the streak, then it's all T's
            # next_string = [next_base[x] for x in this_string]  #(the right way)
            next_string = ['A' for x in this_string]            #(faster, probably)
            next_string= ''.join(next_string)       
 
        else: #we had some chunk of T's at the end, so keep original stuff up to that point and flip the rest
            next_string= this_string[:length-digits_changing]    #unchanging stuff first

            old_ending = this_string[length-digits_changing:]
            new_ending_list = [next_base[x] for x in old_ending]  #use list comprehension to grab the new characters
            new_ending_string= ''.join(new_ending_list)            #convert to string for concatenation
        
            next_string+=new_ending_string              # append the digits that are rolling over
        
        if (DEBUG): 
            print "I'm on: ", current_base
                         
#    if (DEBUG): 
#        print "string is:", this_string,", with length:",  length
#        print "Change will happen for ", digits_changing , "last digits"
#        print "old ending: ", old_ending
#        print "new ending: ", new_ending_string

    return next_string



print "After ACGTAAAA comes: ", next('ACGTAAAA')
print "After ACGTAAAC comes: ", next('ACGTAAAC')
print "After ACGTAAAG comes: ", next('ACGTAAAG')
print "After ACGTAAAT comes: ", next('ACGTAAAT')
print "After ACGTTTTT comes: ", next('ACGTTTTT')
print "After TTTTTTTT comes: ", next('TTTTTTTT')

