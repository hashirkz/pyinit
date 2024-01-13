#!/bin/bash

# removing python build files
echo "removing build dist and egg-info"
if [[ -d "build" ]]; then
    rm -rf build
fi

if [[ -d "dist" ]]; then
    rm -rf dist
fi

if [[ -d "*.egg-info" ]]; then
    rm -rf *.egg-info
fi

read -p "build wheel (yn)?" yn
if [[ $yn == "y" || $yn == "Y" ]]; then
    # building pip files    
    python setup.py sdist bdist_wheel
fi