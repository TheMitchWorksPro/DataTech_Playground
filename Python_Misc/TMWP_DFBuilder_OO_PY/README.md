# About This Code
These class objects were created to extract information into a Dataframe using the Google Maps API. Initially, this was part of an effort to operationalize the interesting bits of code in a messy procedure I did for some research. The original use case was to extract just the address and add it to tables of information with latitude and longitude in them. The class heirarchy supports expansion to address future more complex use cases and even subclassing with different APIs.

## DFBuilder Abstract Class
The purpose of the <b><font color="blue">DFBuilder</font></b> object is to allow scanning of a larger dataframe, a small number of rows at a time. It then allows code to be customized to make changes and build up a new dataframe from the results. The operation is in a standard loop by design. The original use case was to add a field with data accessed from an API off the web, and time delays were necessary (as well as other logic) to prevent (or at least reduce the risk of) server timeouts during operation.

Scanning through the source a few lines at a time, performing the operation and adding back out to the target DF creates a "caching effect" where data is saved along the way so in the event of a server time-out all is not lost. The resulting DF can then be saved out to a file and a rerun of <font color="blue"><b>buildOutDF()</b></font> should make it possible to pick up where you left off and add in more data (instead of losing everything and having to begin again).

## GMapsLoc_DFBuilder Subclass
The abstract class is intended to be the "work horse" of this code. Intent is that it gets the developer to the point where all they need to think about is what their final subclass will do to enrich the data. The parent class sets up a loop that can extract from a larger input DF, a small number of rows to be operated on in a temp DF and then be added to an outputDF. In the event of something interrupting the process (a common event when dealing with web APIs), modified rows created before the incident are waiting in output DF and can be extracted. Then code can be restarted or continued to allow building up the rest of the Dataframe without losing previous work or having to go all the way back to the beginning.

The abstract class sets up the core logic and subclasses add in functions to modify the data in different ways and potentially using different APIs. This notebook only tests the subclass designed for the Google Maps API.  Some configuration logic, where it needs to interact with new variables or methods introduced by the subclass may also be contained within it.  Any configuration details which can be specified at the parent level are included there.

## More Documentation, Examples and Testing
Final test Jupyter notebooks have been edited to show examples of how to use the classes and their methods.  This content is chock full of examples while showing the final tests that verify the code works.  This content displays better in Jupyter Notebooks than on Git due to wider display margins. But you can view this content here, or download it for use:

- [Testing_and_Documentation](https://github.com/TheMitchWorksPro/DataTech_Playground/blob/master/Python_Misc/TMWP_DFBuilder_OO_PY/testing_and_documentation)
- [Test Data](https://github.com/TheMitchWorksPro/DataTech_Playground/blob/master/Python_Misc/TMWP_DFBuilder_OO_PY/testing_and_documentation/data)





