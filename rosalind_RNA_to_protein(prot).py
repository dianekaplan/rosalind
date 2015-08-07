# -*- coding: utf-8 -*-
# Diane Kaplan
# Rosalind Problem: RNA to protein (prot)
# http://rosalind.info/problems/iprb/
# Aug 7, 2015

#Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
#Return: The protein string encoded by s.

    
DEBUG = False

def RNA_to_protein(string):
    # k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

    RNA_string = string
    length = len(RNA_string)
    protein_string= ''
    cursor = 0
    current_codon= ''
    current_protein= ''
    stop_codons=['UAA', 'UAG', 'UGA']
    hit_stop = False
    
    rna_to_prot = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UGU":"C", "UGC":"C", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", 
   "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R",  "CGG":"R", "AUU":"I", 
    "AUC":"I", "AUA":"I", "AUG":"M", "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", 
    "AAG":"K", "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"} 
    
    
    while cursor < (length-2) and not hit_stop:
        current_codon = RNA_string[cursor:cursor+3]
        #print "current_codon:" , current_codon
        if current_codon in stop_codons:
            hit_stop = True

        else:
            protein_string += rna_to_prot[current_codon]
            #print "string is now: " , protein_string
        cursor +=3
    return protein_string            

            
    if (DEBUG): 
        print "we're in debug mode:"



