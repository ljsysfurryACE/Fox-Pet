# 🦊 Fox Pet — 像素狐狸桌宠 (Linux/Ubuntu)

透明置顶 GIF 桌宠：拖拽移动 / 右键菜单 / 动画循环

## 🚀 运行（免依赖，单文件）

```bash
./fox_pet                  # 自动加载同目录 fox.gif
./fox_pet 任意.gif         # 或指定你自己的 GIF
```

> Linux x86_64 · PySide6 自包含 · 无需安装任何依赖

## 🎮 交互

| 操作 | 功能 |
|------|------|
| 左键拖拽 | 移动桌宠 |
| 右键菜单 | 暂停/播放 · 置顶切换 · 退出 |

## 📁 文件

- `fox_pet` — 编译好的可执行文件 (67MB, PyInstaller 单文件)
- `fox.gif` — 像素狐狸素材 (180×180, 61 帧)
- `fox_pet.py` — 源码 (PySide6, ~90 行)

## 🔧 自己改素材

```python
# 任意 GIF 都能当桌宠: 替换 fox.gif 即可
# 或命令行指定: ./fox_pet my_pet.gif
```

## 🏗️ 重新编译

```bash
pip install pyinstaller PySide6
python3 -m PyInstaller --noconfirm -F -w --name fox_pet fox_pet.py
```

## 素材来源

像素狐狸 GIF（墨镜傲娇狐狸，61 帧动画）
