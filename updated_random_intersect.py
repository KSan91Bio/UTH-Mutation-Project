import random
import numpy
import pybedtools
import operator
from operator import itemgetter
from pybedtools import BedTool

count_list = []
total_list = []
average_list = []
sorted_list = []

print('Loading variants.\n')
b = pybedtools.BedTool('cosmicchr1.bed').sort()
print('Loaded '+str(b.count()))

num_trials = 10
max_rand_shift = 1000

print('Loading matches.\n')
with open("matches_chr1.txt", "r") as m:
    matches = m.readlines()

print('Loaded '+str(len(matches))+' motifs.')
    


for r in range(num_trials):
    print('Running '+str(r)+' iteration.\n')
    
    trial_list = []
    random.seed()
    ran_pos = int(random.random()*2*max_rand_shift - max_rand_shift)

    randomized=""
    #with open("matches_chr1.txt", "r") as m:
     #   line = m.readline()
    print('Shifting and randomizing the regions.')

    n_line=0
    for line in matches:
    #while line:
        #print(line)
        #chromo = str(line.split("\t")[0])
        #start = int(line.split("\t")[1])
        #end = int(line.split("\t")[2])
        #name = str(line.split("\t")[3])

        tokens=line.split('\t')
        chromo = tokens[0]
        start = int(tokens[1])
        end=int(tokens[2])
        name=tokens[3]
        
        start_s = ran_pos + start
        start_e = ran_pos + end
        name_s = name.split('_')
        randomized = randomized + "\n" + chromo + "\t" + str(start_s) + "\t" + str(start_e) + "\t" + str(name_s[0])

        if n_line % 1000 == 0:
            print('Processed '+str(n_line))
            
        n_line+=1
        
        #line = m.readline()

    print('Creating bedtool object from randomized regions.\n')

    #print (randomized)
    RanIntersect = BedTool(randomized, from_string=True)
    #print (RanIntersect)

    print('Creating pybedtools object from regions.')
    a = pybedtools.BedTool(RanIntersect)

    print('Created '+str(a.count())+' regions')

    print('Intersecting regions.\n')
    intersecttrial = (a.intersect(b, u=True, stream = True))

    print('Processing intersections.\n')
    for trial_total in intersecttrial:
        trial_list.append(trial_total.name)
        total_list.append(trial_total.name)

    print('Processing overlap statistics.\n');
    trial_unique, trial_counts = numpy.unique(trial_list, return_counts = True)
    trial_result = dict(zip(trial_unique, trial_counts))
    unique, counts =  numpy.unique(total_list, return_counts = True)
    results = dict(zip(unique,counts))
    average_results = dict(zip(unique, counts/num_trials))
    #print (trial_result)
        #print (intersecttrial)
    print(trial_result)

print ("\n Total results of the trials: \n", results)
print ("\nAverage results of the trials: \n", average_results)

average_sorted = sorted(average_results.items(), key=operator.itemgetter(1),reverse=True)
total_sorted = sorted(results.items(), key=operator.itemgetter(1),reverse=True)
print ("\nThis is the total number of hits sorted by highest to lowest: \n", total_sorted)
print ("\nThis is the average number of hits sorted by highest to lowest: \n", average_sorted)
