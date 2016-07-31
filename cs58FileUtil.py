# s50FileUtil
#
# Jeff Parker        Feb 2009
#
# File Handling utilities
# Other programs can use these utilities

import string
import sys

# Remove white space, change to upper case
def prepare(text):
    text = string.replace(text, " ", "")
    text = string.replace(text, "\n", "")
    text = string.replace(text, "\t", "")
    text = text.upper()
    return text

def readFastaFile(fileName):
    f = open(fileName, 'r')

    # First line in Fasta format is header
    line = f.readline()
    # print "Saw", line

    text = f.read()
    f.close()
    
    # Remove end of lines
    text = prepare(text)
    return text
    
def readMultiFastaFile(fileName):
#
#    seqArray = ["GATTACA", "TAGACCA", "ATACA"]
    seqArray = []
    
    f = open(fileName, 'r')
    currentString = ''
    

        
    for line in f:
        # if it's a new one, save the current value into array and start fresh
        # check that currentSring has something to prevent saving an empty value in the first step
        if ((line.find('Rosalind') > 0 ) & (currentString != '')):
        #if (line.find('Rosalind') > 0 ) :
            #print "this line is a new one"
            seqArray.append(currentString)
            currentString = ''
    
        # otherwise (it's one in progress) save it into currentString unless it's that very first rosalind heading
        else:    
            if (line.find('Rosalind') < 0 ):
                currentString += line
            #print "currentString is: ", currentString


    # add the last value
    seqArray.append(currentString)
    #line = f.readline()
    
    #while (line != '\n'):
    #    
    #    currentString += f.readline()
    #print "currentString is: ", currentString
#
    #line = f.readline()
    #print "Saw", line
    


#    text = f.read()
#    f.close()
    
    # Remove end of lines
    #text = prepare(text)
    return seqArray