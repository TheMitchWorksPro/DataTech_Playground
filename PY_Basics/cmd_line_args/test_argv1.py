#!/usr/bin/env python
# source:
#   https://stackoverflow.com/a/17523836/7525365
#   simple demo of using argv to get arguments from command line
#   Note: user has to pass in args (un-named) in the right sequence 
#         to use a script that is built on this concept

import sys

def hello(v):
    print('hello '+ v)

def main(args):
	# demo using first arg
    hello(args[1])
    print(sys.argv)  # output all args passed

if __name__ == '__main__':
    main(sys.argv)