import cv2
import random
import numpy as np
from PIL import Image


def PixRandomChange(img):
    # Image转cv2
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img[0, 0, 0] = random.randint(0, 0xfffffff)
    # cv2转Image
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return img
