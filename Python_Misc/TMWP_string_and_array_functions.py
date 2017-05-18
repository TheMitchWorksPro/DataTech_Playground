#!/usr/bin/python
# Filename: TMWP_string_and_array_functions.py
#           TMWP = TheMitchWorksPro

# string and array manipulation functions for demo, learning, and practical usage
# array = lists, dictionaries (associative arrays), and other array-like constructs of python
# source:  Multiple
# Written in Python 2.7 - should work in 3.x as well

# required imports are noted in the code where used/required
from collections import Counter
import itertools

# future development notes:
# * string.count() => takes 1 arg & counts # of specified character or string
#                len(string) => counts chars in a string, 
#                               and elements in a list, tuple, dictionary, etc.

version = '0.1'
python_version_support = 'created in Python 2.7; should be compatible with 3.x'

# This section:  source = https://learnpythonthehardway.org/book/ex25.html

def string_to_words_list(myString):
    """This function will split a string into a list of its component words."""
    words = myString.split(' ')
    return words

def sort_words_list(words):
    """Sorts the words in a list of words.  
	   Could receive output of string_to_word_list()."""
    return sorted(words)

def print_first_word_in_list(words):
    """Prints the first word after popping it off a list of words."""
    word = words.pop(0)
    print(word)

def print_last_word_in_list(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = string_to_words_list(sentence)
    return sort_words(words)

def print_first_and_last_words_of_sentence(sentence):
    """Prints the first and last words of the sentence."""
    words = string_to_words_list(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_words_of_sorted_sentence(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# this section developed from: 
#      https://www.codementor.io/python/tutorial/python-tricks-for-beginners

def reverse_string(inputString):
    """Reverses a string."""
    return inputString[::-1]

def isAnagram(str1, str2):
     """Tests if two strings are an anagram or not returning True/False."""
     # moved to top of module: from collections import Counter
     return Counter(str1) == Counter(str2)

def convert_stringOfInts_to_list(inputStr):
    """Takes string like '1 2 3 4' and converts it to [1, 2, 3, 4]"""
    return map(lambda x:int(x), inputStr.split())

def flatten_simple_nested_list(nestedList):
    # requires: import itertools
    """Takes a simple nested list like [[1,2],[3,4],[5,6]] and 
	   flattens it to [1, 2, 3, 4, 5, 6]"""
    return list(itertools.chain.from_iterable(nestedList))	 
	 
# This section:  source = TheMitchWorksPro (me)

def isPalindrome(inputString):
    """Calls reverse_string & uses it to tests if a string is a Palindrome.  
	   Returns True/False."""
    reversed_string = reverse_string(inputString)
    return reversed_string == inputString

# alternative to above function from Stack Overflow:

def is_palindromic(s):
    """Another way to test if a string is a Palindrome using tilde (not) operator 
	   source: http://stackoverflow.com/questions/8305199/the-tilde-operator-in-python  
	"""
    return all(s[i] == s[~i] for i in range(len(s) / 2))
	
def initialCaps_anyString(myString):
    """Makes first letter of all words in a string upper case 
	   (sometimes called camel case)."""
    
    textList = myString.split(" ")
    myString = ""
    
    for i in range(len(textList)):
        textList[i] = textList[i].capitalize()
        myString = myString + textList[i] + ' '
		# note: python loops don't need last line of i += 1
    
    # above logic adds ' ' to end of textList.  
	# This line removes it before returning the result:
    myString = myString[:-1]
    
    return myString

def convert_win_path_to_bashPath(inputURL):
    return inputURL.replace("\\", "/")
	
# More Mitch additions (testing different code functions)

def print_ArrayElements(myArray):
    count = 0
    for i in elements:
        try:
            count += 1
            print "Element %d: %d" % (count, i)
        except TypeError:
            # element was counted before error thrown
            print "Element %d: %s" % (count, i)

			
def convert_win_path_to_onlinePath(inputURL):
    '''convert windows file path string to browser or UNIX compatible syntax.'''
    return inputURL.replace("\\", "/")
	
# Related research:
#   https://www.tutorialspoint.com/python/string_join.htm	
#   https://wiki.python.org/moin/PythonSpeed/PerformanceTips#String_Concatenation
