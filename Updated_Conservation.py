import numpy
import pandas as pd
import operator
from operator import itemgetter
import collections
from collections import OrderedDict

name_counts = []

num_trials = 20

print ('Loading overlaps.\n')
fc = open("4rand_avg_leukemia_conserve_average.txt", "w")
with open("3rand_leukemia_conserve_motif_overlap_filter.txt", "r") as o:
    overlaps = o.readlines()
    for line in overlaps:
        trial = line.split('\t')[0]
        name = line.split('\t')[1]
        conserve = line.split('\t')[2]
        trial_s = trial.split(':')
        name_s = name.split('_')
        conserve_s = conserve.split('\n')
        name_counts.append((str(trial_s[1]),name_s[0],conserve_s[0]))

print ('Loaded ' +str(len(overlaps))+' overlaps.')

for r in range(num_trials):
    gene_name = []
    gene_counts = []
    conserve_name = []
    conserve_value = []
    conserve_add = {}
    #conserve_avg = {}
    print ('Loading Genes.\n')
#     with open ("overlap_counts.txt", "r") as g:
#         genes = g.readlines()
#         for line in genes:
#             nameg = line.split(' ')[0]
#             value = line.split(' ')[1]
#             gene_name.append(nameg)
    print ('Running '+str(r+1)+' iteration.\n')
    fc.write ('\nRunning '+str(r+1)+' iteration.\n')
    
    
    print ('Getting names and conservation values')
    for trial_total in name_counts:
        if trial_total[0] == str(r+1):
            gene_name.append(trial_total[1])
            conserve_name.append(trial_total[1])
            conserve_value.append(trial_total[2])
    print ('success')
    print ('Names obtained: '+str(len(conserve_name)))
    print ('Values obtained: '+str(len(conserve_value)))
    
    print('Obtaining gene count from file')
    gene_conserve, gene_count = numpy.unique(conserve_name, return_counts= True)
    gene_results = dict(zip(gene_conserve, gene_count))
    #print (gene_results)
    
    print('\nSending lists created previously into dictionaries')
    conserve = dict(zip(conserve_name,conserve_value))
    print ('success')
    print('Grouping genes with conservation scores')
    for x, y in conserve.items():
        if x in conserve_add:
            conserve_add[x] = conserve_add[x] + float(str(y))
        else:
            conserve_add[x] = float(y)
    print ('success')
    
    print('\nSorting conservation scores alphabetically')
    conserve_sort = OrderedDict(sorted(conserve_add.items(), key=lambda t: t[0]))
    map(str, conserve_sort)
    print ('success')
    
    #print(conserve_add)
    print('\n')
    #print(conserve_sort)
    print('\n')
    average_conserve = {k: conserve_sort[k]/gene_results[k] for k in conserve_sort}
    print('averages of conservation total divided by number of hits\n')
    print (average_conserve)
#     fc_conserve = pd.DataFrame.from_dict([average_conserve], orient = 'index')
#     print (fc_conserve)
    #fc_conserve = "\n".join(str(s) for s in conserve_sort)
    #c = "\n".join(str(i) for i in protein_result)
    #print (*conserve_sort, sep= "\n")
    #fc.write(fc_conserve)
    print ('\nend iteration')
# df = pd.DataFrame({'gene': conserve_sort})
    df = pd.DataFrame({'gene': average_conserve})
    print (str(df))
    fc.write(df.to_string())
fc.close()
