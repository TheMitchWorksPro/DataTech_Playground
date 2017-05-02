#!/usr/bin/python
# Filename: TMWP_Misc_Calculations.py
#           TMWP = TheMitchWorksPro

# placeholder for notes
#
#
# Written in Python 2.7 - should work in 3.x as well

import math

def is_leap(year):
    '''is_leap()-->\n]nTests if a year is a leap year.  Accepts years like 1990 as input.'''
    # test if a year is a leap year 
    # dfinition of problem provided by hackerrank
    # https://www.timeanddate.com/date/leapyear.html
    
    if year % 400 == 0:
        # if divisible by 400 we know it is also divisible by 100
        return True
    elif year % 100 == 0:
        # divisible by 100 but not divisible by 400
        return False
    elif year % 4 == 0:
        # fails first two tests but is divisible by 4
        return True
    else:
        return False
 
def countPowOfNumInN(N, powNum):
    '''countPowOfNumInN()-->\n\nCounts the number of powers of powNum within any given number N.  
Examples: countPowOfNumInN(N, 10) Returns 2 for N=100 and for N=114. 0 for N=3 and N=7, and 1 for N=10 and N=13.'''
# import math                            # needed for log functions
def powOfTens(N):                        # find the powers of 10 inside a number
    if N < 1:
        N = 1                            # less than 1 would throw an error, this is a work-around based on
                                         # how this function is used in the code
            
    return int(math.log10(N))            # converts decimal to whole integer
                                         # int() rounds down no matter how big the decimal
                                         # note: math.log(x, 10) produces floating point rounding errors
	
def roundTraditional(val,digits):
   '''roundTraditional()-->\n\nWork-around for rounding bug that should work almost all the time.'''
   # source:  http://stackoverflow.com/a/38239574/7525365
    return round(val+10**(-len(str(val))-1))
   
def convertTemp(temperature, t_in='F', t_out='C'):
    if t_in == 'C' and t_out == 'F': 
	    return float(9)/5)*temperature + 32
	elif t_in == 'F' and t_out == 'C':
	    return float(5)/9)*(temperature-32)
	# future development:  add options for kelvin
	else:
	    raise ValueError("Incorrect Arguments for function convertTemp(temperature, t_in='F', t_out='C'")
