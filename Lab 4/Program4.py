import pandas as pd

TRANSACTIONS = {}; #store information about transactions and unique items
UNIQUE_ITEMS = {};

MIN_SUPPORT_COUNT = 2;
CONFIDENCE = 0.5;


def removeChar(word, charToRemove):  # A function to remove specified characters from the beginning and end of a word
    while len(word) != 0 and word[0] == charToRemove:
        word = word[1:];

    while len(word) != 0 and word[-1] == charToRemove:
        word = word[0:len(word) - 1];

    return word;


def findFrequenctItems(filePath):     # A function to find frequent items in transactions and populate the TRANSACTIONS and UNIQUE_ITEMS dictionaries

    file = open(filePath, 'r');
    for line in file:
        transac = line.split(" ");
        TRANSACTIONS[transac[0]] = [];
        for item in transac[2].split(","):
            item = removeChar(item, '\n');
            TRANSACTIONS[transac[0]].append(item);
            if UNIQUE_ITEMS.get(item) == None:
                UNIQUE_ITEMS[item] = 1;


findFrequenctItems("Transactions.txt");
# print(TRANSACTIONS);
# print(UNIQUE_ITEMS);
UNIQUE_ITEMS_ARR = list(UNIQUE_ITEMS.keys());
# print(UNIQUE_ITEMS_ARR);


CANDIDATE_SETS = {}; #empty dictionary that will be used to store candidate itemsets generated during the Apriori algorithm process.


def findSupportCount(arr):     # A function to find the support count of an itemset in transactions
    count = 0;
    for transac in TRANSACTIONS:
        flag = True;
        for i in range(0, len(arr)):
            if (arr[i] not in TRANSACTIONS[transac]):
                flag = False;
                break;
        if (flag):
            count += 1;
    return count;


def findCandidateSet(indx, k, arr, c_index):     # Recursive function to generate candidate itemsets of size k using the Apriori algorithm
    #starts with an index indx, an empty array arr, and a candidate index c_index
    if (k == 0):
        if (CANDIDATE_SETS.get(c_index) == None):
            CANDIDATE_SETS[c_index] = {};
        str = " "
        CANDIDATE_SETS[c_index][str.join(arr)] = findSupportCount(arr);
        return;
    if (indx >= len(UNIQUE_ITEMS_ARR)):
        return;

    findCandidateSet(indx + 1, k, arr, c_index);
    arr.append(UNIQUE_ITEMS_ARR[indx]);
    findCandidateSet(indx + 1, k - 1, arr, c_index);
    arr.pop();


for i in range(1, len(UNIQUE_ITEMS_ARR) + 1): #This loop generates candidate itemsets of different sizes (i) using the findCandidateSet function.
    findCandidateSet(0, i, [], i);

VALID_CANDIDATE_SETS = {}; # empty dictionary that will be used to store valid candidate itemsets that meet the minimum support count.
# iterating  through the CANDIDATE_SETS dictionary to filter out valid candidate itemsets based on the minimum support count. The valid ones are stored in the VALID_CANDIDATE_SETS dictionary.
print("\n\n------------------------DICTIONARY FORMAT------------------------\n");
for i in CANDIDATE_SETS:
    for j in CANDIDATE_SETS[i]:
        if (CANDIDATE_SETS[i][j] >= MIN_SUPPORT_COUNT):
            if (VALID_CANDIDATE_SETS.get(i) == None):
                VALID_CANDIDATE_SETS[i] = {};
            VALID_CANDIDATE_SETS[i][j] = CANDIDATE_SETS[i][j];

    if (VALID_CANDIDATE_SETS.get(i) != None):
        print("Candidate Set", i, '\n', VALID_CANDIDATE_SETS[i]);

print("\n\n------------------------TABULAR FORMAT------------------------\n");
df = pd.DataFrame(VALID_CANDIDATE_SETS)
print(df)