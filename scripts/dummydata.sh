#!/bin/bash

GRAPH_SERVER='104.131.45.105'
GRAPH_PORT='2003'
METRIC_NAME=$1
DATA_TYPE=$2

if [ $DATA_TYPE == "bend" ]; then
    while [ 1 -eq 1 ]; do
        echo "$METRIC_NAME $(( RANDOM % (947 - 730 + 1 ) + 730 )) `date +%s`" | nc $GRAPH_SERVER $GRAPH_PORT; #If running on a mac will need -c in the nc command
        sleep 1;
    done;
fi

