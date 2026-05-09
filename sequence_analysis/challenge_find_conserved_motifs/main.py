def find_motif_positions(sequence, motif):
    # Write your code here
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)]== motif:
            positions.append(i + 1) 
    return positions

sequence = "ATGCGATATCGATCGATCG"
motif = "ATCG"


positions = find_motif_positions(sequence, motif)
print(positions)
