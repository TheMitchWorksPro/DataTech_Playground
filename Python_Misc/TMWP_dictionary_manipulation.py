#!/usr/bin/python
# Filename: TMWP_string_and_array_functions.py
#           TMWP = TheMitchWorksPro

# Functions and/or objects for smarter handling of common data structures
# this function is intended to have solutions for dictionaries, lists, numpy objects, etc.
# it may initially get pandas but as it grows those may separate out into their own module.

# source:  Multiple
# Written in Python 2.7 - should work in 3.x as well

# required imports are noted in the code where used/required
# from ... import ...

version = '0.1'
python_version_support = 'created in Python 2.7; should be compatible with 3.x'

def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    
    # source: 
    #   http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
    z = x.copy()
    z.update(y)
    return z

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts. 
    """
    # source: 
    #  http://stackoverflow.com/questions/38987/how-to-merge-two-python-dictionaries-in-a-single-expression
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def addToNestedDictionary(d, tup):
    '''This function adds a tupple to a dictionary by making it a nested dictionary.'''
    # source: http://stackoverflow.com/questions/8550912/python-dictionary-of-dictionaries
    if tup[0] not in d:
        d[tup[0]] = {}
    d[tup[0]][tup[1]] = tup[2]   # to embed in a list: [tup[2]]

def output_NestedDictSummary(nstdDict, descr1 = "People in the Chat Log", 
                                       descr2 = "People each sent this many messages",
                                       descr3 = "chat records"):
    '''Print summary of sub-dictionaries stored in Nested Dictionary.'''
    
    # Dictionary summarizes what?
    #   descr1, descr2, descr3 (for dictionary and subctionary records)
    #   test with default values to see how to use the arguments
    #   first used in sample code accompanying: FileDataObj
    
    print("Number of %s: %s" %(descr1, len(nstdDict)))
    print("%s:" %(descr2))

    for eachKey in nstdDict:
        outStr = eachKey + ": " + str(len(nstdDict[eachKey]))
        print("\t%s" %outStr)
    print("\tTotal: %d %s" %(sum(len(v) for v in nstdDict.values()), descr3))  # itervalues
