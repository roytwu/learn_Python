"""
Author:      Roy Wu
Description: reading/parsing MS Excel sheet for further analysis
""" 
import pandas as pd
import helper
print("Program starts here...")

sourceFile  = '678-ORCRB-all sub-DataDownload-1.xlsx'
sourceSheet = 'Original-DataDownload'
outputFile  = 'output.xlsx'
meterRef    = '678113'

helper.sortByMeter(sourceFile, sourceSheet, meterRef, outputFile)