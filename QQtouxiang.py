# 引入Pillow
from PIL import Image, ImageDraw, ImageFont, ImageColor
import random
def add_num(img):
    # 创建一个Draw对象
    draw = ImageDraw.Draw(img)
    # 创建一个 Font
    myfont = ImageFont.truetype('C:/windows/Fonts/Arial.ttf', size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    i=random.randint(1,9 )
    draw.text((width-30, 0), '%i'%i, font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    return 0
if __name__ == '__main__':
    image = Image.open('D:\photo\head.jpg')
    add_num(image)

