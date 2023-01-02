import cv2
import numpy as np
from os import getcwd
from os.path import exists


def readImage() -> np.ndarray:
    while True:
        path = input("文件路径：")
        if exists(path):
            break
        print("文件不存在")
    return cv2.imread(path, cv2.IMREAD_UNCHANGED)


def imageToPixels(img: np.ndarray) -> list:
    height = img.shape[0]
    pixels = []
    for y in range(height):
        for x in range(500):
            pixels.append(img[y, x])
    return pixels


def pixelsToText(pixels: list) -> bytes:
    text = b''
    null_num = 0
    for r, g, b, a in pixels:
        text += int.to_bytes(int(r), 1, "big")
        text += int.to_bytes(int(g), 1, "big")
        text += int.to_bytes(int(b), 1, "big")
        null_num += 255 - a
    return text[:-null_num]


def save(text: bytes):
    while True:
        path = input("保存文件的名称：")
        if not exists(getcwd() + "\\" + path):
            with open(getcwd() + "\\" + path, "wb") as file:
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
