# RemssNetCDF4toCsv.py
import sys
import argparse as argparse
import numpy as np
import numpy.ma as ma
import pandas as pd
from netCDF4 import Dataset
from printTopInfo import *
from printVariableInfo import *

def RemssNetCDF4toCsv(args) :

  ifname = args.ifname[0]
  ofname = args.ofname[0]
  target = args.target
  lon_min = args.lon_min
  lon_max = args.lon_max
  lat_min = args.lat_min
  lat_max = args.lat_max

  if not(lon_min==None) and not(lon_max==None) :
    if lon_min > lon_max :
      print('[Error] Invalid longitude range: lon_min should be smaller than lon_max')

  if not(lat_min==None) and not(lat_max==None) :
    if lat_min > lat_max :
      print('[Error] Invalid latitude range: lat_min should be smaller than lat_max')

  # Consider that:
  # 1. No subgroup
  # 2. dimentions of variables are always (time,longitude,latitude)
  # 3. dimention of time equals to 1
  # Add selection criteria to the top information

  top = Dataset(ifname,'r+')

  ofname_info = ofname+'.info'

  with open(ofname_info,'w') as ofile :
    
    ofile.write('File name: ')
    ofile.write(ifname)
    ofile.write('\n')
    ofile.write(printTopInfo(top))
    ofile.write('\n')

    for variable in list(top.variables) :
      var = top[variable]
      ofile.write('Variable: ')
      ofile.write(variable)
      ofile.write('\n')
      ofile.write(printVariableInfo(var))
      ofile.write('\n')

  ofile.closed

  list_variables = list(top.variables)
  list_variables.remove('time')
  list_variables.remove('lon')
  list_variables.remove('lat')

  if target!=None :
    for variable in target :
      if not(variable in list_variables) :
        target.remove(variable)
  else :
    target = list_variables

  dict_data = {'lon': top['lon'][:].reshape([-1]),
               'lat': top['lat'][:].reshape([-1]) }

  #for variable in list_variables :
  for variable in target :
    var = top[variable][:].reshape([-1])
    dict_data[variable] = var

  df = pd.DataFrame(dict_data, columns=dict_data.keys())
  if lon_min == None :
    lon_min = df['lon'].min()
  if lon_max == None :
    lon_max = df['lon'].max()
  if lat_min == None :
    lat_min = df['lat'].min()
  if lat_max == None :
    lat_max = df['lat'].max()

  df2 = df[ (df['lon']>lon_min) &
            (df['lon']<lon_max) &
            (df['lat']>lat_min) &
            (df['lat']<lat_max)  ]

  df2.to_csv(ofname,sep=';',index=False)


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description='Simply convert netCDF4 file to csv file.')
  parser.add_argument('ifname', metavar='input', type=str, nargs='+',
                      help='input file name')

  parser.add_argument('ofname', metavar='output', type=str, nargs='+',
                      help='output file name')

  parser.add_argument('--target',dest='target', type=str, nargs='+',
                      help='target variables')

  parser.add_argument('--lon_min',dest='lon_min',type=float,
                      help='lower bound for longitude')
  
  parser.add_argument('--lon_max',dest='lon_max',type=float,
                      help='upper bound for longitude')
  
  parser.add_argument('--lat_min',dest='lat_min',type=float,
                      help='lower bound for latitude')
  
  parser.add_argument('--lat_max',dest='lat_max',type=float,
                      help='upper bound for latitude')
  
  args = parser.parse_args()

  RemssNetCDF4toCsv(args)
