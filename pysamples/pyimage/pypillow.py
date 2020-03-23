#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFilter


def showImage():
    image = Image.open("./timg.jpg")
    print(image.format, image.size, image.mode)
    image.show()


def cutImage():
    image = Image.open("./timg.jpg")
    rect = (80, 20, 310, 360)
    newImage = image.crop(rect)
    newImage.show()


def resizeImage():
    image = Image.open("./timg.jpg")
    image.show()
    new_image = image.resize((int(image.size[0]/2), int(image.size[1]/2)))
    new_image.show()


def toThumbnail():
    image = Image.open("./timg.jpg")
    size = (128, 128)
    image.thumbnail(size)
    image.show()


def cropAndPaste():
    image1 = Image.open("./timg.jpg")
    image2 = Image.open("./block.png")

    rect = (80, 20, 310, 360)
    newImage1 = image1.crop(rect)
    size = newImage1.size
    image2.paste(newImage1, (172, 40))
    image2.show()


def rotateImage():
    image = Image.open("./timg.jpg")
    image.rotate(90).show()  # 逆时针旋转
    image.rotate(120).show()
    image.rotate(180).show()
    image.rotate(270).show()


def transposeImage():
    image = Image.open("./timg.jpg")
    image.show()
    image.transpose(Image.FLIP_LEFT_RIGHT).show()


def putpixel():
    image = Image.open("./timg.jpg")
    for x in range(0, 300):
        for y in range(0, 500):
            image.putpixel((x, y), (255, 255, 255))
    image.show()


def filterImage():
    image = Image.open("./timg.jpg")
    image.filter(ImageFilter.CONTOUR).show()

if __name__ == "__main__":
    showImage()
    cutImage()
    resizeImage()
    toThumbnail()
    cropAndPaste()
    rotateImage()
    transposeImage()
    putpixel()
    filterImage()
