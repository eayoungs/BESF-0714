import sys
import pprint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'

pathnameto_eppy = '/Users/eayoungs/repo/Code/Simulation_Tools/Scripting/eppy/eppy'
sys.path.append(pathnameto_eppy)

from eppy import readhtml
iddfile = "/Users/eayoungs/Dropbox/SHARE/BSUG/Energy+.idd"

#IDF.setiddname(iddfile) # This only needs to be run the first time through

#=======================================================================================================================

htmlDoc = open('/Users/eayoungs/Dropbox/SHARE/BSUG/FinalModels/BaselineTable.html', 'r')
htmlContents = htmlDoc.read()
linesTable = readhtml.lines_table(htmlContents, True)

pp = pprint.PrettyPrinter(indent=4)

reportDict = {}
tableDict = {}
tableContents =[]
for i in range(len(linesTable)):
    reportHeader = linesTable[i][0]
    if any("Report: " in s for s in reportHeader):
        reportLst = [s for s in reportHeader if "Report: "]
        reportName = reportLst[0]
        tableName = reportHeader[len(reportHeader)-1]
        tableContents = linesTable[i][1]
        
        tableDict[tableName] = tableContents
        #reportDict[reportName] = tableDict
        
    else:
        tableName = reportHeader[0]
        tableContents = linesTable[i][1]
        
        tableDict[tableName] = tableContents
        #reportDict[reportName] = tableDict

#-----------------------------------------------------------------------------------------------------------------------
        
tblNm = "End Uses"
tbl = tableDict[tblNm]

tblCols = tbl[0]

i=0
tblArray = []
tblRows = []
maxRow = []
while i < len(tbl[1:]):
    if all(isinstance(x, float) for x in tbl[1:][i][1:]):
        tblArray.append(tbl[1:][i][1:])
        tblRows.append(tbl[1:][i][0])
        maxRow.append(max(tbl[1:][i][1:]))
    i = i + 1
    
#=======================================================================================================================

print tblNm
print tblCols
pp.pprint(tblRows)
pp.pprint(tblArray)

#-----------------------------------------------------------------------------------------------------------------------

%matplotlib inline
N = 6
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, tblArray[0], width, color='r')
p2 = plt.bar(ind, tblArray[1], width, color='g')
p3 = plt.bar(ind, tblArray[2], width, color='b')
p4 = plt.bar(ind, tblArray[3], width, color='r')
p5 = plt.bar(ind, tblArray[4], width, color='g')
p6 = plt.bar(ind, tblArray[5], width, color='b', bottom=tblArray[0])

plt.ylabel('Watts')
plt.title(tblNm)
maxY = round(max(maxRow),1000)
plt.xticks(ind+width/2., ('G1', 'G2'), rotation='vertical')
plt.yticks(np.arange(0,maxY,maxY/10))
plt.legend((p1[0], p2[0]), p3[0], p4[0], p5[0], p6[0] (tblCols[0], tblCols[1], tblCols[2], tblCols[3], tblCols[4],
                                                       tblCols[5]))

plt.show()