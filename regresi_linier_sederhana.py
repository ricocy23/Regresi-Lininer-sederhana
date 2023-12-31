# -*- coding: utf-8 -*-
"""Regresi linier sederhana.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1914X70_hOB-nuqb9HPCcnJFzVO3NOwJW

#Import Library
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""#Load Dataset"""

url = 'https://drive.google.com/file/d/1aSX6KOE2ziTOiapQgbWuGiqzGK3Ow594/view?usp=share_link'
file_id=url.split('/')[-2]
dwn_url='https://drive.google.com/uc?id=' + file_id

dataset = pd.read_csv(dwn_url)
print(dataset.tail())

"""#Check the General information"""

dataset.shape

dataset.info()

"""#Handling Missing Values"""

dataset.isnull().sum()

"""#Exploratory Data Analysis (EDA)"""

f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
dataset['Tahun_bekerja'].plot(kind='kde')
f.add_subplot(1,2,2)
plt.boxplot(dataset['Tahun_bekerja'])
plt.show()

f = plt.figure(figsize=(12,4))
f.add_subplot(1,2,1)
dataset['Gaji'].plot(kind='kde')
f.add_subplot(1,2,2)
plt.boxplot(dataset['Gaji'])
plt.show()

import pandas as pd

# Membuat DataFrame contoh
data = {'Tahun_bekerja': [12, 4],
        'Gaji': [5, 4]}
df = pd.DataFrame(data)

# Menggunakan metode corr() untuk menghitung korelasi
korelasi = df['Tahun_bekerja'].corr(df['Gaji'])

print("Korelasi antara Tahun_bekerja dan Gaji adalah:", korelasi)

plt.scatter(dataset['Tahun_bekerja'], dataset['Gaji'])
plt.xlabel('Tahun_Bekerja')
plt.ylabel('Gaji')
plt.title('Scatter Plot Tahun_bekerja vs Gaji')
plt.show()

"""#Splitting Data"""

X = dataset.iloc[:, :-1].values
print(X)

Y = dataset.iloc[:, 1].values
print(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state = 0)
print(X_train.shape)
print(X_train)

"""#Modeling"""

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, Y_train)

print(lin_reg.coef_)
print(lin_reg.intercept_)

"""#Evaluation"""

Y_prediksi = lin_reg.predict(X_test)

df = pd.DataFrame({'aktual': Y_test,'Prediksi': Y_prediksi})
print(df)

df.plot(kind='bar',figsize=(12,4))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y_prediksi))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y_prediksi))
print('Robot Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, Y_prediksi)))

plt.scatter(X_train, Y_train)
plt.plot(X_train, lin_reg.predict(X_train), c='red')
plt.xlabel('Tahun_Bekerja')
plt.ylabel('Gaji')
plt.title('Prediksi Gaji Berdasarkan tahun bekerja (training set)')

plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_prediksi, c='r')
plt.xlabel('Tahun_Bekerja')
plt.ylabel('Gaji')
plt.title('Prediksi Gaji Berdasarkan Tahun Bekerja(Testing set)')

"""#Prediction"""

print('Gaji Seseorang setelah Bekerja selama 2.7 tahun adalah',lin_reg.predict([[2.7]]))
print('Gaji Seseorang setelah Bekerja selama 5.7 tahun adalah',lin_reg.predict([[5.5]]))
print('Gaji Seseorang setelah Bekerja selama 7.7 tahun adalah',lin_reg.predict([[7.5]]))