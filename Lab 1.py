ATTRIBUTES = {
    'war': 0,
    'fly': 1,
    'ver': 2,
    'end': 3,
    'gro': 4,
    'hai': 5
}

DATA_SET = {
    "ant": [1, 1, 1, 1, 2, 1],
    "bee": [1, 2, 1, 1, 2, 2],
    "cat": [2, 1, 2, 1, 1, 2],
    "cpl": [1, 1, 1, 1, 1, 2],
    "chi": [2, 1, 2, 2, 2, 2],
    "cow": [2, 1, 2, 1, 2, 2],
    "duc": [2, 2, 2, 1, 2, 1],
    "eag": [2, 2, 2, 2, 1, 1],
    "ele": [2, 1, 2, 2, 2, 1],
    "fly": [1, 2, 1, 1, 1, 1],
    "fro": [1, 1, 2, 2, 'NA', 1],
    "her": [1, 1, 2, 1, 2, 1],
    "lio": [2, 1, 2, 'NA', 2, 2],
    "liz": [1, 1, 2, 1, 1, 1],
    "lob": [1, 1, 1, 1, 'NA', 1],
    "man": [2, 1, 2, 2, 2, 2],
    "rab": [2, 1, 2, 1, 2, 2],
    "sal": [1, 1, 2, 1, 'NA', 1],
    "spi": [1, 1, 1, 'NA', 1, 2],
    "wha": [2, 1, 2, 2, 2, 1],
}

n = len(DATA_SET)

oneFreq = [0]*6
twoFreq = [0]*6

for data in DATA_SET.values():
    for i in range(0, 6):
        if data[i] == 1:
            oneFreq[i] += 1
        elif data[i] == 2:
            twoFreq[i] += 1

print(oneFreq)
print(twoFreq)

PROCESSED_DATA = {}

for data in DATA_SET:
    PROCESSED_DATA[data] = [0] * 6
    for i in range(0, 6):
        if DATA_SET[data][i] == 'NA':
            if oneFreq[i] > twoFreq[i]:
                PROCESSED_DATA[data][i] = oneFreq[i]
            else:
                PROCESSED_DATA[data][i] = twoFreq[i]
print(PROCESSED_DATA)