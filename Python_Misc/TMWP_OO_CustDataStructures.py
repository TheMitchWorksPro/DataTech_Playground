#!/usr/bin/python
# Filename: TMWP_OO_CustDataStructures.py
#           TMWP = TheMitchWorksPro

# Functions and/or Objects for smarter handling of common data structures
# required imports are noted in the code where used/required
# from ... import ...

version = '0.1'
python_version_support = 'code shoud be compatibile w/ Python 2.7 and Python 3.x'


import collections

class OrderedSet(collections.MutableSet):
    # source: https://code.activestate.com/recipes/576694/
	#         added to collection for testing but may or may not be tested yet
	#         notes say this was created for Python 2.6 but should be compatible w/ 2.7 and 3.x
	# Alternatives:  from sortedcontainers import SortedSet
	#                pip install sortedcontainers library to use it
	
	# libraries needed:  import collections
	
    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)