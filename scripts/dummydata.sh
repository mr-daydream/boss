#!/bin/bash

GRAPH_SERVER='104.131.45.105'
GRAPH_PORT='2003'
METRIC_NAME=$1

while [ 1 -eq 1 ]; do
        echo "$METRIC_NAME $(( RANDOM % (10 - 5 + 1 ) + 5 )) `date +%s`" | nc -c $GRAPH_SERVER $GRAPH_PORT;
    sleep 1;
done;

