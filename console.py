import cv2
import os.path
import platform
import random
import sys


def main(args):
    # 读入剪贴板图片
    abs_img_path = AbsPathFix(args[1])
    print(abs_img_path)

    try:
        # 读入 修改 写出
        img = cv2.imread(abs_img_path)
        img[0, 0, 0] = random.randint(0, 0xffffff)
        cv2.imwrite(abs_img_path, img)
        print(0)
    except cv2.error:
        print('ERR:1,请输入完整正确图片路径')


# 绝对路径判断
def isAbsPath(path):
    # 判断操作系统
    os_type = platform.system()
    if os_type == 'Windows':
        if path.find(':') != -1:
            return True
    elif os_type == 'Linux':
        if path[0] == '/':
            return True

    return False


# 绝对路径修正
def AbsPathFix(path):
    if not isAbsPath(path):
        path = os.path.join(os.getcwd(), path)
    return path


if __name__ == '__main__':
    main(sys.argv)
