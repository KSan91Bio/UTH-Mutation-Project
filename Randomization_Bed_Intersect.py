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
b = pybedtools.BedTool('cosmicchr1.bed').sort()
num_trials = 2

for r in range(num_trials):
    trial_list = []
    random.seed()
    ran_pos = int(random.random()*2000 - 1000)
    with open("matchestest.txt", "r") as m:
        matches = m.readlines()
        for line in matches:
            #print(line)
            chromo = str(line.split("\t")[0])
            start = int(line.split("\t")[1])
            end = int(line.split("\t")[2])
            name = str(line.split("\t")[3])
            for add in line:
                start_s = ran_pos + start
                start_e = ran_pos + end
                name_s = name.split('_')
            randomized = chromo + "\t" + str(start_s) + "\t" + str(start_e) + "\t" + str(name_s[0])
            #print (randomized)
            RanIntersect = BedTool(randomized, from_string=True)
            #print (RanIntersect)
            a = pybedtools.BedTool(RanIntersect)
            intersecttrial = (a.intersect(b, u=True, stream = True))
            for trial_total in intersecttrial:
                trial_list.append(trial_total.name)
                total_list.append(trial_total.name)  
            trial_unique, trial_counts = numpy.unique(trial_list, return_counts = True)
            trial_result = dict(zip(trial_unique, trial_counts))
            unique, counts =  numpy.unique(total_list, return_counts = True)
            results = dict(zip(unique,counts))
            average_results = dict(zip(unique, counts/num_trials))
        #print (trial_result)
            #print (intersecttrial)
        print(trial_result)
print (results)
average_sorted = sorted(average_results.items(), key=operator.itemgetter(1),reverse=True)

#or a in average_sorted:
#   print (a, int(average_sorted[a]))
print (average_results)
print (average_sorted)
