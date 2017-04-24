This demo is mostly screen dumps from a command line test in which the python module "string_and_array_functions.py"
is set up so its functions become callable within the active Python environment.  Note that this configuration, if
re-created, makes the functions available all the time (is is for a permanent setup).  Though the test was done at
the command line, it was to set the module up to work with an Anaconda distribution if Jupyter/iPython. 
<br/>
The example includes how to give the user a version #.  This help topic is useful for making modules and 
setting up the version #:<br/>
<br/>
https://www.ibiblio.org/g2swap/byteofpython/read/making-modules.html<br/>
<br/>
This topic for making modules permanently accessible by your environment:<br/>
http://stackoverflow.com/questions/7472436/add-a-directory-to-python-sys-path-so-that-its-included-each-time-i-use-python<br/>
<br/>

Sample from Windows Powershell window - 1/9/2017:<br/>
<br/>
<style>
pre{
    background-color: #EBECE4; 
} 
</style>
<pre>
PS C:\Users\TMWP\...full path...\ModulesDir> python
Python 2.7.13 |Anaconda custom (64-bit)| (default, Dec 19 2016, 13:29:36) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org

>>> import sys

>>> sys.path.append(r'C:...\Python\Jupyter_NBs\a_GitProjx\Python_in_Plain_English')

>>> import string_and_array_functions as myFun

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'myFun', 'sys']

>>> dir(myFun)
['Counter', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'convert_stringOfInts_to_list', 'convert_w
in_path_to_onlinePath', 'flatten_simple_nested_list', 'initialCaps_anyString', 'isAnagram', 'isPalindrome', 'itertools',
 'print_first_and_last', 'print_first_and_last_sorted', 'print_first_word', 'print_last_word', 'reverse_string', 'sort_s
entence', 'sort_words', 'string_to_word_list', 'version']

>>> print myFun.version
0.1

>>> print myFun.string_to_word_list("This is a test")
['This', 'is', 'a', 'test']

>>> words =  myFun.string_to_word_list("Do not go gentle into that good night.")

>>> print words[2:4]
['go', 'gentle'] 
</pre>