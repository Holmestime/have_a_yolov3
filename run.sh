#!/bin/bash
./darknet detector train test/data/test.data test/data/test.cfg darknet53.conv.74 -gpus 0 | tee train.log
