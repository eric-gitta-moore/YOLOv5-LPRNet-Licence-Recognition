export PYTHONPATH=`pwd`

python tools/train_yolov5.py \
    --cfg models/yolov5s.yaml \
    --data data/ccpd.yaml \
    --weights weights/yolov5_best.pt \
    --device 0