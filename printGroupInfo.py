# printGroupInfo.py

from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma

def printGroupInfo(group) :

  ostream = ''

  ostream += 'dimensions;'
  for item in list(top.dimensions) :
    ostream += str(item)
    ostream += ' '

  ostream += '\n'

  for item in list(top.dimensions) :
    ostream += str('%s (%s);%d\n'%("dimensions",item,top.dimensions[item].size) )

  ostream += 'groups;'
  for item in list(top.groups):
    ostream += str(item)
    ostream += ' '

  ostream += '\n'

  return ostream
