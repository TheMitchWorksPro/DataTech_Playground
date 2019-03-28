#!/usr/bin/env python
"""
    Fuse csv files into one single file.
"""

## file_fuser.py

### fuse individual files into one giant file
import pandas as pd 
import os
import argparse
from abc import ABCMeta, abstractmethod

class CsvFuserAbs(object, metaclass=ABCMeta):
    ## This object initialized from command line arguments when used in a Python script
    def __init__(self):
        ## parse named arguments from command line
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--inputStart', '-i', help="intput file name starting pattern (only files that match will be fused)", type=str)
        self.parser.add_argument('--input_index', '-idx', help="enter True if input has an index / Omit this argument if it doesn't", type=bool, default=False)
        self.parser.add_argument('--output', '-o', help="Name of final output file", type= str)
        self.parser.add_argument('--output_index', '-odx', help="enter true to output an index / Omit this argument to leave off the index", type=bool, default=False)
        self.parser.add_argument('--dir', '-d', help="input files directory", type= str, default=".")
        self.args=self.parser.parse_args()
        self.pyVer = "3.6.1"

        self.tmpDF = pd.DataFrame()   # holds entire input file when 
        self.tmpDF2 = pd.DataFrame()  # DF to get overwritten by each file fragment

    def fuse_files(self):
        fileStart = self.args.inputStart                   # start of filenames to fuse here (assumes all files have a pattern starting with this)
        outfilename = self.args.output                     # output file to merge files into
        path = self.args.dir                               # directory files are found in
        print("Input files will be located at: ", path)
        print("args.input_index is set to:", str(type(self.args.input_index)), self.args.input_index)
        print("args.output_index is set to:", str(type(self.args.output_index)), self.args.output_index)

        filesInDir = os.listdir(path)
        # print(type(filesInDir)) # is list
        filesInDir.sort()
        outDF = pd.DataFrame()
        tmpDF = pd.DataFrame()

        if self.args.input_index == True:
            df_input_indx = 0               ## if true - set index column number to index 0
        else:
            df_input_indx = False

        for name in filesInDir:
            if name[0:len(fileStart)] == fileStart:
                # print(name[0:len(fileStart)])
                # print(name)
                print("Adding This File To Output: ", name)
                tmpDF = pd.read_csv(name, index_col=df_input_indx)

                self._changeInputFiles_()  ## abstract method footprint
                                         ## allows this code to be expanded to operate on each subfile ahead of output

                outDF = outDF.append(tmpDF)
                tmpDF = pd.DataFrame()
        if self.args.input_index == False and self.args.output_index == True:
        	print("Creating Unique Index for Output File...")
        	outDF.reset_index(drop=True, inplace=True)
        	
        if self.args.output_index == False:
        	print("If the input files have an index, this will be dropped during output.")
        	outDF.to_csv(outfilename, index=False) 
        else:
        	if self.args.input_index == True and self.args.output_index == True:
        		print("The DF Index will be output giving each data row an index field value.")
        	outDF.sort_index(inplace=True)
        	outDF.to_csv(outfilename, index=self.args.output_index)
        print("Output File Created:  ", outfilename)

    @abstractmethod
    def _changeInputFiles_(): pass

    def codeVersion(self):
        print("This code was written in Python ", self.pyVer)

class CsvFuser(CsvFuserAbs):
    def __init__(self):           
        super().__init__()  

    def _changeInputFiles_(self): pass
        # in othe child objects, this function will operate on each input file
        # ahead of adding/merging them into the single output file
        # this object just merges the CSV and does nothing special to the inputs before merging.

### actual script that uses the object code

def main():
    csvFileFuser = CsvFuser()
    csvFileFuser.fuse_files()
    csvFileFuser.codeVersion()

if __name__ == '__main__':
    main()
