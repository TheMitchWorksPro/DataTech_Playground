#!/usr/bin/env python

"""
     Command Line tool to split a csv file
     Takes carguments from the command line.  For argument help use: python file_fragmenter.py --help
     Script will bring source CSV into Pandas Dataframe and use DF to ouput to smaller files
     Arguments include the ability to control how many rows are in the output files and whether or not 
     an index is desired

"""

import pandas as pd
import argparse
from abc import ABCMeta, abstractmethod

### object code

class CsvSplitterAbs(object, metaclass=ABCMeta):
    ## This object initialized from command line arguments when used in a Python script
    def __init__(self):
        ## parse named arguments from command line
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--input', '-i', help="intput file", type= str)
        self.parser.add_argument('--input_index', '-idx', help="enter true or false for has indes column", type=bool, default=False)
        self.parser.add_argument('--numRows', '-rw', help="number rows in each output file after splitting the intput file", type=int, default=1000)
        self.parser.add_argument('--outputStart', '-o', help="output file name starts with this string", type= str)
        self.parser.add_argument('--output_index', '-odx', help="enter true or false for whether to output an index column", type=bool, default=False)
        self.args=self.parser.parse_args()

        self.tmpDF = pd.DataFrame()   # holds entire input file when 
        self.tmpDF2 = pd.DataFrame()  # DF to get overwritten by each file fragment

    def split_file(self):
        ## input file controls:
        if self.args.input_index == True:
            tDF_index_col = 0      ## does input file have index column (with labels for each row)?
        else:
            tDF_index_col = False

        inFileToSplit = self.args.input
          ## Example: "TestFileSmall2.csv"

        ## output file controls
        numRows = self.args.numRows         ## 10  ##  10000                       ## rows to include in each subset
        fileStart = self.args.outputStart   ## "TestFlFrag"    #"tempSet"          ## file name for output (numbers and .csv for each file will be added by the code)
        tDF2_index_label = self.args.output_index                                  ## true outputs the index (row labels)

        self.tmpDF = pd.read_csv(inFileToSplit, 
                            index_col=tDF_index_col, low_memory=False) 
                             ## Your input file is brought into memory here

        ## process input file into correct number of output files
        rowCnt = len(self.tmpDF)
        print("Your file has ", str(rowCnt), " rows excluding the header row.")
        if tDF2_index_label == True:
            print("The DF Index will be output giving each data row a unique number starting at 0.") 
            print("To exclude these numbers, set index_labels to False (recommended if files will be imported to R).")

        dataSets = int(round(rowCnt/numRows,0))
        if dataSets * numRows < rowCnt:
            dataSets += 1

        print("Splitting source file into ", str(dataSets), " smaller files.")
        print("Please wait ...")
        limit = numRows
        innerStart = 0
        for i in range(0, dataSets): 
            filename = fileStart + str(i+1) + ".csv"
            print("Building File ", str(i+1), ": ", filename)
            # tmpDF2 = pd.DataFrame()  ## delete me after first successful test
            # print("Loop Range:", innerStart, ":", rowCnt)
            for j in range (innerStart, rowCnt):
                if j > innerStart and j % limit == 0:
                    # print("j: ", j)
                    innerStart = j
                    break 
                self.tmpDF2 = self.tmpDF2.append(self.tmpDF[j:j+1])

            self._changeOutFiles_()  ## abstract method footprint
                                     ## allows this code to be expanded to operate on each subfile ahead of output

            self.tmpDF2.to_csv(filename, index=tDF2_index_label)  # index_label
            self.tmpDF2 = pd.DataFrame()  ## teset tmpDF2 for next file
        print("Files Ready.")

    @abstractmethod
    def _changeOutFiles_(): pass

class CsvSplitter(CsvSplitterAbs):
    def __init__(self):           
        super().__init__()  

    def _changeOutFiles_(self): pass
        # in othe child objects, this function will operate on each subfile
        # ahead of creating the smaller output subfiles from the original input file.
        # this object just splits the CSV and does nothing special to the pieces. 

### actual script that uses the object code

def main():
    csvFileSplitter = CsvSplitter()
    csvFileSplitter.split_file()

if __name__ == '__main__':
    main()
