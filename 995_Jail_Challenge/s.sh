#!/bin/bash

for i in $( ls comedor ) 
do
  base64 comedor/$i >> comedor/.miau 2> /dev/null
done
