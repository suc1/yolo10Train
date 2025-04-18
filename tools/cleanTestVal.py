from pathlib import Path

dirs_to_clean = [
    Path('../datasets/val/images'),
    Path('../datasets/val/labels'),
    Path('../datasets/test/images'),
    Path('../datasets/test/labels')
]

# 删除目录下所有文件
for folder in dirs_to_clean:
    if folder.exists():
        files = list(folder.glob('*'))
        for f in files:
            if f.is_file():
                f.unlink()
        print(f"✅ 已清空：{folder.resolve()}")
    else:
        print(f"⚠️ 目录不存在：{folder}")
