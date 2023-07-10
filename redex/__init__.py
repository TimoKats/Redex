__description__ = 'contains the basic functionalities of redex'
__filename__ = '__init__.py'
__author__ = 'Timo Kats'

# local imports

from redex.lexical_analysis import *
from redex.split import *

# main functionalities

def has(query, string, split=' ', granularity=1, threads=2) -> bool:
    search = RedexSearch(query, string, split=split, granularity=granularity, threads=threads)
    search.parse_query()
    if True in search.get_result():
        return True
    else:
        return False

def find(query, string, split=' ', granularity=1, format='string', threads=2) -> list:
    search = RedexSearch(query, string, split=split, granularity=granularity, threads=threads)
    search.parse_query()
    locations = []
    for index, location in enumerate(redex_split(string, split, granularity)):
        if search.get_result()[index] and format == 'int':
            locations.append(index)
        elif search.get_result()[index] and format == 'string':
            locations.append(location)
        elif search.get_result()[index] and format == 'tuple':
            locations.append((index, location))
    return locations

def count(query, string, split=' ', granularity=1, threads=2) -> int:
    search = RedexSearch(query, string, split=split, granularity=granularity, threads=threads)
    search.parse_query()
    count = 0
    for substring in search.get_result():
        if substring:
            count += 1
    return count

def info():
    print('\n')
    print('  ;,//;,    ,;/      Description:        Python library for readable regex.')
    print(' o:::::::;;///       Version:            1.0.1')
    print('>::::::::;;\\\\\\       Author:             Timo Kats')
    print('  "\\\\\\\\\\""  \';\      Last updated:       10/07/2023', end='\n\n\n')
