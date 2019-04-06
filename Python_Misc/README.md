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
  + *Files in The Root of this folder:*
    + [TMWP_Misc_Calculations.py](./TMWP_Misc_Calculations.py) - Misc. calculations organized in functions
    + [TMWP_OO_CustDataStructures.py](./TMWP_OO_CustDataStructures.py) - custom data structures (Ex: OrderedSet)
