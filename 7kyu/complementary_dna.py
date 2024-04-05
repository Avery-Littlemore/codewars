def DNA_strand(dna):
    transformed_string = ''
    for char in dna:
        match char:
            case 'A':
                transformed_string += 'T'
            case 'T':
                transformed_string += 'A'
            case 'C':
                transformed_string += 'G'
            case 'G':
                transformed_string += 'C'
    return transformed_string

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"


print(DNA_strand("AAAA") == "TTTT")
print(DNA_strand("ATTGC") == "TAACG")
print(DNA_strand("GTAT") == "CATA")