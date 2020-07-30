"""
Author:      Roy Wu
Description: reading/parsing MS Excel sheet for further analysis, driver script
""" 
import helper
print("Program starts here...")

sourceFile  = '678-ORCRB-all sub-DataDownload-1'  #* source file name without extension .xlsx
sourceSheet = 'Original-DataDownload'   #* Excel sheet name
outputFile  = 'output'   #* output file name without .xlsx
meterRef    = '678113'   #* meter reference
sumIn24hr   = True       #* if True power is measured per hour; measured in per half hour if False
monthlySum  = False      #* if mothlySum is False, data will be listed daily

helper.sortByMeter(sourceFile, sourceSheet, meterRef, outputFile, sumIn24hr, monthlySum)