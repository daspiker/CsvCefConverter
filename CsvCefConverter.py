#!/usr/bin/python
## Simple Python script designed to read a CSV file and write the values to the local Syslog file in CEF format.
## started with work from Frank Cardinale at https://www.frankcardinale.com/2020/04/27/script-to-read-from-csv-file-and-write-to-syslog-in-cef-format/

## Importing the libraries used in the script
import syslog
import csv

##open csv file
with open('./example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #loop through each row of csv
    for row in readCSV:

        #Creating a value that will be used to write to the Syslog file. Rows added to applicable CEF fields.
        syslog_message = "CEF:0|" + row[0] + "|" + row[1] + "|1.0|1000|ThreatIntelFeed|10|src=" + row[2]

        #Writing the event to flat file
        outputFile = open('./CEFLogFile.txt', 'w')
        outputFile.write(syslog_message)

    outputFile.close()