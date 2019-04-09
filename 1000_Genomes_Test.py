
# Define all the input file paths.
# vcf_fp = "Chr1_1000_Genomes.txt"
vcf_fp = "3.vcf"
chr_ids_lengths_fp = "hg19_lengths.list"
gc = open('Chr3_1000_Genomes_Sequence.txt', 'w')

# Allocate the chromosome sequences.
NucleotideA = {}
NucleotideC = {}
NucleotideG = {}
NucleotideT = {}
print('Printing Chromosome Length.\n')
with open(chr_ids_lengths_fp, "r") as h:
    overlaps = h.readlines()
    for line in overlaps:
        info = line.split('\t')
        chromosome = info[0]
        chr_length = info[1]
        chromosome = chromosome.replace("chr", "")
        # Remove "chr" from the name.
        
        print ("sequence of " + chromosome + " of length " + chr_length)
        NucleotideA[chromosome] = [0] * int(chr_length)
        NucleotideC[chromosome] = [0] * int(chr_length)
        NucleotideG[chromosome] = [0] * int(chr_length)
        NucleotideT[chromosome] = [0] * int(chr_length)

# Parse the VCF file.
n_lines = 0
with open (vcf_fp, "r") as g:
    overlaps = g.readlines()
    for line in overlaps:
        # if line[0] == '#':
        #         continue
	
        #print("Line is: " + line)
        tokens = line.strip().split("\t")
        #print(tokens)
        #print(len(tokens))
        chrom = tokens[0]
        pos = tokens[1]
        rsid = tokens[2]
        ref_str = tokens[3]
        alt_str = tokens[4]

        # if chrom != "1":
        #         break

        #print(chrom)
        #print(pos)
        #print(rsid)
        #print(ref_str)
        #print(alt_str)

#         n_lines = n_lines + 1
#         if n_lines % 1000 == 0:
#             print(n_lines)

#         key1, value1, value2 = line.strip().split(' ')      
      #  chrom, pos, rsid, ref_str, alt_str = line.strip().split(" ")      

        # Remove "chr" from the beginning.
       # chrom.replace("chr", "")
        
        if len(alt_str) != 1 or len(ref_str) != 1:
            continue
            
       # key1 = 250*1000*1000;
        
        if ref_str == 'A':
            NucleotideA[chrom][int(pos)] = 1

        if ref_str == 'C':
            NucleotideC[chrom][int(pos)] = 1

        if ref_str == 'G':
            NucleotideG[chrom][int(pos)] = 1

        if ref_str == 'T':
            NucleotideT[chrom][int(pos)] = 1
                
        if alt_str == 'A':
            NucleotideA[chrom][int(pos)] = 1

        if alt_str == 'C':
            NucleotideC[chrom][int(pos)] = 1

        if alt_str == 'G':
            NucleotideG[chrom][int(pos)] = 1

        if alt_str == 'T':
            NucleotideT[chrom][int(pos)] = 1

# Save signals.
gc.write(str(NucleotideA))
gc.write(str(NucleotideC))
gc.write(str(NucleotideG))
gc.write(str(NucleotideT))
    
print ("Program Complete")        
