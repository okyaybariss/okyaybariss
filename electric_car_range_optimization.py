# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 13:07:53 2024

@author: okyaybariss
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Verileri yükleyin
file_path = r"C:\Users\neslihan\OneDrive\Masaüstü\research\electric_car_set.csv"
df = pd.read_csv(file_path, delimiter=';')

# Özellikler (X) ve hedef (y) olarak verileri ayırın
X = df[['TopSpeed_KmH', 'Efficiency_WhKm', 'PriceEuro']]
y = df['Range_Km']

# Eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Doğrusal regresyon modelini eğitin
model = LinearRegression()
model.fit(X_train, y_train)

# Modeli test verileri üzerinde değerlendirin
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Ortalama Kare Hata (MSE):", mse)
print("R-kare değeri:", r2)

# Yeni veriler için tahmin yapın
new_data = {'TopSpeed_KmH': [233], 'Efficiency_WhKm': [161], 'PriceEuro': [55480]}
new_df = pd.DataFrame(new_data)

# Yeni veriler için Range_Km tahmini yapın
prediction = model.predict(new_df)
print("Tahmin edilen Range_Km:", prediction[0])
