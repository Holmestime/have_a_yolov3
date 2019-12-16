#### simple detect
'./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg'

#### exact detect
'./darknet detector test cfg/coco.data cfg/yolov3.cfg weights/yolov3.weights data/dog.jpg'

##### not pointer to jpg to detect multiples
'./darknet detector test cfg/coco.data cfg/yolov3.cfg weights/yolov3.weights'

#### change the detection thresold
'./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg -thresh 0'

#### display the current
'./darknet detector demo cfg/coco.data cfg/yolov3.cfg weights/yolov3.weights'

#### detect the video
'./darknet detector demo cfg/coco.data cfg/yolov3.cfg weights/yolov3.weights <video file>'

#### train
'./darknet detector train cfg/voc.data cfg/yolov3-voc.cfg darknet53.conv.74'

#### calculate the anchors
'./darknet detector calc_anchors /path/to/.data -num_of_clusters 4 -width 416 -heigh 416'

