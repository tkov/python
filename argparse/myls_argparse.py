# myls_argparse
# using the argparse library

import argparse

import os
import sys

# create the parser
my_parser = argparse.ArgumentParser(prog='myls', description='List the content of a folder')

# add the arguments
my_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to list')

# execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
