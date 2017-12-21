#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2
from scipy.misc import imsave
import os

input_path = '/home/swq/Documents/光流图转RGB图程序脚本/flow_out'
output_path = './flow_contours_output'


def find_contours(input_img_path, input_img_name, out_path):
    img = cv2.imread(input_img_path)
    # print img.shape
    high = img.shape[0]
    weight = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 0, 0), 2)
    for i in range(high):
        for j in range(weight):
            if (img[i, j][0] == 0) and (img[i, j][1] == 0) and (img[i, j][2] == 0):
                pass
            # elif (img[i, j][0] != 255) or (img[i, j][1] != 255) or (img[i, j][2] != 255):
            else:
                img[i, j][0] = 255
                img[i, j][1] = 255
                img[i, j][2] = 255
    # for i in range(high):
    #     for j in range(5):
    #         img[i, j][0] = 0
    #         img[i, j][1] = 0
    #         img[i, j][2] = 0
    # for i in range(high):
    #     for j in range(weight - 5, weight):
    #         img[i, j][0] = 0
    #         img[i, j][1] = 0
    #         img[i, j][2] = 0
    # for i in range(5):
    #     for j in range(weight):
    #         img[i, j][0] = 0
    #         img[i, j][1] = 0
    #         img[i, j][2] = 0
    # for i in range(high - 5, high):
    #     for j in range(weight):
    #         img[i, j][0] = 0
    #         img[i, j][1] = 0
    #         img[i, j][2] = 0
    cv2.imshow('img', img)
    out = os.path.join(out_path, input_img_name)
    imsave(out, img)
    cv2.waitKey(0)


# if __name__ == '__main__':
#     # for i in range(2):
#     #     flowname = os.path.join(input_path, '%05d_flow.png' % (i + 1))
#     #     print i + 1
#     #     find_contours(flowname, '%05d_flow.png' % (i + 1), output_path)
#     img = cv2.imread('./images/00026_flow.png')
#     print img.shape
#     high = img.shape[0]
#     weight = img.shape[1]
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#     image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(img, contours, -1, (0, 0, 255), 2)
#     # for i in range(high):
#     #     for j in range(weight):
#     #         if (img[i, j][0] == 0) and (img[i, j][1] == 0) and (img[i, j][2] == 0):
#     #             pass
#     #         # elif (img[i, j][0] != 255) or (img[i, j][1] != 255) or (img[i, j][2] != 255):
#     #         else:
#     #             img[i, j][0] = 255
#     #             img[i, j][1] = 255
#     #             img[i, j][2] = 255
#     cv2.imshow('img', img)
#     cv2.waitKey(0)


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
    cv2.imshow('canny demo', dst)
    cv2.waitKey(0)


if __name__ == '__main__':

    lowThreshold = 0
    max_lowThreshold = 200
    ratio = 3
    kernel_size = 3

    img = cv2.imread('./images/00026_img1.ppm')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.namedWindow('canny demo')
    #
    # cv2.createTrackbar('Min threshold', 'canny demo', lowThreshold, max_lowThreshold, CannyThreshold)
    #
    # CannyThreshold(0)  # initialization
    # if cv2.waitKey(0) == 27:
    #     cv2.destroyAllWindows()
    CannyThreshold(4)


# def CannyThreshold(lowThreshold, input_img_name, out_path):
#     detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
#     detected_edges = cv2.Canny(detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size)
#     dst = cv2.bitwise_and(img, img, mask=detected_edges)  # just add some colours to edges from original image.
#
#     out = os.path.join(out_path, input_img_name)
#     high = img.shape[0]
#     weight = img.shape[1]
#     for i in range(high):
#         for j in range(weight):
#             if (dst[i, j][0] == 0) and (dst[i, j][1] == 0) and (dst[i, j][2] == 0):
#                 pass
#             else:
#                 dst[i, j][0] = 255
#                 dst[i, j][1] = 255
#                 dst[i, j][2] = 255
#
#     gray2 = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
#     ret, binary = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
#     image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cv2.drawContours(dst, contours, -1, (255, 255, 255), 2)
#     imsave(out, dst)
#
#
# if __name__ == '__main__':
#
#     lowThreshold = 0
#     ratio = 3
#     kernel_size = 3
#
#     for i in range(22872):
#         flowname = os.path.join(input_path, '%05d_flow.png' % (i + 1))
#         print i + 1
#         img = cv2.imread(flowname)
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         CannyThreshold(5, '%05d_flow.png' % (i + 1), output_path)
