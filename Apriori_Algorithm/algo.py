import pandas as pd #helps in data manipulation
import numpy as np  #helps to perform mathematical operations
from itertools import combinations  # generate combinations of items in the candidate sets.

df = pd.read_csv("dataset.csv", header=None) #Read the CSV file into a Pandas DataFrame

candidate_set = []
frequent_set = []
items = pd.unique(df.values.ravel('K')) #traversing the df values in order they occur in memory(k)
items = items[~pd.isnull(items)]  #an array containing all unique items found in the transactions.

#take minimum support from the user
min_support = int(input("+ Enter absolute value of minimum support:"))

for i in range(1,len(items)):
    count = {}  #Initialize a dictionary to count itemset occurrences and a list to store itemsets in the process
    in_Process = []

    if i==1:
        candidate_set.append(items)
        for txn in candidate_set[i-1]:
            ctr=0
            for val in df.values:
                if txn in val:
                    ctr+=1
            count[txn] = ctr  #counts the occurrences of each candidate itemset in the transactions and stores the counts in the count dictionary.
    else:
        candidate_set.append(list(combinations(np.unique(np.array(frequent_set[i-2]).ravel('K')),i))) #candidate itemsets by taking combinations of items from the previous frequent itemsets.
#np.unique and ravel('K') are used to ensure unique items in combinations.
        for txn in candidate_set[i-1]:
            ctr = 0
            for val in df.values:
                if all(i in val for i in txn):
                    ctr+=1
            count[txn] = ctr   #counts the occurrences of each candidate itemset in the transactions and stores the counts in the count dictionary.

    for k in count.keys():
        if count[k]>=min_support:
            in_Process.append(k) #checks if each candidate itemset meets the minimum support threshold and adds those itemsets to in_Process.

    if in_Process == []:
        print("+ Frequency Set =", frequent_set)
        break #If in_Process is empty, it means no frequent itemsets were found in the current iteration, and the loop terminates.

    frequent_set.append(in_Process)