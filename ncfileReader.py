#!/usr/bin/env python
import json
import numpy as np
from thor.reader import Reader
import os
import json
import re
folder = "/home/owodunni/thor/ncFiles"
outputInfoFile = 'EUR-44i.json'
outputDataFile = 'EUR-44i.data'

files = os.listdir(folder)

readers = []

for file in files:
    readers.append(Reader(folder+"/"+file))

data = readers[0].getData(readers[0].startDate,
                          readers[0].lastDate,
                          readers[0].minLat,
                          readers[0].maxLat,
                          readers[0].minLon,
                          readers[0].maxLon)["data"].data

for reader in readers[1:]:
    my_data = reader.getData(reader.startDate,
                             reader.lastDate,
                             reader.minLat,
                             reader.maxLat,
                             reader.minLon,
                             reader.maxLon)["data"].data
    
    data = np.concatenate((data,my_data), axis = 0)

data = data * 86400
data[data > 10000] = 0

dataInfoDict = {'Domain' : readers[0].domain,
            'Experiment' : readers[-1].experiment,
            'Model' : readers[0].model,
            'Dimension' : data.shape,
             'Area' : [readers[0].minLat,
                      readers[0].maxLat,
                      readers[0].minLon,
                      readers[0].maxLon],
            'StartDate' : readers[0].startDate.strftime("%Y-%m-%d"),
            'LastDate' : readers[-1].lastDate.strftime("%Y-%m-%d"),
            'Data' : data.tolist()
            }

dataDict = data.tolist()

#print(dataDict)

j = json.dumps(dataInfoDict)
f = open(outputInfoFile, 'w')
f.write(j)
f.close()

#j = json.dumps(dataDict, indent=4)
#f = open(outputDataFile, 'w')
#f.write(j)
#f.close()

#print(dataDict)

#with open(outPutFile, 'w') as outfile:
 #   json.dump(data,outfile)

    
    


