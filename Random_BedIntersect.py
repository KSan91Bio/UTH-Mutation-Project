import random
import numpy
import pybedtools
from pybedtools import BedTool

count_list = []

for r in range(2):
    random.seed()
    ran_pos = int(random.random()*2000 - 1000)
    with open("matchestest.txt", "r") as m:
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
            #feature_a = a[0]
            b = pybedtools.BedTool('cosmic.bed').sort()
            #feature_b = b[0]
            intersecttrial = (a.intersect(b, u=True, stream = True))
            #intersect_result = intersecttrial[0]
            #print (intersecttrial)
            #print (intersect)
            
            for current_region in intersecttrial:
                count_list.append(current_region.name)
            
        unique, counts =  numpy.unique(count_list, return_counts = True)
        results = dict(zip(unique,counts))
        print (results)
