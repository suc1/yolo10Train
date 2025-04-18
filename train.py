#coding:utf-8
from ultralytics import YOLO
import matplotlib
matplotlib.use('TkAgg')

model_yaml_path = "ultralytics/cfg/models/v10/yolov10n.yaml"
data_yaml_path = 'datasets/data.yaml'
pre_model_name = 'models/yolov10n.pt'


if __name__ == '__main__':
    model = YOLO(model_yaml_path).load(pre_model_name)
    results = model.train(data=data_yaml_path,
                          epochs=2,         # 训练轮数
                          batch=1,          # batch大小
                          name='train_v10', # 保存结果的文件夹名称
                          optimizer='SGD')  # 优化器

    # model.export(format='onnx')  # 导出模型
