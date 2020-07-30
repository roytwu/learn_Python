"""
Author:      Roy Wu
Description: helper functions
"""
import pandas as pd


def sortByMeter(fileName, sheetName, meterRef, outputFileName):
    #* read Excel file
    data = pd.read_excel (fileName, sheet_name=sheetName)
    
    #* indexing
    data.index = pd.to_datetime(data['Date'], format='%m/%d/%y')
    gp1=data.groupby(by=['Meter Reference', data.index.year, data.index.month, data.index.day], sort=False)
    output=gp1.sum()  #*sum all entries in group, from beginning of the month to the end of the month
    
    #* extract a particualr row
    output = output.loc[int(meterRef)]
    
    print(list(output))
    output['0-1'] = output[output.columns[2]] + output[output.columns[3]] 
    output['1-2'] = output[output.columns[4]] + output[output.columns[5]] 
    output['2-3'] = output[output.columns[6]] + output[output.columns[7]] 
    output['3-4'] = output[output.columns[8]] + output[output.columns[9]] 
    output['4-5'] = output[output.columns[10]] + output[output.columns[11]] 
    output['5-6'] = output[output.columns[12]] + output[output.columns[13]] 
    output['6-7'] = output[output.columns[14]] + output[output.columns[15]] 
    output['7-8'] = output[output.columns[16]] + output[output.columns[17]] 
    output['8-9'] = output[output.columns[18]] + output[output.columns[19]] 
    output['9-10'] = output[output.columns[20]] + output[output.columns[21]] 
    output['10-11'] = output[output.columns[22]] + output[output.columns[23]] 
    output['11-12'] = output[output.columns[24]] + output[output.columns[25]] 
    output['12-13'] = output[output.columns[26]] + output[output.columns[27]] 
    output['13-14'] = output[output.columns[28]] + output[output.columns[29]] 
    output['14-15'] = output[output.columns[30]] + output[output.columns[31]] 
    output['15-16'] = output[output.columns[32]] + output[output.columns[33]] 
    output['16-17'] = output[output.columns[34]] + output[output.columns[35]] 
    output['17-18'] = output[output.columns[36]] + output[output.columns[37]] 
    output['18-19'] = output[output.columns[38]] + output[output.columns[39]] 
    output['19-20'] = output[output.columns[40]] + output[output.columns[41]] 
    output['20-21'] = output[output.columns[42]] + output[output.columns[43]] 
    output['21-22'] = output[output.columns[44]] + output[output.columns[45]] 
    output['22-23'] = output[output.columns[46]] + output[output.columns[47]] 
    output['23-0'] = output[output.columns[48]] + output[output.columns[49]] 
    
    #* remove all columns between index 1 to 50
    output.drop(output.iloc[:, 1:50], axis = 1, inplace = True) 
    
    
   
    
    #* output Excel file
    output.to_excel(outputFileName+"_"+meterRef)