import random
import numpy
import pybedtools
import operator
import os
from operator import itemgetter
from pybedtools import BedTool

count_list = []
total_list = []
average_list = []
sorted_list = []
token_list = []
iteration_list = ""

# print ('Loading matches.\n')
# b = pybedtools.BedTool('matches_chr1.txt')
# print ('Loaded ' + str(b.count()))

num_trials = 20
max_rand_shift = 1000

file = open('cosmictrial20.bed', 'w')

print ('Loading variants.\n')
with open ("L_cosmic.bed", "r") as c:
    cosmic = c.readlines()
    for line in cosmic:
        tokens = line.split('\t')
#         chromo = modify[0]
#         start = int(modify[1])
#         end = int(modify[2])
        token_list.append(tokens)
        
        
print ('Loaded ' + str(len(cosmic)) +' variants.')

#add line for opening new file, prepare for tomorrow
for r in range(num_trials):
    #print ('Running ' + str(r+1) + ' iteration.\n')
    
    trial_list = []
    random.seed()
    ran_pos = int(random.random()*2*max_rand_shift - max_rand_shift)
    randomized = ""
    #randomized_combined = ""
    
    #print ('Shifting and randomizing the regions.')
    
#    n_line = 0
    for modify in token_list:
        
        chromo = modify[0]
        start = int(modify[1])
        end = int(modify[2])

        
        start_s = ran_pos + start
        start_e = ran_pos + end
        
        if start_s > 0:
            randomized = str(chromo) + "\t" + str(start_s) + "\t" + str(start_e) + "\t" + "trial:" + str(r+1) + "\n"
        #iteration_list = iteration_list + randomized
        #if num_trials == 2:
            #randomized = str(chromo) + "\t" + str(start_s) + "\t" + str(start_e) + "\t" + "trial:" + str(r+1)
        iteration_list = iteration_list + randomized
        #randomized_combined += int(randomized[modify])
#         if n_line % 1000 == 0:
#             print ('Processed ' + str(n_line))
#         n_line+=1
        
#print (randomized)
#print (iteration_list)
file.write(iteration_list)
print ("program complete")
file.close()

#print (randomized_combined)
# print ('Creating bedtool object from randomized regions.\n')
# RanIntersect = BedTool(iteration_list, from_string = True)
# #print (RanIntersect)
# print ('Creating pybedtools object from the regions.')
# a = pybedtools.BedTool(RanIntersect)
# #print (a)
# # print ('Created ' + str(a.count()) + ' regions.')

# print ('Intersecting regions.\n')
# Intersecttrial = (b.intersect(a, u=True, stream=True))

# # print ('Processing intersections.\n')
# print (Intersecttrial)
