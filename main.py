import cv2
import random
import ImgTextClipboard
import numpy as np

from PIL import Image


def main():
    # 读入剪贴板图片
    img = ImgTextClipboard.copyImgFormClipboard()

    # Image转cv2
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img[0, 0, 0] = random.randint(0, 0xffffff)

    # cv2转Image
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # 写入图片到剪贴板
    ImgTextClipboard.pasteImgToClipboard(img)


if __name__ == '__main__':
    main()
