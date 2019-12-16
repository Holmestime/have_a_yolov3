filters = 3 *(classes+5)   ##the num of center
anchors(聚类方法有关)
random(多尺度训练)

Result 
Region xx : cfg文件中yolo-layer索引
Avg IOU: 当前迭代中,预测的box与标注的box平均交并比，越大越好，期望值为1
class: 标注物体分类的准确率，越大越好，期望为1
obj: 越大越好，期望为1
No obj :越小越好
.5R : 以IOU = 0.5为阈值时候的recall
recall = 检出的正样本 / 实际的正样本
count: 正样本数目

#### train
`./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74`

#### use multiple GPU
`./darknet detector train cfg/coco.data cfg/yolov3.cfg darknet53.conv.74 -gpus 0,1,2,3`

#### restart
`./darknet detector train cfg/coco.data cfg/yolov3.cfg backup/yolov3.backup - gpus 0,1,2,3`



#### run the detector

`./darkent detect cfg/yolov3.cfg yolov3.weights data/xxx.jpg`

##### most common 

`./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/xxx.jpg`



#### change the Threshold

`./darknet detect cfg/yolov3.cfg yolov3.weights data/xxx.jpg -thresh 0.5`



#### detect the video

`./darknet detector demo cfg/coco.data cfg/yolov3.cfg yolov3.weights /path/to/video`



#### the process to train

label.txt / xxx.data / xxx.cfg /xxx.names

