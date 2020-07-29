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

#*  ----- group data by date -----
data = pd.read_excel (r'678-ORCRB-all sub-DataDownload-1.xlsx', sheet_name='Original-DataDownload')
data.index = pd.to_datetime(data['Date'], format='%m/%d/%y')
gp1=data.groupby(by=[data.index.month, data.index.year])
#gp1=data.groupby(by=[data.index.month])

output=gp1.sum()  #sum all entries in group, from beginning of the month to the end of the month
output.to_excel("output.xlsx")
# with pd.ExcelWriter('output.xlsx') as writer:  
#     for row, group in gp1:
#         group.to_excel(writer, sheet_name=row)



# gp1=data.groupby('Meter Reference')
# output = gp1.first() #* group all the 1ist entries to a data frame
# output.to_excel("output.xlsx")
