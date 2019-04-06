### About Python_Misc

This folder is evolving as a kind of subject within "DataTech_Playground".  Code here has the potential to be useful either as coding samples of more advanced concepts than found in "Python_Basic", or actual code and reusable code that can be a starting point for real pythonic solutions.

### Points of Interest
Points of interest and/or just some explanations of what is in here:

+ [/data/](./data/) - data used to test other code or referenced in notebooks in this folder
+ Working with CSVs (usually using Pandas)
  + [TMWP_DFBuilder_OO_PY/](./TMWP_DFBuilder_OO_PY/) - 
    + reusable objects for scanning a large data csv, and adding it to a dataframe a small number of rows at a time (saving the results as it builds)
    + child object using `requests` library to illustrate how this allows you to make web calls and not lose the results if an error is encountered while enriching a large CSV with data obtained from the web
  + [TMWP_CSV_Manipulation/](./TMWP_CSV_Manipulation/) - 
    + code to split a large CSV into smaller ones
    + code to fuse smaller csvs of a certain pattern into one large csv
    + all code is arranged in reusable objects and integrated into scripts that take command line arguments to run
  + __Files in The Root of this folder:__
    + [TMWP_Misc_Calculations.py](./TMWP_Misc_Calculations.py) - Misc. calculations organized in functions
    + [TMWP_OO_CustDataStructures.py](./TMWP_OO_CustDataStructures.py) - custom data structures (Ex: OrderedSet)
    + [TMWP_PY27_MagicSquaresTest.ipynb](./TMWP_PY27_MagicSquaresTest.ipynb) - Magic Squared Jupyter NB Demo
    + [TMWP_PY36_OO_Towers_of_Hanoi.ipynb](./TMWP_PY36_OO_Towers_of_Hanoi.ipynb) - Towers of Hanoii Jupyter NB Demo (includes example of recursive programming to solve the problem)
    + [TMWP_PY_FileDataObjects.ipynb](./TMWP_PY_FileDataObjects.ipynb) - Objects that manipulate a chatLog file; Parent object may have applications to manipulating other text based files; Child object illustrates how it could be used.
    + [TMWP_PY_NormDistrProb_Code.ipynb](./TMWP_PY_NormDistrProb_Code.ipynb) - Object to build a normal distribution from simple data; Organizes someone else's nice implementation into object code.
    + [TMWP_dictionary_manipulation.py](./TMWP_dictionary_manipulation.py) - functions for working with dictionaries
    + [TMWP_string_and_array_functions.py](./TMWP_string_and_array_functions.py) - code for manipulating strings and arrays; includes: code to convert a windows URL string to an online string, create a list of words from a string, and many more ...
