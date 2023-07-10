__description__ = 'contains functions related to splitting the strings'
__filename__ = 'split.py'
__author__ = 'Timo Kats'

def redex_split(string, split, granularity=1):
    granularity_count = 0
    indices = [-1]
    for index, char in enumerate(string):
        for split_char in split:
            if split_char == char:
                granularity_count += 1
                if granularity_count % granularity == 0 or granularity_count == 0:
                    indices.append(index)
    return [string[i+1:j] for index, (i,j) in enumerate(zip(indices, indices[1:]+[None]))]
