from PIL import Image
from math import ceil, floor
from os.path import exists


def readText() -> bytes:
    while True:
        mode = input("文件（f）/直接输入（i）？")
        if mode == "f" or mode == "i":
            break
        print("输入“f”或“i”")
    if mode == "f":
        while True:
            path = input("文件路径：")
            if exists(path):
                with open(path, "rb") as file:
                    return file.read()
            print("文件不存在")
    print("单行输入“<!--end-->”以结束：")
    text = ""
    while True:
        ln = input()
        if ln == "<!--end-->":
            text = text[:-1]
            break
        text += ln + "\n"
    return text.encode("utf-8")


def textToPixels(text: bytes) -> list:
    pixels = [text[3 * i: 3 * i + 3] for i in range(floor(len(text) / 3.0))]
    pixels_ = []
    for r, g, b in pixels:
        pixels_.append((r, g, b))
    rest_n = len(text) % 3
    if rest_n:
        if rest_n == 2:
            pixels_.append((text[-2], text[-1], 0))
        else:
            pixels_.append((text[-1], 0, 0))
    return pixels_


def paint(pixes: list) -> Image:
    height = ceil(len(pixes) / 200.0)
    img = Image.new(mode="RGB", size=(200, height), color="#000000")
    for y in range(height):
        for x in range(200):
            n = 200 * y + x
            if n < len(pixes):
                img.putpixel((x, y), pixes[n])
    return img


def save(img: Image):
    while True:
        path = input("保存在：")
        if not exists(path):
            img.save(path)
            print("保存成功")
            break
        print("文件已存在")


if __name__ == "__main__":
    while True:
        try:
            text = readText()
            pixels = textToPixels(text)
            img = paint(pixels)
            save(img)
        except:
            print("出现错误")
