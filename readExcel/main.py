"""
Author:      Roy Wu
Description: reading/parsing MS Excel sheet for further analysis
"""

import numpy as np   
import pandas as pd
print("Program starts here...")

#*  ----- -----
# #* read Excel sheet
# data = pd.read_excel (r'678-ORCRB-all sub-DataDownload-1.xlsx', sheet_name='Original-DataDownload')
# #* print out the entire column
# df = pd.DataFrame(data, columns=['Site Code'])
# #print (df)


#*  ----- ----- 
# data = pd.read_excel (r'678-ORCRB-all sub-DataDownload-1.xlsx', sheet_name='Original-DataDownload', 
#                        index_col="Meter Reference")
# foo = data["Date"]
# print(foo)

# row0 = data.iloc[0]  #*access the 0-st row
# print(row0)

# #* covert data frame to Python list
# outputList = row0.values.tolist()
# print (outputList)

#*  ----- -----
data = pd.read_excel (r'678-ORCRB-all sub-DataDownload-1.xlsx', sheet_name='Original-DataDownload')
gp1=data.groupby('Meter Reference')
output = gp1.first()
output.to_excel("output.xlsx")
