#!/bin/bash

result0=$(echo "$1" | python3 python_test.py | filter-resolved);
result1=$(echo -n "$result0" | wc -m);
if [[ $result1 > 0 ]] 
    then
    echo "$1"
  fi
