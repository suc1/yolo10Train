# YOLO 10
1. [doc](https://docs.ultralytics.com/models/yolov10/)
2. [coco8.yaml](D:\PycharmProjects2\YOLO10\.venv\Lib\site-packages\ultralytics\cfg\datasets\coco8.yaml)

## Install
```commandline
uv init yolo10Train
cd yolo10Train
uv add ultralytics==8.2.91
```

## 打标工具: `<class_id> <x_center> <y_center> <width> <height>`
1. `uv add label-studio`, `label-studio`
2. `uv add labelImg`, `labelImg`
3. [CVAT](https://cvat.org)
4. [Roboflow Annotate](https://roboflow.com)
5. [local files](https://labelstud.io/guide/storage.html#Local-storage)
```commandline
set LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
set LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=D:\\PycharmProjects2\\YOLO10\\datasets\\coco8\\images
```