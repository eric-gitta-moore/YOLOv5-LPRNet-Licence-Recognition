export PYTHONPATH=`pwd`

python tools/train_yolov5.py \
    --cfg models/yolov5s.yaml \
    --data data/ccpd.yaml \
    # --weights weights/yolov5s.pt \
    --device 0