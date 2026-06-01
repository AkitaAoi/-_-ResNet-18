# -_-ResNet-18
从零开始的第一个项目
2026/5/30 23：43
<img width="1472" height="472" alt="image" src="https://github.com/user-attachments/assets/1c17489e-7618-4975-8313-90f87f7f4660" />
无论如何，这个代码在此刻跑通了，接下来可以慢慢优化了。


2026/5/31 0：20
<img width="674" height="324" alt="image" src="https://github.com/user-attachments/assets/975b5513-558c-4c4a-829f-f6ae586d5377" />

使用数据归一化，减小了学习率，使得loss是个数了。

2026/6/1 23:18

学习率调整为0.0001，训练批次增加到50. 增加了权重衰减1e-4，全连接层之前加入了暂退层，参数为0.3. 整体上模型在验证集上的准确率高了一些，甚至最好的情况达到了70%(我想抓哟是巧合)，主要是Dropout(0.3)的功劳，不过最后还是过拟合了，下次考虑加点数据增强之类的。
<img width="663" height="559" alt="image" src="https://github.com/user-attachments/assets/ef739b46-f0d7-454d-80cc-38c860fc29f1" />

