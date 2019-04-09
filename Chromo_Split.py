import sys
if len(sys.argv) < 3:
    print("USAGE: " + sys.argv[0] + " [VCF file path] [Chromosome IDs/Lengths list file path]\n")
    exit(0)

vcf_fp = sys.argv[1]
chr_ids_lengths = sys.argv[2]

print("Splitting " + vcf_fp + " into chromosomes.")

# Splitting the chromosome length file separately
# for each chromosome in the file

vcf_files = {}

print("Creating new files for each chromosome")
with open(chr_ids_lengths, "r" ) as c:
    overlaps = c.readlines()
    for line in overlaps:
        chromo_name = line.split('\t') [0]
        length_chr = line.split('\t') [1]
        chromo_name = chromo_name.replace("chr", "")
        f = open(chromo_name + ".vcf", "w")
        vcf_files[chromo_name] = f

        #f.close()

# Parse the VCF file.
print("Parsing the VCF file")
n_lines = 0
with open (vcf_fp, "r") as g:
    overlaps = g.readlines()
    for line in overlaps:
        if line[0] == '#':
                continue

        n_lines = n_lines + 1

        if n_lines % 100000 == 0:
            print("Processing " + str(n_lines) + ". line\r")

        # Parse the chromosome id.
        tokens = line.strip().split("\t")
        chrom = tokens[0]

        # Write the current vcf line to the corresponding chromosome's VCF file.
        vcf_files[chrom].write(line)

# Close the VCF files for all the chromosomes.
with open(chr_ids_lengths, "r" ) as c:
    overlaps = c.readlines()
    for line in overlaps:
        vcf_files[chromo_name].close()
