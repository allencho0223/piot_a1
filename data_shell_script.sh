#!/bin/bash

# Variables
TIMER=0
MAX_RUNTIME=12

# Run data_collector.py script for a minute (12 different data is collected)
while [ $TIMER -le $MAX_RUNTIME ]
do
    python3 data_collector.py
    sleep 5;
    TIMER=$(( TIMER + 1 ))
done
