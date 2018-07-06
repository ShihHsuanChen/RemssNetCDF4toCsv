# printTopInfo.py

from netCDF4 import Dataset
import numpy as np
import numpy.ma as ma

def printTopInfo(top) :

  ostream = ''

  ostream += str('%s;%s\n'%("Conventions"               , top.Conventions               ) )
  ostream += str('%s;%s\n'%("title"                     , top.title                     ) )
  ostream += str('%s;%s\n'%("summary"                   , top.summary                   ) )
  ostream += str('%s;%s\n'%("comment"                   , top.comment                   ) )
  ostream += str('%s;%s\n'%("references"                , top.references                ) )
  ostream += str('%s;%s\n'%("institution"               , top.institution               ) )
  ostream += str('%s;%s\n'%("gds_version_id"            , top.gds_version_id            ) )
  ostream += str('%s;%s\n'%("netcdf_version_id"         , top.netcdf_version_id         ) )
  ostream += str('%s;%s\n'%("date_created"              , top.date_created              ) )
  ostream += str('%s;%s\n'%("uuid"                      , top.uuid                      ) )
  ostream += str('%s;%s\n'%("history"                   , top.history                   ) )
  ostream += str('%s;%s\n'%("license"                   , top.license                   ) )
  ostream += str('%s;%s\n'%("id"                        , top.id                        ) )
  ostream += str('%s;%s\n'%("naming_authority"          , top.naming_authority          ) )
  ostream += str('%s;%s\n'%("product_version"           , top.product_version           ) )
  ostream += str('%s;%s\n'%("file_quality_level"        , top.file_quality_level        ) )
  ostream += str('%s;%s\n'%("spatial_resolution"        , top.spatial_resolution        ) )
  ostream += str('%s;%s\n'%("start_time"                , top.start_time                ) )
  ostream += str('%s;%s\n'%("stop_time"                 , top.stop_time                 ) )
  ostream += str('%s;%s\n'%("time_coverage_start"       , top.time_coverage_start       ) )
  ostream += str('%s;%s\n'%("time_coverage_end"         , top.time_coverage_end         ) )
  ostream += str('%s;%s\n'%("southernmost_latitude"     , top.southernmost_latitude     ) )
  ostream += str('%s;%s\n'%("northernmost_latitude"     , top.northernmost_latitude     ) )
  ostream += str('%s;%s\n'%("westernmost_longitude"     , top.westernmost_longitude     ) )
  ostream += str('%s;%s\n'%("easternmost_longitude"     , top.easternmost_longitude     ) )
  ostream += str('%s;%s\n'%("source"                    , top.source                    ) )
  ostream += str('%s;%s\n'%("platform"                  , top.platform                  ) )
  ostream += str('%s;%s\n'%("sensor"                    , top.sensor                    ) )
  ostream += str('%s;%s\n'%("Metadata_Conventions"      , top.Metadata_Conventions      ) )
  ostream += str('%s;%s\n'%("metadata_link"             , top.metadata_link             ) )
  ostream += str('%s;%s\n'%("keywords"                  , top.keywords                  ) )
  ostream += str('%s;%s\n'%("keywords_vocabulary"       , top.keywords_vocabulary       ) )
  ostream += str('%s;%s\n'%("standard_name_vocabulary"  , top.standard_name_vocabulary  ) )
  ostream += str('%s;%s\n'%("geospatial_lat_units"      , top.geospatial_lat_units      ) )
  ostream += str('%s;%s\n'%("geospatial_lat_resolution" , top.geospatial_lat_resolution ) )
  ostream += str('%s;%s\n'%("geospatial_lon_units"      , top.geospatial_lon_units      ) )
  ostream += str('%s;%s\n'%("geospatial_lon_resolution" , top.geospatial_lon_resolution ) )
  ostream += str('%s;%s\n'%("acknowledgment"            , top.acknowledgment            ) )
  ostream += str('%s;%s\n'%("creator_name"              , top.creator_name              ) )
  ostream += str('%s;%s\n'%("creator_email"             , top.creator_email             ) )
  ostream += str('%s;%s\n'%("creator_url"               , top.creator_url               ) )
  ostream += str('%s;%s\n'%("project"                   , top.project                   ) )
  ostream += str('%s;%s\n'%("publisher_name"            , top.publisher_name            ) )
  ostream += str('%s;%s\n'%("publisher_url"             , top.publisher_url             ) )
  ostream += str('%s;%s\n'%("publisher_email"           , top.publisher_email           ) )
  ostream += str('%s;%s\n'%("processing_level"          , top.processing_level          ) )
  ostream += str('%s;%s\n'%("cdm_data_type"             , top.cdm_data_type             ) )

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

