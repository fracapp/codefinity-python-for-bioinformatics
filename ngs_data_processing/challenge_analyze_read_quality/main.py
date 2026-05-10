def count_high_quality_reads(fastq_lines, threshold):
    # Write your code here
    count = 0
    
    for i in range(0, len(fastq_lines), 4):
        quality_str = fastq_lines[i + 3]
        
        quality_scores = [ord(char) - 33 for char in quality_str]

        avg_quality = sum(quality_scores) / len(quality_scores)

        if avg_quality > threshold:
            count += 1

    return count
        

sample_fastq = [
    "@SEQ_ID1",
    "GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATTTTGGGGTTCAAAGCAGTATCGATCAAATAGTAA",
    "+",
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    "@SEQ_ID2",
    "AGCTTAGCTAGCTACCTATATCTTGGTCTTGGCCG",
    "+",
    "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII",
    "@SEQ_ID3",
    "CGTAGCTAGCTAGCTGACTGATCGATCGTAGCTAGC",
    "+",
    "########IIIIIIIIIIIIIIIIIIIIIIIIIIIII"
]

threshold_value = 30
result = count_high_quality_reads(sample_fastq, threshold_value)
print(result)
