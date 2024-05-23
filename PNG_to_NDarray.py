# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:43:26 2024

@author: okyaybariss
"""

from PIL import Image
import numpy as np

# PNG dosyasını yükle
image = Image.open("dosya.png")

# Görüntüyü NumPy dizisine dönüştür
image_array = np.array(image)
