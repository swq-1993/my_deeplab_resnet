#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

flow_origin_path = '/flow_origin_1'
flow_contours_path = '/flow_contours_output'
train_txt_path = './dataset'


if __name__ == '__main__':
    train_txt_name = 'train_flow.txt'
    train_txt = os.path.join(train_txt_path, train_txt_name)
    for i in range(22872):
        print i
        f = open(train_txt, 'a')
        flow_origin = os.path.join(flow_origin_path, '%05d_img1.jpg' % (i + 1))
        flow_contours = os.path.join(flow_contours_path, '%05d_flow.png' % (i + 1))
        f.write(flow_origin + ' ' + flow_contours + '\n')
    pass
