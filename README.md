# CsvCefConverter

This script takes in a csv file and outputs a cef encoded log file.  
The idea is that you take the template.csv and file out the fields that you want in your cef log.  you can have as many lines as you want.  
the script reads this in and translates this input into a multiline text file that has one log per line with the columns of the template translated int the appropriate cef fields and extensions

this script does not look for characters that need to be escaped so be careful to check for these.  see page 8 of this doc but summary is |, \ and = will need to be escaped with a \
https://www.secef.net/wp-content/uploads/sites/10/2017/04/CommonEventFormatv23.pdf
