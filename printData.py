# printData.py

from netCDF4 import Dataset
import numpy as np

def printData(top) :

  ostream = ''

  data_dims = list(top.dimensions)
  data_vars = list(top.variables)

  data_shape = {}
  for item in data_dims :
    data_shape[item] = top.dimensions[item].size

  data = {}
  mask = {}

  data_flat = {} # keys=(time,ni,nj) values=[time lon lat var1 var2 var3 ... ]

  # specify the dimensions: time nj ni
  # check dimensions
  if not('time' in data_dims) :
    print('Cannnot find dimension \'time\' in dimension')
    return ''
  if not('nj' in data_dims) :
    print('Cannnot find dimension \'nj\' in dimension')
    return ''
  if not('ni' in data_dims) :
    print('Cannnot find dimension \'ni\' in dimension')
    return ''
  if not('time' in data_vars) :
    print('Cannnot find dimension \'time\' in variable')
    return ''
  else :
    data_vars.remove('time')

  if not('lon' in data_vars) :
    print('Cannnot find dimension \'lon\' in variable')
    return ''
  else :
    data_vars.remove('lon')

  if not('lat' in data_vars) :
    print('Cannnot find dimension \'lat\' in variable')
    return ''
  else :
    data_vars.remove('lat')

  title = ['time','lon','lat']
  for variable in data_vars :
    title.append(variable)

  for itime in range(data_shape['time']) :

    time = top['time'][itime]
    for nj in range(data_shape['nj']) :
      for ni in range(data_shape['ni']) :

        print('process (%d,%d)'%(nj,ni))
        #if top['lon'][:].mask[nj,ni] :
        #  continue

        #lon = top['lon'][:].data[nj,ni]
        #lat = top['lat'][:].data[nj,ni]
        lon = top['lon'][:][nj,ni]
        lat = top['lat'][:][nj,ni]
        data_flat[(time,nj,ni)] = [time,lon,lat]

        for variable in data_vars :
          if False : # top[variable][:].mask[itime,nj,ni] :
            data_flat[(time,nj,ni)].append('')
          else :
            data_flat[(time,nj,ni)].append(top[variable][:].data[itime,nj,ni])
  
  for item in title :
    ostream += str(item)
    ostream += ';'
  ostream += '\n'

  for keys in data_flat :
    for value in data_flat[keys] :
      ostream += str(value)
      ostream += ';'
    ostream += '\n'

  return ostream
