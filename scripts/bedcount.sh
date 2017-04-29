#!/bin/bash
GRAPH_SERVER='104.131.45.105'
GRAPH_PORT='2003'

while [ 1 -eq 1 ]; do
    for i in $( ls -d /local/storage/whisper/center* | awk -F / {'print $5;'} ); do
        echo "$i.count `ls -d /local/storage/whisper/$i/bed* |wc -l` `date +%s`"| nc $GRAPH_SERVER $GRAPH_PORT;
        sleep 1;
    done;
done;
