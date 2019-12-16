#!/bin/bash

# befor training
# gedit the .names .data .cfg
# .names concludes the names of the classes
# .data concludes of the exact pointer the the file
# 	train	the exact position of the training picture
#	valid	the exact position of the validing picture
#	names	the exact position of the classes
#	backup	store the temp weights while training
# .cfg concludes the fundamental paraments of the network
#	batch	the size of per fetching
#	filters	3*(classes+5)
#	classes the classes
	
# option | tee train.log 	produce the log before visualising

./darknet detector train cfg/test/voc.data cfg/yolov3-voc.cfg darknet53.conv.74

