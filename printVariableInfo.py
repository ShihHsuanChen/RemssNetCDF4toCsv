# printVariableInfo.py
from netCDF4 import Dataset

def printVariableInfo(var) :

  try :
    valid_min = var.valid_min
  except :
    valid_min = ''

  try :
    valid_max = var.valid_max
  except :
    valid_max = ''

  try :
    standard_name = var.standard_name
  except :
    standard_name = ''

  try :
    units = var.units
  except :
    units = ''

  try :
    FillValue = str(var._FillValue)
  except :
    FillValue = ''

  ostream = ''
  ostream += str('%s;%s\n'%("name"           , var.name           ) )
  ostream += str('%s;%s\n'%("standard_name"  , standard_name      ) )
  ostream += str('%s;%s\n'%("long_name"      , var.long_name      ) )
  ostream += str('%s;%s\n'%("units"          , units              ) )
  ostream += str('%s;%s\n'%("comment"        , var.comment        ) )
  ostream += str('%s;%s\n'%("datatype"       , var.datatype       ) )
  ostream += str('%s;%s\n'%("dtype"          , var.dtype          ) )
  ostream += str('%s;%s\n'%("mask"           , var.mask           ) )
  ostream += str('%s;%s\n'%("ndim"           , var.ndim           ) )
  ostream += str('%s;%s\n'%("scale"          , var.scale          ) )
  ostream += str('%s;%s\n'%("shape"          , var.shape          ) )
  ostream += str('%s;%s\n'%("size"           , var.size           ) )
  ostream += str('%s;%s\n'%("valid_min"      , valid_min          ) )
  ostream += str('%s;%s\n'%("valid_max"      , valid_max          ) )
  ostream += str('%s;%s\n'%("_Fill_Value"    , FillValue          ) )
  ostream += str('%s;%s\n'%("dimensions"     , str(var.dimensions)) )

  return ostream












