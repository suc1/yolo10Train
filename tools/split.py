from pathlib import Path
from shutil import copy2, move
import random

random.seed(0)

base = Path('../datasets')
train_images_dir = base / 'train' / 'images'
train_labels_dir = base / 'train' / 'labels'

val_images_dir = base / 'val' / 'images'
val_labels_dir = base / 'val' / 'labels'

test_images_dir = base / 'test' / 'images'
test_labels_dir = base / 'test' / 'labels'

for path in [val_images_dir, val_labels_dir, test_images_dir, test_labels_dir]:
    path.mkdir(parents=True, exist_ok=True)

image_files = sorted(train_images_dir.glob('*.jpg')) + sorted(train_images_dir.glob('*.png'))
random.shuffle(image_files)

# 拆分比例 3:2:1
total = len(image_files)
train_count = total * 3 // 6
val_count = total * 2 // 6
test_count = total - train_count - val_count

new_train = image_files[:train_count]
new_val = image_files[train_count:train_count+val_count]
new_test = image_files[train_count+val_count:]

# 辅助函数：复制图像和标签
def copy_pair(image_path, dest_images_dir, dest_labels_dir):
    label_path = train_labels_dir / (image_path.stem + '.txt')
    # copy2(image_path, dest_images_dir)
    move(image_path, dest_images_dir)
    if label_path.exists():
        # copy2(label_path, dest_labels_dir)
        move(label_path, dest_labels_dir)
    else:
        print(f"⚠️ 标签不存在: {label_path.name}")

# 执行复制
for img in new_val:
    copy_pair(img, val_images_dir, val_labels_dir)

for img in new_test:
    copy_pair(img, test_images_dir, test_labels_dir)

print("✅ 按照 3:2:1 完成 val/test 数据拆分。")
