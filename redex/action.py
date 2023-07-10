__description__ = 'contains the actions that user can call in redex'
__filename__ = 'action.py'
__author__ = 'Timo Kats'

# local imports

from redex.wildcards import *

# helper functions

def is_in(char, string) -> bool:
    if char in wildcard.keys():
        for wchar in wildcard[char]:
            if wchar in string:
                return True
    else:
        return char in string
    
def is_in_end(char, string) -> bool:
    if char in wildcard.keys():
        for wchar in wildcard[char]:
            if wchar == string[-1]:
                return True
    else:
        return char == string

def is_in_start(char, string) -> bool:
    if char in wildcard.keys():
        for wchar in wildcard[char]:
            if wchar == string[0]:
                return True
    else:
        return char == string

# actions

def startswith(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    return is_in_start(sub_query, string[:len(sub_query)])

def endswith(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    return is_in_end(sub_query, string[-len(sub_query):])

def contains(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    return is_in(sub_query, string)

def count(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    char = list(sub_query[1:-1].split(','))[0]
    threshold = int(list(sub_query[1:-1].split(','))[1])
    count = 0
    if char in wildcard.keys():
        for wchar in wildcard[char]:
            count += string.count(wchar)
    else:
        count = string.count(char)
    return count >= threshold

def proximity(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    char_set = list(sub_query.split('}')[0][1:].split(','))
    threshold = int(sub_query.split('}')[1])
    max_proximity = -1
    for char in char_set:
        proximity = abs(string.find(char) - string.find(char_set[0]))
        if is_in(char, string) and (max_proximity < proximity or max_proximity == -1):
            max_proximity = proximity
        if not is_in(char, string):
            return False
    return max_proximity <= threshold and max_proximity != -1

def sequence(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    sequence_list = list(sub_query[1:-1].split(','))
    current_index = 0
    for char in string:
        if is_in(sequence_list[current_index], char) and current_index < len(sequence_list) - 1:
            current_index += 1
        if not is_in(sequence_list[current_index], string):
            return False
    return current_index == len(sequence_list) - 1

def location(sub_query, string) -> bool:
    sub_query = sub_query.split(':')[1]
    char = list(sub_query[1:-1].split(','))[0]
    location = int(list(sub_query[1:-1].split(','))[1])    
    if location < len(string) - 1:
        return is_in(char, string[location])
    else:
        return False

