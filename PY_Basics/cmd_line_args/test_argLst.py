
import argparse, sys
# source
#   https://stackoverflow.com/questions/40001892/reading-named-command-arguments
#     this script demonstrates a concept for how to pass arguments from command line
#     where each arg has a name and the user can then enter the named arguments in 
#     any order desired.  See test_argv1.py for demo of integrating with main()

# related resources:
#  https://docs.python.org/3.6/library/argparse.html?highlight=argparse#module-argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', '-f', help="a random options", type= str)
parser.add_argument('--bar', '-b', help="a more random option", type= int, default= 0)

print(parser.format_help())
# usage: test_args_4.py [-h] [--foo FOO] [--bar BAR]
# 
# optional arguments:
#   -h, --help         show this help message and exit
#   --foo FOO, -f FOO  a random options
#   --bar BAR, -b BAR  a more random option

args = parser.parse_args("--foo pouet".split())
print(args)      # Namespace(bar=0, foo='pouet')
print(args.foo)  # pouet
print(args.bar)  # 0