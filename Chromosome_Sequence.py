import sys
#from pathlib import path

if len(sys.argv) < 3:
    print("USAGE: " + sys.argv[0] + " [VCF file path] [Chromosome IDs/Lengths list file path]\n")
    exit(0)
# from ctypes import *
# Define all the input file paths.
# vcf_fp = "Chr1_1000_Genomes.txt"
# vcf_fp = "1000_Genomes_ALL.vcf"
# chr_ids_lengths_fp = "hg19_lengths.list"
chr_ids_lengths = sys.argv[1]
vcf_fp = sys.argv[2]
#gc = open('Chr1_1000_Genomes_Sequence.txt', 'w')
# gc = open(chr_ids_lengths + "txt" , "w")
# Allocate the chromosome sequences.
NucleotideA = {}
NucleotideC = {}
NucleotideG = {}
NucleotideT = {}
print('Printing Chromosome Length.\n')
with open(chr_ids_lengths, "r") as h:
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
gc = open("chr" + chromosome + ".txt" , "w")
# Parse the VCF file.
n_lines = 0
with open (vcf_fp, "r") as g:
    overlaps = g.readlines()
    for line in overlaps:
        if line[0] == '#':
                continue
	
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
# if chrom != "1":
#         #         break
#         iif chrom != "1":
#         #         breakf alt_str == 'G':
#          if chrom != "1":
#         #         break   NucleotideG[chrom][int(pos)] = 1
# if chrom != "1":
#         #         break
#         iif chrom != "1":
#         #         breakf alt_str == 'T':
#          if chrom != "1":
#         #         break   NucleotideT[chrom][int(pos)] = 1

# Save signals.
gc.write(str(NucleotideA))
gc.write(str(NucleotideC))
gc.write(str(NucleotideG))
gc.write(str(NucleotideT))
gc.close()
    
print ("Program Complete")        