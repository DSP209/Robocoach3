#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:10:02 2017

@author: david
"""
import os
import numpy as np,cv2
fn = 'drop.avi'

cd = os.getcwd()
cap = cv2.VideoCapture(cd+'/'+fn,0)

video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
fr = int(cap.get(cv2.CAP_PROP_FPS ))
fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT ))
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))

stat = cap.isOpened()