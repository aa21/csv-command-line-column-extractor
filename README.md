csv-command-line-column-extractor
=================================

Purpose of this script:
 - Quickly sample csv data from command line
 - Extract just a particular column to another file (or print to screen)

This script came about because I have hundreds of irregularly structured csv files and I need to extract just the postal code data from all of them. With this script I don't need to fire up Excel for each file. I can sample just the first few rows and columns (or more) and quickly dump the column I need to another file. 

There are two modes: Sampler mode and Regular mode. Sample mode is used to quickly get a sense of the file's structure and locate the column I'm looking for. Regular mode is used for printing specific column's data to screen or to write that column's data to a file.


1. <b>Sampler Mode - to get a sense of the column structure.</b> 

  <i>Arguments: fileName [t][cols][,rows]

  - <b>fileName</b>: can be relative file path also
  - <b>t</b>: triggers sample mode, by default dumps 5x5 data, column by column.
  - <b>cols</b>: sample more columns, default 5 - e.g t10 will dump data from first 10 columns
  - <b>rows</b>: sample more rows, default 5 - e.g t2,10 will dump 10 row data from first 2 columns

  <b>E.g See first 5 columns, sampling 5 rows for each</b>
  
    cli_csv.py orders.csv 
    
  <b>E.g See first 15 columns, sampling 5 rows for each</b>    
  
    cli_csv.py orders.csv t15
  
  <b>E.g See first 4 columns, sampling 15 rows for each</b>    
  
    cli_csv.py orders.csv t4,15



2. <b>Regular Mode</b>
  
  <i>Arguments: fileName, columnNumber [, write=p, delimiter=',', quotationSymbol='"']  

  - <b>fileName</b>: can be relative file path
  - <b>columnNumber</b>: starts from 0
  - <b>write</b>: Specifying 'w' will write to a new file, anything else will dump to screen
  - <b>delimiter</b>: Default is comma. Useful when you need to specify ';' etc
  - <b>quotationSymbol</b>: Default is double apostrophe ( " )
  

  <b>E.g To dump the third column's contents:</b>

    cli_csv.py orders.csv 2

  <b>E.g to write the contents of the first column to a new file:

    cli_csv.py orders.csv 0 w 

  <b>E.g specify ; as delimiter and | as quote character, and dump second col

    cli_csv.py orders.csv 2 p ';' '|'

  
