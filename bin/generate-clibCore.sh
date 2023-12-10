#!/bin/bash

cp ../libbbmm/src/bbmm.h pyBbMm
cp ../libbbmm/libbbmm.so pyBbMm
python3 ./bin/c-to-py.py pyBbMm/bbmm.h pyBbMm/clibCore.py
