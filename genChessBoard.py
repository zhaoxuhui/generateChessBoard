# coding=utf-8
import cv2
import numpy as np
import sys

if sys.argv.__len__() == 2 and sys.argv[1] == "help":
    print("用于生成相机标定棋盘格\n")
    print("脚本启动命令格式：")
    print("scriptname.py:[ROW] [COL] [DPI] [IMG_PATH]")
    print("\n脚本帮助:")
    print("[ROW]:棋盘格行数")
    print("[COL]:棋盘格列数")
    print("[DPI]:棋盘格每个格子的分辨率，如256")
    print("[IMG_PATH]:生成的棋盘格图片文件保存文件名")
elif sys.argv.__len__() == 5:
    rows = int(sys.argv[1])
    cols = int(sys.argv[2])
    dpi = int(sys.argv[3])
    img_path = sys.argv[4]

    black_white_flag = False
    line1 = np.zeros([dpi, dpi], np.uint8)
    line2 = np.zeros([dpi, dpi], np.uint8) + 255
    for i in range(cols):
        if black_white_flag:
            tem_block = np.zeros([dpi, dpi], np.uint8)
            line1 = np.hstack((line1, tem_block))
            line2 = np.hstack((line2, tem_block + 255))
            black_white_flag = False
        else:
            tem_block = np.zeros([dpi, dpi], np.uint8) + 255
            line1 = np.hstack((line1, tem_block))
            line2 = np.hstack((line2, tem_block - 255))
            black_white_flag = True

    img = line1
    for i in range(rows):
        if i % 2:
            img = np.vstack((img, line1))
        else:
            img = np.vstack((img, line2))

    cv2.imwrite(img_path, img)
    print("ChessBoard was saved.")
else:
    print("Input \"scriptname.py help\" for help information.")
