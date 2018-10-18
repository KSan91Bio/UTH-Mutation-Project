import random
import numpy
import pybedtools
from pybedtools import BedTool

count_list = []
total_list = []
average_list = []
b = pybedtools.BedTool('cosmicchr1.bed').sort()

for r in range(2):
    trial_list = []
    random.seed()
    ran_pos = int(random.random()*2000 - 1000)
    with open("matchestest1.txt", "r") as m:
        matches = m.readlines()
        for line in matches:
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
                #if (r == 2):
                    #average_list.append(trial_total.name) 
            trial_unique, trial_counts = numpy.unique(trial_list, return_counts = True)
            trial_result = dict(zip(trial_unique, trial_counts))
            unique, counts =  numpy.unique(total_list, return_counts = True)
            results = dict(zip(unique,counts))
            #average_unique, average_counts = numpy.unique(average_list, return_counts = True)
            #average_results = dict(zip(average_unique, average_counts / r))
        #print (trial_result)
            #print (intersecttrial)
    #if r == 2:
        #for average_total in results:
            #aver = average_list.append[average_total] / r
            #average_unique, average_counts = numpy.unique(average_total, return_counts = True)
            #grand = dict(zip(average_unique,average_counts))
                #average = results.append(total_list()/len(r))
        
        print(trial_result)
#print (average_result)
print (results)
#print (average_results)
