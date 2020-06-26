rna_key = {'A':'T','T':'A','G':'C','C':'G'}
def DNA_strand(dna):
    return ''.join(rna_key.get(x,'') for x in dna)
