'''

分析题目，一个是对图片文件的操作，更改尺寸为1130 * 640

还有一个是遍历目录，把很多照片都规范化尺寸

下面给出更改图片大小的方法


def resize(filename):
    img = Image.open(filename)
    out = img.resize((640, 1130), Image.ANTIALIAS)


参数值
含义
Image.NEAREST
低质量
Image.BILINEAR
双线性
Image.BICUBIC
三次样条插值
Image.ANTIALIAS
高质量
resize（（宽，高），表格内参数值一栏）

上次习题应该已经接触过os这个模块，下面用他其中一个函数遍历目录下文件

list = os.listdir(r'X:\X\0005')
for i in list:
    resize(i)
os.listdir（path）返回的是一个列表对象

以上大致功能都已经实现了，下面加一个判断是否是jpg的操作


def getextension():
    for i in list:
        if os.path.splitext(i)[1] == '.jpg':
            f_list.append(i)


通过后缀名是否为jpg

os.path.splitext（filename）分离扩展名与文件名

想得到文件名即os.path.splitext（filename）[0]

'''

from PIL import Image
import os

os.getcwd()
os.chdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0005')


def resize(filename):
    img = Image.open(filename)
    out = img.resize((640, 1130), Image.ANTIALIAS)
    f = filename.strip(".jpg")
    newname = f + "r.jpg"
    out.save(newname)


list = os.listdir(r'C:\Users\Alex.hasee-PC\Desktop\pythonprogram\0005')
f_list = []


def getextension():
    for i in list:
        if os.path.splitext(i)[1] == '.jpg':
            f_list.append(i)


getextension()
for i in f_list:
    resize(i)