#coding:utf-8
from ultralytics import YOLO

# 所需加载的模型目录
path = 'runs\\detect\\train_v10\\weights\\best.pt'
img_path = "datasets\\test\\images\\6.jpg"

model = YOLO(path, task='detect')

results = model(img_path)
print(results)
results[0].show()