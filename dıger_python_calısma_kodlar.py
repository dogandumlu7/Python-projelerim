# from faker import Faker
# fake = Faker('tr_TR')
# print(fake.name())  # Rastgele Türkçe bir isim
# print(fake.email())  # Rastgele bir Türkçe e-posta
# print(fake.country())  # Rastgele bir ülke (Türkçe)
# print(fake.profile())  # Detaylı bir kullanıcı profili





# from turtle import *
# color('red')
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50, 200)  # Yarıçapı 50 olan, 200 derece açıyla bir yay çizecek
# right(140)
# circle(50, 200)  # Yarıçapı 50 olan, 200 derece açıyla başka bir yay çizecek
# forward(133)  # Çizimi tamamlamak için geri dönme
# end_fill()
# done()





# import pywhatkit
# pywhatkit.text_to_handwriting('''Learning Python from the basics is 
# extremely important. Before starting to learn python,understanding a 
# base language like c is a must and 
# some of the oops concepts.Python program has many modulesand packages, 
# which helps with efficient programming.
# Understanding these modules and 1proper usage of many syntax and libraries is recommended.
# In this article, a few modules and packages are used in the program. 
# Python includes tons of libraries and some of them are quiet intresting''')









# import matplotlib.pyplot as plt
# Partition = 'Holidays', 'Eating_Out', 'Shopping', 'Groceries'
# sizes = [250, 100, 300, 200]
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=Partition, autopct='%1.1f%%', shadow=True, startangle=90)         
# ax1.axis('equal')
# plt.show()






# import matplotlib.pyplot as plt
# import numpy as np

# # X ekseni için değerler (0 ile 2π arasında)
# x = np.linspace(0, 2 * np.pi, 500)

# # Y ekseni için değerler
# y_sin = np.sin(x)  # Sinüs dalgası
# y_cos = np.cos(x)  # Kosinüs dalgası

# # Grafik boyutu ayarla
# plt.figure(figsize=(10, 6))

# # Sinüs dalgasını çiz
# plt.plot(x, y_sin, label='Sinüs', color='blue', linewidth=2, linestyle='-')

# # Kosinüs dalgasını çiz
# plt.plot(x, y_cos, label='Kosinüs', color='red', linewidth=2, linestyle='--')

# # Başlık ve etiketler
# plt.title("Sinüs ve Kosinüs Dalgaları", fontsize=16, fontweight='bold')
# plt.xlabel("Açı (Radyan)", fontsize=12)
# plt.ylabel("Değer", fontsize=12)

# # Izgara çizgileri
# plt.grid(color='gray', linestyle='--', linewidth=0.5)

# # Eksen sınırları
# plt.xlim(0, 2 * np.pi)
# plt.ylim(-1.5, 1.5)

# # Gösterge (legend)
# plt.legend(loc='upper right', fontsize=12)

# # Göster
# plt.show()
