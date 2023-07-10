__description__ = 'parses redex queries and calls the actions'
__filename__ = 'lexical_analysis.py'
__author__ = 'Timo Kats'

# libraries

from multiprocessing import Pool
from itertools import repeat

# local imports

from redex.action import *
from redex.split import *

class RedexSearch:
    def __init__(self, query, string, split, granularity, threads=2):
        self.subqueries = self.extract_subqueries(query)
        self.query = query
        self.string = string
        self.split = split
        self.granularity = granularity
        self.threads = threads
        self.results = []

    def extract_subqueries(self, query):
        query = query.replace('(',' ').replace(')', ' ').replace(' ','  ')
        query_new = query.split(' ')
        return [x for x in query_new if len(x) > 3]

    def parse_query(self):
        for sub_string in redex_split(self.string, self.split, self.granularity):
            sub_result = {}
            with Pool(self.threads) as p:
                sub_result = p.starmap(self.parse_subquery, zip(self.subqueries, repeat(sub_string)))
            self.results.append(sub_result)

    def parse_subquery(self, sub_query, sub_string):
        if 'startswith' in sub_query:
            return sub_query, startswith(sub_query, sub_string)
        elif 'endswith' in sub_query:
            return sub_query, endswith(sub_query, sub_string)
        elif 'contains' in sub_query:
            return sub_query, contains(sub_query, sub_string)
        elif 'proximity' in sub_query:
            return sub_query, proximity(sub_query, sub_string)
        elif 'sequence' in sub_query:
            return sub_query, sequence(sub_query, sub_string)
        elif 'location' in sub_query:
            return sub_query, location(sub_query, sub_string)
        elif 'count' in sub_query:
            return sub_query, count(sub_query, sub_string)

    def get_result(self):
        final_result = []
        for result in self.results:
            copy_query = self.query
            for sub_result in result:
                copy_query = copy_query.replace(sub_result[0], str(sub_result[1]))
            final_result.append(eval(copy_query))
        return final_result
