from pathlib import Path

datasets_dir = Path('../datasets')
datasets_dir.mkdir(parents=True, exist_ok=True)

for subfolder in ['train', 'val', 'test']:
    subdir = datasets_dir / subfolder
    subdir.mkdir(parents=True, exist_ok=True)
    for leaf in ['images', 'labels']:
        leaf_dir = subdir / leaf
        leaf_dir.mkdir(parents=True, exist_ok=True)

print('图片放在 datasets/train/images/')