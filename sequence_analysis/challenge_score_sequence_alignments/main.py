def score_alignment(seq1, seq2):
    # Write your code here
    matches = 0
    mismatches = 0
    gaps = 0

    for a, b in zip(seq1, seq2):
        if a == b:
            matches += 1
        elif a == "-" or b =="-":
            gaps += 1
        else:
            mismatches += 1

    return (matches, mismatches, gaps)
        
        

result1 = score_alignment("ATG-C", "AT-AC")
print(result1)

result2 = score_alignment("A--GC", "ATAGC")
print(result2)

result3 = score_alignment("ACGT", "TGCA")
print(result3)