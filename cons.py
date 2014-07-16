import sys

pathnameto_eppy = '/Applications/eppy-0.4.6'
sys.path.append(pathnameto_eppy)

from eppy import modeleditor
from eppy.modeleditor import IDF
iddfile = "/Users/eayoungs/Dropbox/SHARE/BSUG/Energy+.idd"
fname1 = '/Users/eayoungs/Dropbox/SHARE/BSUG/FinalModels/Baseline.idf'

#IDF.setiddname(iddfile) # This only needs to be run the first time through
idf1 = IDF(fname1)

#-----------------------------------------------------------------------------------------------------------------------

surfaces = idf1.idfobjects["BUILDINGSURFACE:DETAILED"]
northExtWalls = []
[northExtWalls.extend(surfaces[0:i]) for i in range(len(surfaces)+1) if surfaces[50].Surface_Type == 'Wall']

print northExtWalls