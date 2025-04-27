# 车牌检测识别模型训练教程

本教程将指导您如何准备数据集并训练车牌检测和识别模型。整个过程分为数据集准备、YOLOv5车牌检测模型训练和LPRNet车牌识别模型训练三个主要部分。

## 一、数据集准备

### 1.1 获取数据集
- 本项目使用CCPD2019数据集的筛选版本（约3万张图片）
- 数据集下载地址：https://aistudio.baidu.com/datasetdetail/262952/0

### 1.2 数据集处理

#### 1.2.1 数据集目录结构
下载并解压数据集后，请按以下结构组织数据：
```
datasets/ccpd/
    ├── images/
    │   ├── train/
    │   ├── val/
    │   └── test/
    └── labels/
        ├── train/
        ├── val/
        └── test/
```

#### 1.2.2 转换为YOLOv5格式
使用`tools/ccpd2yolov5.py`脚本将CCPD数据集转换为YOLOv5格式：

```bash
# 修改ccpd2yolov5.py中的路径配置
python tools/ccpd2yolov5.py
```

#### 1.2.3 转换为LPRNet格式
使用`tools/ccpd2lpr.py`脚本处理车牌识别数据：

```bash
# 修改ccpd2lpr.py中的路径配置
python tools/ccpd2lpr.py
```

## 二、YOLOv5车牌检测模型训练

### 2.1 配置文件说明

#### 2.1.1 模型配置
在`models/yolov5s.yaml`中：
- 修改`nc`参数为1（仅检测车牌一个类别）
- 根据数据集特点调整`anchors`参数

#### 2.1.2 数据集配置
在`data/ccpd.yaml`中配置：
- train、val、test数据集路径
- 类别数量和名称

### 2.2 开始训练

执行以下命令开始训练：
```bash
bash scripts/train_yolo.sh
```

主要训练参数说明：
- `--cfg`: 模型配置文件路径
- `--data`: 数据集配置文件路径
- `--weights`: 预训练权重路径（可选）
- `--device`: GPU设备号

## 三、LPRNet车牌识别模型训练

### 3.1 训练参数说明

在`tools/train_lprnet.py`中的主要参数：
- `train_img_dirs`: 训练集图片目录
- `test_img_dirs`: 测试集图片目录
- `learning_rate`: 学习率
- `train_batch_size`: 训练批次大小
- `img_size`: 输入图片尺寸
- `lpr_max_len`: 车牌最大字符数
- `dropout_rate`: Dropout比率

### 3.2 开始训练

执行以下命令开始训练：
```bash
bash scripts/train_lprnet.sh
```

### 3.3 训练过程监控

训练过程中会输出：
- 每个epoch的训练损失
- 定期的验证准确率
- 模型权重保存在`weights`目录

## 四、注意事项

1. 数据集处理：
   - 确保图片路径正确配置
   - 检查生成的标注文件格式
   - 删除损坏的图片文件

2. YOLOv5训练：
   - 根据显存大小调整batch size
   - 适当调整学习率和训练轮数
   - 定期保存检查点

3. LPRNet训练：
   - 确保车牌图片已正确裁剪和缩放
   - 注意字符映射关系的正确性
   - 监控验证集准确率避免过拟合

## 五、模型评估

训练完成后，可以使用以下脚本评估模型性能：

```bash
# YOLOv5模型测试
python tools/test_yolov5.py

# LPRNet模型测试
python tools/test_lprnet.py
```

评估指标包括：
- 车牌检测：准确率、召回率、mAP
- 车牌识别：字符级准确率、完整车牌准确率