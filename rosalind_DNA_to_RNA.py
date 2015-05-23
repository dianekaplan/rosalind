def DNA_to_RNA(text):
    original= text
    RNA=''
    
    for x in text: 
        if x in ['A', 'C', 'G']:
            RNA+= x
        else:
            RNA += 'U'
    
    # Return counts
    return (RNA)
    

#string = 'CCGTTGCAGTTTGAACGGATTCCCGCGCACCGCGTCGATGGTAGCCTGTAGAAGCCTCGTAGTCCCAGATTGTTAAAGTAAGCTTGCTTATTACCGATTAGTACGTTCCGGGTGCTGGCCCATAAGGTGGGATACACGGACTTATGGCTGCGACATGTGACATTAGCCACACAGCCAGTGCTAAGGCTCTACTATAGTTAACAGAGACAAAACGAGACGTTGGGGGAGCACCCGAACACACCATCGAGCCCGAGCTGGGAAAACAGAGCACCTCTACAAGTGTAGTTACCAGTGACTAAAACTGACTTGCATCCCACAATTTATTACATCACGAGCCGCAGGCCGGTTTAGGACGTTCTACGTGTGTTTGTTTACCGGTATTTACCAACCGGGTGATGTTTCTTCCCGGCCTGGCAGTTCTGTTGCCGAAACTTACTTACAGTTTCTGCATTTCTAGAGGACCGATAGCTACTTGTCTCGCTCTTAGACTTGATTGAGTCAGAGCGATCGGTCTCCGCTCTCGCCATTCTGCTTCTAGGCCACAGCACCGCTCAGTACGCGGGGCCGACTTACTAAGCATCGTTGCACTCGCTGGATGCCTTTCAAGAAATCTAGGAAGTATAGCTTAGCCCTAGCGCGGAGGCGCGGTATAAGTGGGACCTTAGGCATATTTATTGGAAATAGTCATGCCGAACGGGCCAATTCGGCGAGATGATACACCTAAGAATGGACGAAAAAATGTGACACTACAGGATTATTGGCCATTACATGATATAGGCTCGGACGTTGTTGTTATCTTTTCGTAAACAAATTACCTATTGTGTCAGAGGCATGTCATGTAGACCTACTGCAACTCGCTGAAATTATGTCATTCCATCCTCT'
string = 'AAAGATTAAATCTCTGTACGGGTTAGTCTTGGCTTCGGCGGGGCTCACTACCCTGTCTGCAGTCGAAACCTCAACGAATGGCGGCTCAAGAGGTCCTGTGGCAAGTCTCCCCAATATTTGTGGTCAACGTATTTTTGGAGGGCGATCAGAAGGGCTCTCCTCTTAAATGACATGTTGGGCCGGTCCGAAATGTCCTGGAGAACTGAAAGATACAGCACTAGCATACTGTGGGTGTCGGATTCCACGCTCAGTCCGAAGCACCCAGTATCTCGCCGTATTAGGGGGATAATAGAGGTGCAAGCACCCAAGTCCTGGTCTCTGCGTCGAACCTTCAGCACAAACGAACAAATAAAAATTAGACGTTAACATCTTTGGGTGCTAAGTATAAGAACCCTGTACTTCCCAGGGGGCACTCCCGATCTCGTTCGCTCATTTTGTCTGCATATCTTAGCTCGCACTGCATACATTGCCTTCGTATGTGGTCTCCATCAAGGCACAGACTCTCCTAGGATCAGGGTGAGCATTATGAGCCGGCCAATTCCTTTGCGGGGGACCGCGAACAAAAGGCCTTAGTCGAAGATGGTTCTCAGCTTTACCGGGCAACTAATTCGAGGGAACTTATCATCTAGACGCGTCGTATGAGTACAACACCCACAGATTCGGGAAGTGCTCTTAGTTCCTTTGTGATGTGAAGCTCCTACGCTGACGGCAATATTCAGCGCGACCAACCGTCTTCGTCTTAACATTGTATTATTAGTTGGGTGCCGAACCAACCTCATCCAACATTCAGACGCAAACCTCAGAAGAAGTTGCTCTGCGCAAGAGGTGTATGAGCGCACCTGGTGCGCCAACCACACGATCTAGCAGGCATACTACGATTTAATACCATAAAGCGCGGCATTTG'
print DNA_to_RNA(string)