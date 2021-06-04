#!/usr/bin/python
## Simple Python script designed to read a CSV file and write the values to the local Syslog file in CEF format.
## started with work from Frank Cardinale at https://www.frankcardinale.com/2020/04/27/script-to-read-from-csv-file-and-write-to-syslog-in-cef-format/

## Importing the libraries used in the script
import sys
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
            syslog_message = "CEF:0|" + row[0] + "|" + row[1] + "|" + row[29] + "|" + row[2] + "|" + row[30] + "|" + row[3] + "|" + " act=" + row[5] + " Host=" + row[7] + " deviceDirection=" + row[8] + " deviceFacility=" + row[9] + " dpt=" + row[10] + " dst=" + row[11] + " dvc=" + row[12] + " dvchost=" + row[13] + " msg=" + row[14] + " proto=" + row[15] + " spt=" + row[16] + " src=" + row[17] + " Name=" + row[30] + " app=" + row[31] + " cnt=" + row[32] + " destinationDnsDomain=" + row[33] + " destinationServiceName=" + row[34] + " destinationTranslatedAddress=" + row[35] + " destinationTranslatedPort=" + row[36] + " deviceDnsDomain=" + row[37] + " deviceExternalID=" + row[38] + " deviceInboundInterface=" + row[39] + " deviceNtDomain=" + row[40] + " deviceOutboundInterface=" + row[41] + " devicePayloadId=" + row[42] + " deviceProcessName=" + row[43] + " deviceTranslatedAddress=" + row[44] + " dhost=" + row[45] + " dmac=" + row[46] + " dntdom=" + row[47] + " dpid=" + row[48] + " dpriv=" + row[49] + " dproc=" + row[50] + " dtz=" + row[51] + " duid=" + row[52] + " duser=" + row[53] + " dvcmac=" + row[54] + " dvcpid=" + row[55] + " externalId=" + row[56] + " fileCreateTime=" + row[57] + " fileHash=" + row[58] + " fileId=" + row[59] + " fileModificationTime=" + row[60] + " filePath=" + row[61] + " filePermission=" + row[62] + " fileType=" + row[63] + " fname=" + row[64] + " fsize=" + row[65] + " in=" + row[66] + " oldFileCreateTime=" + row[67] + " oldFileHash=" + row[68] + " oldFileId=" + row[69] + " oldFileModificationTime=" + row[70] + " oldFileName=" + row[71] + " oldFilePath=" + row[72] + " oldFilePermission=" + row[73] + " oldFileSize=" + row[74] + " oldFileType=" + row[75] + " out=" + row[76] + " Request=" + row[77] + " requestClientApplication=" + row[78] + " requestContext=" + row[79] + " requestCookies=" + row[80] + " requestMethod=" + row[81] + " shost=" + row[82] + " smac=" + row[83] + " sntdom=" + row[84] + " sourceDnsDomain=" + row[85] + " sourceServiceName=" + row[86] + " sourceTranslatedAddress=" + row[87] + " sourceTranslatedPort=" + row[88] + " spid=" + row[89] + " spriv=" + row[90] + " sproc=" + row[91] + " suid=" + row[92] + " suser=" + row[93] + " type=" + row[94] + " c6a1=" + row[95] + " c6a1Label=" + row[96] + " c6a2=" + row[97] + " c6a2Label=" + row[98] + " c6a3=" + row[99] + " c6a3Label=" + row[100] + " c6a4=" + row[101] + " c6a4Label=" + row[102] + " cfp1=" + row[103] + " cfp1Label=" + row[104] + " cfp2=" + row[105] + " cfp2Label=" + row[106] + " cfp3=" + row[107] + " cfp3Label=" + row[108] + " cfp4=" + row[109] + " cfp4Label=" + row[110] + " cn1=" + row[111] + " cn1Label=" + row[112] + " cn2=" + row[113] + " cn2Label=" + row[114] + " cn3=" + row[115] + " cn3Label=" + row[116] + " cs1=" + row[117] + " cs1Label=" + row[118] + " cs2=" + row[119] + " cs2Label=" + row[120] + " cs3=" + row[121] + " cs3Label=" + row[122] + " cs4=" + row[123] + " cs4Label=" + row[124] + " cs5=" + row[125] + " cs5Label=" + row[126] + " cs6=" + row[127] + " cs6Label=" + row[128] + " deviceCustomDate1=" + row[129] + " deviceCustomDate1Label=" + row[130] + " deviceCustomDate2=" + row[131] + " deviceCustomDate2Label=" + row[132] + " flexDate1=" + row[133] + " flexDate1Label=" + row[134] + " flexNumber1=" + row[135] + " flexNumber1Label=" + row[136] + " flexNumber2=" + row[137] + " flexNumber2Label=" + row[138] + " flexString1=" + row[139] + " flexString1Label=" + row[140] + " flexString2=" + row[141] + " flexString2Label=" + row[142]
            #syslog_message = "CEF:0|" + row[0] + "|" + row[1] + "|" + row[29] + "|" + row[2] + "|" + row[30] + "|" + row[3] + "|msg=" + row[14]
            #Writing the event to flat file
            outputFile.write(syslog_message)
            outputFile.write("\n")
        
    outputFile.close()