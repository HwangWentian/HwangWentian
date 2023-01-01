from PIL import Image
from os.path import exists


def readImage() -> Image:
    while True:
        path = input("文件路径：")
        if exists(path):
            break
        print("文件不存在")
    return Image.open(path)


def imageToPixels(img: Image) -> list:
    height = img.size[1]
    pixels = []
    img_ = img.load()
    for y in range(height):
        for x in range(200):
            pixels.append(img_[x, y])
    return pixels


def pixelsToText(pixels: list) -> bytes:
    text = b''
    for r, g, b in pixels:
        text += int.to_bytes(r, 1, "big")
        text += int.to_bytes(g, 1, "big")
        text += int.to_bytes(b, 1, "big")
    return text.rstrip(b'\x00')


def save(text: bytes):
    while True:
        path = input("保存在：")
        if not exists(path):
            with open(path, "wb") as file:
                file.write(text)
                print("保存成功")
            break
        print("文件已存在")


if __name__ == "__main__":
    while True:
        try:
            img = readImage()
            pixels = imageToPixels(img)
            text = pixelsToText(pixels)
            save(text)
        except:    
            print("出现错误")
