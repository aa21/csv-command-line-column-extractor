csv-command-line-column-extractor
=================================

Extract a single column from a csv file from command line using this script.

  Arguments:
   fileName, columnNumber [, write=p, delimiter=',', quotationSymbol='"']  

  - fileName: can be relative file path also
  - columnNumber: starts from 0
  - write: Specifying 'w' will write to a new file, anything else will dump to screen
  - delimiter: Default is comma. Useful when you need to specify ';' etc
  - quotationSymbol: Default is double apostrophe ( " )


  E.g

   cli_csv.py orders.csv 0 w ';' '"'

  to write the contents of the first column to a new file.
