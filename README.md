# NameAnalysis

This is a simple script that goes through a plain text file and looks for names. 

You have to supply a namelist, but you an find them at places like [this](http://www.outpost9.com/files/WordLists.html)
or other places as recommended [here](http://stackoverflow.com/questions/1803628/raw-list-of-person-names).

To use, you need a few inputs:
    * A data file with text in it to search (``data.txt``)
    * A list of male names (``male-names``)
    * A list of female names (``female-names``)
    
Then just run the script. You'll see output of the top names for each section of text.

```
>>> python nameAnalysis.py
```
Enjoy. 
