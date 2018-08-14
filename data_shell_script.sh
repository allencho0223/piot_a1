#!/bin/bash

TIMER=0
MAX_RUNTIME=12

while [ $TIMER -le $MAX_RUNTIME ]
do
    python3 data_collector.py
    sleep 5;
    TIMER=$(( TIMER + 1 ))
done
