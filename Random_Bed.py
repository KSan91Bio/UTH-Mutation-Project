import random

for r in range(3):
    random.seed()
    ran_pos = int(random.random()*2000 - 1000) #this will define the equation of the random function
    with open("matchestest.txt", "r") as m:
        matches = m.readlines()
        for line in matches:
            chromo = str(line.split("\t")[0]) #chromosome name position of array
            start = int(line.split("\t")[1]) #start position of gene
            end = int(line.split("\t")[2]) #end position of gene
            name = str(line.split("\t")[3]) #name of the gene
            period = str(line.split("\t")[4]) #optional for bed file
            strand = str(line.split("\t")[5]) #strand position of gene
            for add in line:
                total_s = ran_pos + start
                total_e = ran_pos + end
            #print (line, str(total_s), str(total_e))
            print (line) #provides information of the original start and end positions
            randomized = chromo +"\t"+ str(total_s) +"\t"+ str(total_e) +"\t"+ name +"\t"+ period +"\t"+ strand
            print (randomized)
            #print (chromo +"\t"+ str(total_s) +"\t"+ str(total_e) +"\t"+ name +"\t"+ period +"\t"+ strand)