export PYTHONPATH=`pwd`
python tools/train_lprnet.py \
    --train_img_dirs /home/linux/workspace/ccpd2019/images/train \
    --test_img_dirs /home/linux/workspace/ccpd2019/images/test \
    --pretrained_model weights/lprnet_best.pth \
    --num_workers 10
