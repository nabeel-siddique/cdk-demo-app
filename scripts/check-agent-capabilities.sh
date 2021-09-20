#!/usr/bin/env bash

if ! [ -x "$(command -v jq)" ]; then
    printf "%sPlease install jq %s\\n" 
    exit 1
elif ! [ -x "$(command -v cdk)" ]; then
    printf "%sPlease install cdk %s\\n" 
    exit 1
fi

printf "%sDependencies checked. %s\\n"