csv-command-line-column-extractor
=================================

Purpose of this script:
 - Quickly sample csv data from command line
 - Extract just a particular column to another file (or print to screen)

This script came about because I have hundreds of irregularly structured csv files and I need to extract just the postal code data from all of them. With this script I don't need to fire up Excel for each file. I can sample just the first few rows and columns (or more) and quickly dump the column I need to another file. 

There are two modes: Sampler mode and Regular mode. Sample mode is used to quickly see what data is in each column. Regular mode is used for printing specific column's data to screen or to write that column's data to a file.


  1. <b>Regular Mode</b>
  
    <i>Arguments: fileName, columnNumber [, write=p, delimiter=',', quotationSymbol='"']  

  - <b>fileName</b>: can be relative file path
  - <b>columnNumber</b>: starts from 0
  - <b>write</b>: Specifying 'w' will write to a new file, anything else will dump to screen
  - <b>delimiter</b>: Default is comma. Useful when you need to specify ';' etc
  - <b>quotationSymbol</b>: Default is double apostrophe ( " )
  

  <b>E.g To dump the third column's contents:</b>

    cli_csv.py orders.csv 2

  <b>E.g to write the contents of the first column to a new file:

    cli_csv.py orders.csv 0 w ';' '"'

  
  2. <b>Sampler Mode</b> 
    <i>Arguments: fileName, t[cols][,rows]

  - <b>fileName</b>: can be relative file path also
  - <b>t</b>: triggers sample mode, dumps first 5 columns and first 5 rowdata for eachcolumn
  - <b>cols</b>: sample more columns, e.g t10 will dump data from first 10 columns
  - <b>rows</b>: sample more rows, e.g t2,10 will dump 10 row data from first 2 columns

