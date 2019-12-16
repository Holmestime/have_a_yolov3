#!/bin/bash
./darknet detector valid test/data/test.data test/data/test.cfg backup/test_final.weights -out chopper.txt
