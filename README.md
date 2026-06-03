# -_-ResNet-18
从零开始的第一个项目
# Cat vs Dog Image Classification

## 项目简介
使用 ResNet-18 预训练模型对 Kaggle 猫狗数据集进行二分类，通过数据增强、动量 SGD、权重衰减、Dropout 等技术将验证准确率提升至 82%。

## 数据集
- 来源：Kaggle Dogs vs Cats（[https://www.kaggle.com/datasets/tongpython/cat-and-dog]）
- 训练集：约 8000 张图片（cats:4001, dogs:4006）
- 划分：训练集 70%，验证集 30%（使用随机划分）

## 依赖环境
- Python 3.8+
- PyTorch 1.9+
- torchvision
- matplotlib
- numpy

## 快速开始
1. 安装依赖：`pip install torch torchvision matplotlib numpy pillow`
2. 数据集：下载 Kaggle 猫狗数据集，并将 `training_set` 路径修改到代码中。
3. 训练：打开 `dogs-vs-cats-with-aug seed42.ipynb`，按顺序执行单元格即可。
4. 预测单张图片：`python inference.py /path/to/your/cat.jpg`

## 模型架构
- 基础模型：ResNet-18（ImageNet 预训练）
- 修改：最后一层全连接改为 2 个输出，添加 Dropout(0.3)
- 优化器：SGD with momentum=0.9, lr=0.001, weight_decay=1e-4
- 损失函数：交叉熵
- 数据增强：随机水平翻转、随机裁剪、颜色抖动（可选）

## 训练结果
- 最佳验证准确率：82.42%（epoch 38）
- 训练/验证 loss 曲线：<img width="1106" height="410" alt="image" src="https://github.com/user-attachments/assets/3a61a031-5280-40e5-b693-cfac8dc0b05a" />


## 改进方向
- 使用更深的预训练模型（ResNet-50, EfficientNet）
- 增加更多数据增强（随机旋转、仿射变换）
- 学习率调度（ReduceLROnPlateau）
- 模型集成

## 作者
AkitaAoi / GitHub 链接

## 许可证
MIT

------------------下面是一些过程记录--------------------





2026/5/30 23：43
<img width="1472" height="472" alt="image" src="https://github.com/user-attachments/assets/1c17489e-7618-4975-8313-90f87f7f4660" />
无论如何，这个代码在此刻跑通了，接下来可以慢慢优化了。


2026/5/31 0：20
<img width="674" height="324" alt="image" src="https://github.com/user-attachments/assets/975b5513-558c-4c4a-829f-f6ae586d5377" />

使用数据归一化，减小了学习率，使得loss是个数了。

2026/6/1 23:18

学习率调整为0.0001，训练批次增加到50. 增加了权重衰减1e-4，全连接层之前加入了暂退层，参数为0.3. 整体上模型在验证集上的准确率高了一些，甚至最好的情况达到了70%(我想应该是巧合)，主要是Dropout(0.3)的功劳，不过最后还是过拟合了，下次考虑加点数据增强之类的。
<img width="663" height="559" alt="image" src="https://github.com/user-attachments/assets/ef739b46-f0d7-454d-80cc-38c860fc29f1" />

2026/6/3 23:09

重新写了一下README，上传了自家的几张狗，可以通过命令行运行inference.py(model.py和best_cat_dog_model.pth也要下载放在同一个文件夹里)预测单张图片是猫还是狗。目前测试只有1.jpg给认成猫了。