our_string = 'AUGCUGUCGUGUUGGAGGACCCUUGUGUUAGGUUCUAUCCCACUAGAGUUAACUUUUAGCCCGGUAGUCACCCCCUCUAGUAAGAUACUCAAGUUAAUUGGUCACCCAACCGUUGCGGGAAACUCUCGUACGACCAUAAUGCUUUCCAGCCAGCUUAUAAGGAUUGAGAGAAUUGCGAAUCUUUGUAGUGCGCAGUACCUACCCAGAAAUUCCCUAAUGGGCGACCCUCAUCAGGCGCCUUGGAACUAUCCAGACGUUAUUUGUAUUGCCUACGGAUUCAGCUUUUAUCGGUUACGUGCGUGGAUGCGAAGGUACCUGCAAUCACCCACGAUAUCCGUAUACUGCGCUAGUCGAACAGGCAUCGAACGACUUCGUAUCACCUUAUCGCUCCUACACAGUUUCGGCCCGGAUCGAACAUGGAGGCCAAACUCGCGAGAUUCGCAGCAUUUCACCGGGCAGGCCAAGUCUUUUGCUGGUCCUAGGAGUGUCUGGAUGGCGGGGACAGAUUAUUUAAUUAAAGGCAAGAUAACUAUAAGAGGCCCCCGUUGUUGUGCCGCGGCAGGAGGAGAUCGUUUCACCUCACCCGGCUCGUUCGUCCGAUACUUAGUUUUUGAGCGCCCAGGAACAUUAGUUACUUCUUAUGGUGCACUUAUAGGGGUAAGGGAAACCACGAUUUCUGAAGUGCUUGGAGUCCACUCUACUACCCCAGACAGAGGUCGGAGACCUAUGGUUUAUCUGUCUAUGUCGUCAAUCACCUACACUCACACACGAGCAUUGGGGCGAUCAGCCCAAGAUCCCUGGCUCAUGUAUGGAGCCGCGACAACGACUCAGCUAGACGUUCCAGCCCGUCGCUGGAGAUCGGAAUGUCCUCGCGAAGCGCCUAGAUUAAUCAUCCGUAGCAAUAAAUUCCCUCAGACAAGUGUGGUAAGAGAACCAACGCCCUGGUCCUGUGCCCGAGACGCUUCGAUGUCCCCAAAUUCGAUAAAGGUUUUCCGCGGAAUGCACCCAAAAGCCUUGGAACAUAUCCAAAAUCCAUCUUCCGGUAGGAGGGUUUGGAGUCGAGCGUGCCCUUACAGUAUACUGCGGUUCGUCCGGCUAUGUGUAAGUAAGCGAACCAGGCGGAAUUGCCCCGACAGAUCUAUCGCUACCGUCUUUAUCGGCGUGACUCCAGAUGUUCGCUCUCUCAAGGCCUUACGUCACAAACCCGAACGGAACUCGGUUCGGAGGAUACGUCAUACAGCACUCCGUUACCCUAUGGACCCAUUCAUCUGCGCGCAAACGUUUUACAUCCGGGGCUAUAGUGUAAUUCGACACACCACAACAGACAGAACAAAGAACGGAAGGAACCUCCUUGCCGCGCAUCUUAGCUCACAUCUUUUCAGUGUCGCCCGCCUACUCGUCGCACGCCUAGUACAAUUUGGGCGGCGGAAAUCCUCAAAAAUAGCAGGCUGCGCCAAGUGGCAGACUAGUCAGCUGCACUGGAGACGCUUGACUCAGCGCCGAGGCGUCCGUAUAGAUCAGAAGUGUCGGCGAGCAGGCAAACAUAGUACACGCCCAGUCUGGCCGACAGAGGGCGAGCAAGGCUUACAGACAGAGUUUAGUCGGCAAUGCGUAUGCAUCAUCCCCCUCAUGACGAAUCACCUAAAGCAAACUGUCGUUGCCCUAUAUCCCGCCCGUGCAAAAGUUGAGAAGUCUAUCGUACAAUGCUUUCAUAUUACCAAGGAAAGAUUAGCCGUACGUGCAAACAUACAAGGCUCUCCCGGUCAAGUAGAGUUCAACUACGUGCAAACACUAUAUGCAAGAUUUCCAAAGAGCGAGGGGUCAUCCACCGCGACGAUAGCAGGCAUCGUGAUUCACCAGGCUGCGUGGCGUUGCUCCACAGUUCUGUGCGGUUCAGUCCUACUUCCACGGUGUGGGAGCUUGCGAUACUCCACCGGCCGAACUCGUAAACCCACGAGAAGGUGUGUGGCGUUACUAGUAUCGACUCAGCCCGAAGGUCUUGCCAGAUUCAGAUGUAAAGUUAGAAGGUCGCCAACCUUAGGAAUCUUUCGGUUUCAUAUUAACAGCGCAGAGUUGAUUCUCACCACCCUGACACUUGUGUUAGAUCACGUGGCGGCGCGUAAUGAUCGUGGGAUUGUACUGAACUCAGGUCUAACCCUCGGAGUGCUAGGACAUGCGGGCAGACUCCAAGUGCCUCGCGCGUGUACGGGCAACACCUCGGAAGUUGGAAUCCAAGGUAACCAUCGUGCGAUCUCUGAACCUCAGCUAUGGCUGGCUGUCGGAGAAUUGCUACGGGUACAAAACAAACAUACAGAACGUUCUUCAAUCCGAUCUGACCAAGUUUCGUCAGCGGACCGAGACUUCGAUUGUGCUUGCCGGAUGCUACAAUGUGCCACAGUACGCCGAGGUUUGGUGGAGGACAGUCCAAGUGACAACACUAUUUUGGACCUGUCGACGAAGACUAUGCCUGAUCAGGCAGAGGCAGUCACGUCAUUUCCCUCCAGUACCGAGUUCGCCUCGUACCGGUCAAGCAACCAUGCAGGUCGAACCAUAUCGCCGACAGCUACCUCAGAGAUAUUGGUUGUUUGUCACGUGAUCGUCCGCAUUACAAGAGAUCGGUCAAGUAUUAUCGACCGAAAUCUUAAACGGACUGAAGGGCGGCCGGGCAACGGGAGAUUCUCUCGCAUCACUAUAGCUUAUGUGUGUCCUCGCGUAAUAACACUAAUGUUGGGGGGUUCCCUAUCGAUAACCCAAGACCGUUGUUUGCAGCGCCGGCAUGAUACUAACAUUUUACUAUCUUUGGGGCCGCCAAGCGCCAAUACCUCGAUUAAGACGGAUACGGCUCCGCUCAAUUUCUCGGGGUUACCUAUUGAACUGGACAUCUAUGGCGCUAUUCGCUACGUCGCUUCGACAAGUAAAUCGGUAGCUGGUCCGCAGGUUCCUUCGGUCCGUUUUUAUCAACUACCUCUAGGCCGAGAAUAUCGUGGGGUCUGCAGGUAUAAACAGUGCGCGGCAAGACAGGCCUUGGCAGGAGUGAUAACUUGCGCCCUUUCUUUAUGUUGCCGCACAAUGCUCUACAAUCUGCUAUGCUGCAACAGUAGGGUAGCAUUAGAACUAUUUAAGCGCGGGAGGCUUGUCCAUUGUUCGUUGUCCGAGCUCGUACUAAGCUCUGCGGCAGGGUGCCUGGACUUUAUAAAAUUUCUAAUAUCUUUUGACCGCCAGGUGCGGGCUCAACAGUCUGGUCGCUAUCUCGCCCAUUUCUGUCAAGGCAGCCGGCAAUCGAGCCUGAACAGUUCGGUAAAAUUUACUGGAACCAUCCCAAACGAGAAGUUUAGAGCUUCGCACUUACAUGUCGCACACAGCCAAGUCAGGACGCCCAUAGGCCCCAUCAUAUUGAAAUGGGUGUCUUGCUAUAAGAUCACCAGAAUUUCUCUUACAUGCGUCCAGAUCUUUAUUUUCGAGGGUAACUGUCCAGGUGGGCGCCGUGUCGCUCCAUAUAGCUCCCUUCUUGAGAAUAGUACACGAAUCAACCAUGUUGUGACAGCCAGUGCACGUGAAAGGUCCAUGGGAUUCAGCCAGAGGCUACCUAGUAGCGAGUGUGGCCCUGCAAGGAGGAAGUCUGGCCCUGCAAUUGAGGUAGGGUUAUGGCACCAGCCAGUAUUGGAUGAAAGUGCUAACCUCCAUAACAGGAAACACGUUCCAUGGCAUUGUCCUAAGACGCAGCAUGUGCUUGAUGACGCGUAUGGCAGAACUUACAAAAUUGACCUCGAAACAUGCAAUUCCGUCUCCGGCAUAGUGCGCAUGAUUCCUGUCACUCUAAUACUCGCCACACAAUUGGCGGGUCCGCAAGACGGGACGGAUUGCAUAGUACAGCUUGACUACCUGACGUGUUACUCCUGUCACGUAGUGGGGGAGUGGUUGCCCGAUAACCUCUUUCAUGUAAAACUUCACACAUUGUGCGGAGACUGGAUCCAUUUGUCGCUCAAAGAAGCAGGUUUACGGUUAGUAGGUUUUCACUACCCUCAUGUUUCUUUAGAUCAAGUUCCUUGUUCUCAUGACAUGUCGGCCAACUUGUGUGGAGCAACGUCACACCCCCUCAUAUAUUGUCUUGCUUAUUCCCCUUAUCGCGCUCAGCAAUUUUUCGCACUGUCACUAAAAGCUUUUACCGGGGCAUUAGCUCCUCAUAGACGCGCGUUCAGCUCAUAUGUGGUCAAAAGCUUAUCAGUAUCUGCGUUACAUGAGGCGAUAGUUUUAGCUGCGACUCCAUGGCUGACAAACCUAAAUGGGAUGGCCUUAAUUACUUGGUACAGAUUGUUGAUAGAGAGUUGGACACUAAUAUCGACAUGUCGAGAUGGUCAUAUCGGUCAACGGAGGCUCCGACCCUGCAUUAUCGAUACGGUUGUCACGAACCGGGAUUAUCGAUUCAGUCCUCGGCUCAACUCUUUGUGGGUACCGGUUCUCAAGCUUACAGCCAUUCGCCAAGGUUUGAAAAUCUGGCCUCGCAUGUCGGCGCCACGUGUAGGUACACGAGUAUUAGAUGUUUUCCCGACAAAAGUGCGGGCUACUUCCUUUCUGAGAUCCGACUGCGCAGUCAGGGAUCGCUCCCUGAUGUGUUAUCGAAAGAUCAAGGAUCCGCUCCCACGGACGUCGCAUUCUAUGCGACUUCGCGCUGCGGAAGGAAAGAAAUGCAUUGGGCAUAGAGUCACUCAGUUAGUAAGAUGUCUUGGUAGCGCCAUCAGGAUGUAUCCGGGCAAGCCAGUCCGUUGGUCACAUACACCGCCAAGAUACUUGCUUACUUUAGUAGGCCGUCGGCAUGUUUCCUUAGAAGGAGGCGCCUGCCGCACUUCCGUCUGUGCAAAGGGGUCGCAAUAUCCCGUUCGUUUUGACGAUGUCUUAGCAUGCAGGGAAGUUAGUCCGGCCCGCCAGAGUAUAUGUCGGCAGCGACCUGAUAUGAGAUGCGGAGAACCCUUCGCCAUGCCAAACAGCCGGCUGCGGCGUACCCUCUCUCCCGCCGGUCAGGUUGAUGGAGAAUGGUCUAGACUCACGGUUCCUCCAACGCCGUCUACAAAUCUGGUCUCGUGUACGAGCUUAUCAUUCCUUUUUCCUAUCCCAAGCCACCGGGGGCCUGAACAACAUGGAACUAUUGGCAUUGUAAGCACGGAACAACUCUUUCGCAGCUCGUCGCUAGACUUGUGCAUAGUCGCAGGCGCGAUCUGCGAGAAUUAUUCACUCACUGCCGGGAGUACUUUAGAGGCCCGUAGAAGAGCUACAUGUCAGAUCGCUGCGUAUUACUUCUGUAUGCACCCCAUCAAUUCGUGGGAUGAAUUAAUACAUAAAGGGCGAAUGUACGCUUUUCCGCGUAGGACCAUGGAACACGGGAUCAGGCGUGCUGGCGGAUUCAAUGGUCCAUUCUCGCCCCAGAUGGACCCGGCUAUGUUAAAACCUCGUGAACUUGGCGUAGCCCUUGGACCAAAGCCGGGCGUGCAUGCUCUAUUAGAGGGGACCACUCGAUGUGAUGUUACUUACAAGGGCCCGGCUCGCCCAAUGUAUCAUAAAAAUGACGAUGGGUCUGGCGAGAAGAGCGUGUUUACCAUAGAAUCCAAGCGCCUCUGGGAUGUGGCCCUCCGCGCGCGUAGUGUGGAUGAGUUCGAGACUGGGUGGCGUCGUUUGUCUAGAACCCGCAAAUUUACACAGCUACCGAAAUAUUUGAAAGAUGAGGUUCAGUACAACUUUGAGGCAGAAUAUCUUAGCAAAGCGAUCGAGAAGUUCUGCGUUGCUGGGCCCAAAACUCAGUUAAGCCCGUCCUGUACUCGCUCACACCUACCAUCACUCUCUUCCUAUCCUGCGCUAAGCGUUCUCGAACUAUGGGAUCCCUUUCGAGGCGAAGGUCCGUAUGGACGGCCCACGAAAAUUCAAAAUAUCCGAGCAGUCAUAAACACUUGUGACGGUCCUCAAAGCAAGAUUAACGUAUUCGAACGUCUGAUUAGGUUAUCUCACGUACCGAGGCACAUCGUUUUAUGGAGAGGAAUGGUCCUGCAGAUCGGCGUGCACCGAAAUUUUUGCACUCUCUGUACGUCAUUUAGUUACGGUGACCGUGAGGGAGCUCCUCCCCGAUAUUUUACGCGAUGCAAGGCAACAGAAGAGCUAACACUCACAGAGCUCCGUUGCAAGGAUGUGAUGCCGGCGGCAAGACACGAGCUCAAGAGGAUCCGAGAGGUGAGCGCGCAAGCUACUCACAUUGACGUCACUGCACGGCUCAGGAUUGGCAGGCACUCGUUGCAGUUAAUUGUCAAAAGGCUGAGAUUAACCCAGCGCGGGUUAGCGUCCCGUAGGUGCUUAUUGACAAGAGACUCGUUCCGUCUACAGGGCAUGGCAAUCCCAAAGCUUAUGGGGACCCAUACAGUUCCCGCUCUUCAGAAAUCCCGGGACAGAUUGUCCUGCUCAUUAACGACGUUCGAGCACUCAUGCGGGCGGUCUACUAGUCUUGGCCUGGUAGGCGUUCGCCGAGCCCCUUGCUAUCCUCGUUGUAUGAAGCAGACAGUCCGCGUUUAUAAAUCCAAUGUGCUUACUUUUGCGUCGUUCUAUCCAGACCCGUUUCCGGACCCCUCGUUGCUUCCGUCUAUACCUAUGAGCUACCCUUCUGAAGAGUAUGAAUGUAAACCAUUGUGUGGGCCUGCCUGUGAGCCAGGUUCUCGCGACACCUGUAUCAAAGCAAGAGCCUUUUCAAUAGCCCAAGCACGUCCUUCGGGGCAGCUACAAGUAAUCGCCAGGAGCGCUUUCAACUGGUACUCUGGUGUCCCUGCCGAACUUCGGGGGUGUAAGGUUGCCUGGAAGUUGACAACAUUGUUAGACCACCUGCGGCGGUGUGACUUCGCGUCCAUAUCGAUGUCGCAGACGUAUUCGCAUACGUUUUAUGGGAGCCACAGCAUUGUAGUAGUGAAUCGAGGACGCCUUUCGAUUCGAUGUAAUAACCCUAGUAGUUCGCGCGCUUUUUUAGGAUCUGUACGGGAUACCCACACUGUCGGAAACUCAACCGUCCGUCAUGCGUGCCUCAUGGGAGACUUGGCUCAUCCCAGAAUAAGCUGGCGCAAGCGUACUAUCACAGGACAAGCCCCCAUUAACUGCAGCACGCCAAGUAAUACCUGUUGUCGAGUUAUUAGACACAACGCUGGUACAGCAGUAAUCUCGACAAAUAGUAUCUUCUAUUACUCACCGACUACCUACAUAAACGCUGUUAAUGGAGGCAAGGAGCAUGGGGGUGAGGCACCCGAUCGUGGUCACCGGGUACUGCACCGGCUCCGCUCGGGUUUGAAGCUCUAUCCCUCACCUGUAUGUAGUAAUUGUUAUGUUGACAAGACGAUUCGAGACCGGGAGAUCCUUAUGCUGACGGCAUCAAUACUAGUUUGGGCGACCUUUCUUCUUUGCCUUGUCAACGGGGCUGCUAUCGACAGAGAUCAACUACUUAGGGAGAACGCGUCACAACCACGAGAUCCCAAUAUGGCGCACGUCUGGAACAUAGUUUCGACAGAAAUUCACCUGACCUAUGCAUCUGACCAAACUGUUCUCUUUCCGACUGCAGACUCUCUUGCUACAUCCUGCUAUCCUUUGAAUUACCCACAGGAUGGAAGACGAAACAACGUAUCCAGUUCCCUCGCUGGGACGAAUUACAACGAGUGCAUAACGGGCAAAGGAACCUCGGCACCGCUACGUCCUGGCGCAGCAAGAGAACUUGGAGUUGUAAGGCGUAACCGUUUGUUGCACGCUUUCAGGAUCUCGUGCGGCCGUUCUCCACCAGGUAGGGACGGGACGUUUUUAGGUGUAUUUGUUGACCAUUGUACCCCCUUCGUGGUAAAUGGGCACUUUGGAAACCAGACGCUAACAGAUUCUAAGACUAUGCUCGCUCCUUUGCACAUGGCUUCUGCGAUACGGCUGCACGGAUAUAUCGUACCUAGCAAGAAACAGCGUCAUAGUCGGAGCAUUUAUAACCCCCGAUGUUCGAUUAAUUCCACUUUAAAUAGCCACGAACCCAUGCCUCGUCCGGCGGUCCGCUCCGGCGUUCACAAAUGGGGUGCGACCAGCAUGUUCGAGAUUUGCUCCAGCGCAAAAGCCCAUAAGGACGAGUUCCAUCAUGCUUUAGUAAGAUACAGUCUCUUUGAACUCGACGACUACAGGUCUAGGAACGGCAACGGCACCCUUCAUGCAAGUUCCCCCAAAAUAGGAUACCCUUACUAUCGGGCCCCUCGGGCUUCCCAUGGCUCUUAUCCGAUGAGGGAAAUGAGAGAGCCCGAACUGAGGAUGUGCACGAUCAGUUGUGACCCAGUAGUGGACAAGCCGGUUCUGUGGACCGAGGUUAUUUCUCGGUCGGCAUGCCGAAUUCCUGCUAAAGCAGGUCCGCGUCUCCACCACAAAAUCGAGUCUCCUGCUCCGAAAUUGGCCGUAGCUGAGCUACUCGCCAUUAUUGCAUCUCAACCGGCAGUAUUGGGAACACAGCAUUUGAUGGAGUAUUCUCGCUUAUUUAUGGUUCAACUGACUGGUGAUUAUUCCGGUUAUCUAACUUGUACUGUUUUGAAAUGUCCGACCGUGUGGAACACAAUCAAGCCCAUAAUUAGCGAAGCUCGGGUGGUUCAGUCGUACAAUCUCCCUCAUGCGAACAACCCCAUCGUUUUGGUCGCUAUGUCGCCUUCGGUCGGAAGCGCGUUUAUAAAUCCCGGGUGGCCGAUAUUCGCAAUAGACAGCUGUACUCCGACCAACCUAUGCACAUUCCGUUUACGUUGGCCUCUAGUCGCGUCUCUGCUUGCUAAGUAUUGCGUAUAUGACCAGUUUAGCCAUGACCAUCUUAUUGCCUGUGUCAACGGACAGCGAGACCACAUUGUGACGUUGAAUCUUCGUACACGGUCCGCUCGUACGGAAUCACUCUUAGAUCUCGGUAUUCGGUAUCAUUCAGAUGCAUCCAAACGAGGCAGACUUGAGUUGAUUCCACAAUGUAUAAGCCAAGACCCCACGACCUUAGUAGUACAGACGGGGUCGGUGGAGCUAGUGAAGAAUCACAGACCAUAA'
our_string= 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

print RNA_to_protein(our_string)



