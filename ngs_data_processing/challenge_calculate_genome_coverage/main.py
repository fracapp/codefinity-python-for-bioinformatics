def calculate_coverage(read_starts, genome_length):
    # Write your code here
    coverage = [0] * genome_length

    for i in read_starts:
        if 0 <= i < genome_length:
            coverage[i] += 1

    return coverage
            

# Sample calls
read_starts1 = [0, 1, 2, 2, 3, 5]
genome_length1 = 6
result1 = calculate_coverage(read_starts1, genome_length1)
print(result1)

read_starts2 = [2, 2, 2, 4]
genome_length2 = 5
result2 = calculate_coverage(read_starts2, genome_length2)
print(result2)

read_starts3 = []
genome_length3 = 4
result3 = calculate_coverage(read_starts3, genome_length3)
print(result3)
