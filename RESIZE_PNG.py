# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:47:28 2024

@author: okyaybariss
"""

import cv2
import numpy as np
import os

def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".png") or filename.endswith(".jpg"):  # Dosya uzantısına göre filtreleyin
            img_path = os.path.join(input_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)


            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            _, binary = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                x, y, w, h = cv2.boundingRect(contours[0])
                img = img[y:y+h, x:x+w]


            resized_img = cv2.resize(img, (227, 227))


            output_path = os.path.join(output_dir, filename)
            cv2.imwrite(output_path, resized_img)


input_directory = r"C:\Users\neslihan\OneDrive\Masaüstü\mfcc"
output_directory = r"C:\Users\neslihan\OneDrive\Masaüstü\mfcc_result"

process_images(input_directory, output_directory)