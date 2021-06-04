#!/usr/bin/python
## Simple Python script designed to read a CSV file and write the values to the local Syslog file in CEF format.
## started with work from Frank Cardinale at https://www.frankcardinale.com/2020/04/27/script-to-read-from-csv-file-and-write-to-syslog-in-cef-format/

## Importing the libraries used in the script
import sys
import syslog
import csv

##check to see number of arguments and if less than 1 then print help
if len(sys.argv) < 2:
    print("This script requires the first argument.")
    print("python CsvCefConverter.py <template csv filename to read in> <cef filename to write to>")
    print("if cef filename is not provided then CefOutputFile.txt is used")
    exit()

##open csv file
with open(sys.argv[1]) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #loop through each row of csv
    if len(sys.argv) > 2:
        outputFile = open(sys.argv[2], 'w')
    else:
        outputFile = open('./CefOutputFile.txt', 'w')

    for row in readCSV:

        #skip first row
        if "DeviceVendor" not in row[0]:
        #Creating a value that will be used to write to the Syslog file. Rows added to applicable CEF fields.
            syslog_message = "CEF:0|" + row[0] + "|" + row[1] + "|" + row[29] + "|" + row[2] + "|" + row[30] + "|" + row[3] + "|msg=" + row[14]
            #Writing the event to flat file
            outputFile.write(syslog_message)
            outputFile.write("\n")
        
    outputFile.close()