#!/usr/bin/python
## Simple Python script designed to read a CSV file and write the values to the local Syslog file in CEF format.
## started with work from Frank Cardinale at https://www.frankcardinale.com/2020/04/27/script-to-read-from-csv-file-and-write-to-syslog-in-cef-format/

## Importing the libraries used in the script
import syslog
import csv

##open csv file
with open('./testFile.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #loop through each row of csv
    outputFile = open('./CEFLogFile.txt', 'w')

    for row in readCSV:

        #skip first row
        if "DeviceVendor" not in row[0]:
        #Creating a value that will be used to write to the Syslog file. Rows added to applicable CEF fields.
            syslog_message = "CEF:0|" + row[0] + "|" + row[1] + "|" + row[29] + "|" + row[2] + "|" + row[30] + "|" + row[3] + "|msg=" + row[14]
            #Writing the event to flat file
            outputFile.write(syslog_message)
            outputFile.write("\n")
        
    outputFile.close()