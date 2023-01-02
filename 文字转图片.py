import cv2
import numpy as np
from os import getcwd
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
    pixels = [text[3 * i: 3 * i + 3] for i in range(len(text) // 3)]
    pixels_ = []
    for r, g, b in pixels:
        pixels_.append((r, g, b, 255))
        # 注：Alpha 通道的值代表这个像素有几个空值。如 a=1 时 b 应为空值
    rest_n = len(text) % 3
    if rest_n == 2:
        pixels_.append((text[-2], text[-1], 0, 254))
    elif rest_n == 1:
        pixels_.append((text[-1], 0, 0, 253))
    return pixels_


def paint(pixels: list) -> np.ndarray:
    height = len(pixels) // 500 + 1
    img = np.array([[(0, 0, 0, 253)] * 500] * height)
    for y in range(height):
        for x in range(500):
            n = 500 * y + x
            if n < len(pixels):
                img[y][x] = pixels[n]
    return img


def save(img: np.ndarray):
    while True:
        path = input("保存文件的名称：")
        if not exists(getcwd() + "\\" + path + ".png"):
            cv2.imwrite(getcwd() + "\\" + path + ".png", img)
            print("保存成功")
            break
        print("文件已存在")


if __name__ == "__main__":
    while True:
        text = readText()
        pixels = textToPixels(text)
        img = paint(pixels)
        save(img)

        print("出现错误")
