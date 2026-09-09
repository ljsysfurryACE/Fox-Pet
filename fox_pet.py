#!/usr/bin/env python3
"""
fox_pet.py — 像素狐狸桌宠 (Ubuntu)
透明无边框置顶窗口 + GIF 动画 + 拖拽移动 + 右键菜单

用法: python3 fox_pet.py [gif路径]
打包: pyinstaller -F -w fox_pet.py
"""
import sys, os

from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QAction, QMovie, QPixmap, QPainter
from PySide6.QtWidgets import QApplication, QWidget, QMenu

DEFAULT_GIF = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'fox.gif')


class PetWindow(QWidget):
    def __init__(self, gif_path):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint |
                            Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 加载 GIF
        self.movie = QMovie(gif_path)
        self.movie.setScaledSize(self.movie.currentPixmap().size() * 2)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.frameChanged.connect(self.update)
        self.movie.start()

        self.pixmap = None
        self.setFixedSize(self.movie.currentPixmap().size() * 2)
        self._drag_pos = None

    def paintEvent(self, e):
        p = QPainter(self)
        pm = self.movie.currentPixmap()
        p.drawPixmap(0, 0, pm)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self._drag_pos = e.globalPosition().toPoint() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, e):
        if self._drag_pos and (e.buttons() & Qt.LeftButton):
            self.move(e.globalPosition().toPoint() - self._drag_pos)

    def mouseReleaseEvent(self, e):
        self._drag_pos = None

    def contextMenuEvent(self, e):
        menu = QMenu(self)
        menu.setStyleSheet("QMenu { background:#fff; border:1px solid #ccc; }")
        pa = menu.addAction("暂停" if self.movie.state() == QMovie.Running else "播放")
        pa.triggered.connect(self.toggle_pause)
        ta = menu.addAction("置顶" if not self.windowFlags() & Qt.WindowStaysOnTopHint else "取消置顶")
        ta.triggered.connect(self.toggle_top)
        ex = menu.addAction("退出")
        ex.triggered.connect(QApplication.quit)
        menu.exec(e.globalPos())

    def toggle_pause(self):
        if self.movie.state() == QMovie.Running:
            self.movie.setPaused(True)
        else:
            self.movie.setPaused(False)

    def toggle_top(self):
        if self.windowFlags() & Qt.WindowStaysOnTopHint:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.show()


def main():
    app = QApplication(sys.argv)
    gif = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_GIF
    if not os.path.exists(gif):
        print(f"GIF 不存在: {gif}")
        return 1

    w = PetWindow(gif)
    w.move(100, 100)
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
