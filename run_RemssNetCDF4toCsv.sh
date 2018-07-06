#!/bin/bash
Dir='REMSS-L2P_GHRSST-SSTsubskin-TMI-L2b_20140819_20140830'
flist=$Dir/filelist
while read -r ifname;
do
    echo "processing $ifname"
    ofname=${ifname//.nc/.csv}
    python RemssNetCDF4toCsv.py $Dir/$ifname $Dir/$ofname --lon_min 115 --lon_max 130 --lat_min 15 --lat_max 35

done < "$flist"
