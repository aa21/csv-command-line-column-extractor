csv-command-line-column-extractor
=================================

Extract a single column from a csv file from command line using this script.

  Arguments:
  
    fileName, columnNumber [, write=p, delimiter=',', quotationSymbol='"']  

  - <b>fileName</b>: can be relative file path also
  - <b>columnNumber</b>: starts from 0
  - <b>write</b>: Specifying 'w' will write to a new file, anything else will dump to screen
  - <b>delimiter</b>: Default is comma. Useful when you need to specify ';' etc
  - <b>quotationSymbol</b>: Default is double apostrophe ( " )


<b>E.g To dump the third column's contents:</b>

    cli_csv.py orders.csv 2


<b>E.g to write the contents of the first column to a new file:

    cli_csv.py orders.csv 0 w ';' '"'

  
