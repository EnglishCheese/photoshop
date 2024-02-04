from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog,
    QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGUi import *
from PyQt5.QtCore import Qt
import os
from PIL import Image

app = QApplication([])
win = QWidget()
win.resize(1200, 700)
win.setWindowTitle('Easy Editor')
win.setStyleSheet('background-color:#ABDCFF;font-size:24px;padding: 5px; color:white')

lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
lv_files = QListWidget()
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Віддзеркалити')
btn_sharp = QPushButton('Різкість')
btn_bv = QPushButton('Ч-Б')

btn_dir.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_left.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_right.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_flip.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_bv.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_sharp.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')

btn_left.setCursor(Qt.PointingHandCursor)
btn_right.setCursor(Qt.PointingHandCursor)
btn_flip.setCursor(Qt.PointingHandCursor)
btn_sharp.setCursor(Qt.PointingHandCursor)
btn_bv.setCursor(Qt.PointingHandCursor)




















win.show()
workdir = ''
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.andswith(ext):
                result.append(filename)

    return result
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def shoWFilenamesList():
    extensions = ['.jpg','.jpeg','.png','.gif']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)
btn_dir.clicked.connect(shoWFilenamesList)

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'
    def loadImage(self, dir, filename):
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    def saveImage(self):
        path =os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.mkedir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)
    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        pixmapimage = pixmapimage.scaled(600, 650, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()
def ShowChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lv_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.filename)
        workimage.showImage(image_path)
workimage = ImageProcessor()
lv_files.currentRowChanged.connect(showChosenImage)
app.exec_()