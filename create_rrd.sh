#!/usr/bin/env bash

mkdir -p db

rrdtool create ./db/sensordata.rrd \
  --step 300 \
  DS:temperature:GAUGE:600:-274:100 \
  DS:humidity:GAUGE:600:0:100 \
  DS:battery:GAUGE:600:0:5 \
  RRA:AVERAGE:0.5:1:288 \
  RRA:AVERAGE:0.5:3:672 \
  RRA:AVERAGE:0.5:12:744 \
  RRA:AVERAGE:0.5:72:1460