#!/bin/bash

{
    echo "uuid,date,title,vote";
    cat elections/*.csv;
} > all_elections.csv

