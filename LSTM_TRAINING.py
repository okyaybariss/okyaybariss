# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:21:26 2024

@author: okyaybariss
"""
import os
import numpy as np
import librosa
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense













train_acil_olmayan1 = r"C:\Users\neslihan\OneDrive\Masaüstü\Acil Olmayan Durumlar\train_acil_olmayan1"

# Tüm ses dosyalarının adlarını alın
sesdosyalari = os.listdir(train_acil_olmayan1)

# Ses dosyalarını yüklemek için boş bir liste oluşturun
train_acil_olmayan1_list = []

# Her ses dosyasını yükleyin
for dosya in sesdosyalari:
    dosya_yolu = os.path.join(train_acil_olmayan1, dosya)
    # WAV dosyasını yükle
    ses_verisi, sr = librosa.load(dosya_yolu, sr=None)
    # İstenirse, ses verilerini özellik çıkarma veya başka bir işlem için kullanabilirsiniz
    train_acil_olmayan1_list.append(ses_verisi)

# Ses verilerini bir numpy dizisine dönüştürün
train_acil_olmayan1_np = np.array(train_acil_olmayan1)









# Ses dosyalarının bulunduğu dizini belirtin
train_acil1 = r"C:\Users\neslihan\OneDrive\Masaüstü\Acil Durumlar\train_acil1"

# Tüm ses dosyalarının adlarını alın
sesdosyalari = os.listdir(train_acil1)

# Ses dosyalarını yüklemek için boş bir liste oluşturun
train_acil1_list = []

# Her ses dosyasını yükleyin
for dosya in sesdosyalari:
    dosya_yolu = os.path.join(train_acil1, dosya)
    # WAV dosyasını yükle
    ses_verisi, sr = librosa.load(dosya_yolu, sr=None)
    # İstenirse, ses verilerini özellik çıkarma veya başka bir işlem için kullanabilirsiniz
    train_acil1_list.append(ses_verisi)

# Ses verilerini bir numpy dizisine dönüştürün
train_acil1_np = np.array(train_acil1_list)










# Ses dosyalarının bulunduğu dizini belirtin
test_acil_olmayan1= r"C:\Users\neslihan\OneDrive\Masaüstü\Acil Olmayan Durumlar\test_acil_olmayan1"

# Tüm ses dosyalarının adlarını alın
sesdosyalari = os.listdir(test_acil_olmayan1)

# Ses dosyalarını yüklemek için boş bir liste oluşturun
test_acil_olmayan1_list = []

# Her ses dosyasını yükleyin
for dosya in sesdosyalari:
    dosya_yolu = os.path.join(test_acil_olmayan1, dosya)
    # WAV dosyasını yükle
    ses_verisi, sr = librosa.load(dosya_yolu, sr=None)
    # İstenirse, ses verilerini özellik çıkarma veya başka bir işlem için kullanabilirsiniz
    test_acil_olmayan1_list.append(ses_verisi)

# Ses verilerini bir numpy dizisine dönüştürün
test_acil_olmayan1_np = np.array(test_acil_olmayan1_list)














# Ses dosyalarının bulunduğu dizini belirtin
test_acil1 = r"C:\Users\neslihan\OneDrive\Masaüstü\Acil Durumlar\test_acil1"

# Tüm ses dosyalarının adlarını alın
sesdosyalari = os.listdir(test_acil1)

# Ses dosyalarını yüklemek için boş bir liste oluşturun
test_acil1_list = []

# Her ses dosyasını yükleyin
for dosya in sesdosyalari:
    dosya_yolu = os.path.join(test_acil1, dosya)
    # WAV dosyasını yükle
    ses_verisi, sr = librosa.load(dosya_yolu, sr=None)
    # İstenirse, ses verilerini özellik çıkarma veya başka bir işlem için kullanabilirsiniz
    test_acil1_list.append(ses_verisi)

# Ses verilerini bir numpy dizisine dönüştürün
test_acil1_np = np.array(test_acil1_list)















# Eğitim ve test setlerini yükleme ve dönüştürme adımları burada gerçekleştirilebilir

# Örnek LSTM modeli oluşturma
model = Sequential()
model.add(LSTM(100, input_shape=(1, 2)))
model.add(Dense(1, activation='sigmoid'))

# Modeli derleme
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Modeli eğitim seti ile eğitme
model.fit(train_acil_olmayan1_np, train_acil1_np, epochs=10, batch_size=32, validation_data=(test_acil_olmayan1_np, test_acil1_np))

# Modeli test seti ile değerlendirme
loss, accuracy = model.evaluate(test_acil_olmayan1_np, test_acil1_np)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')
