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




from reportlab.pdfgen import canvas

# PDF dosyasını oluştur
file_path = "/mnt/data/Isletim_Sistemleri_Sorulari.pdf"
c = canvas.Canvas(file_path)

# Başlık
c.setFont("Helvetica-Bold", 16)
c.drawString(200, 800, "İşletim Sistemleri Soruları")

# Soru 4
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 770, "Soru 4 (İşletim Sistemleri)")
c.setFont("Helvetica", 10)
c.drawString(50, 750, "a) Aşağıdakilerden hangisi ya da hangileri gerçek zamanlı işleme (real-time processing) gerektirir?")
c.drawString(50, 730, "- Bir dosyayı yazıcıda yazdırma")
c.drawString(50, 715, "- Bir bilgisayar oyunu oynama")
c.drawString(50, 700, "- Bir akıllı telefon üzerinde çalışan numarayı gösterme")
c.drawString(50, 685, "- Gelecek senenin ekonomik durumunu öngören bir yazılımı çalıştırma")
c.drawString(50, 670, "- Bir MP3 müziği dinleme")

c.setFont("Helvetica-Bold", 12)
c.drawString(50, 640, "b) Doğru - Yanlış")
c.setFont("Helvetica", 10)
c.drawString(50, 620, "- Gömülü sistemler, genel amaçlı cihazlardır. (Doğru/Yanlış)")
c.drawString(50, 605, "- Disk formatlama programı, bir hizmet yazılımıdır. (Doğru/Yanlış)")
c.drawString(50, 590, "- MS-DOS, metin tabanlı kullanıcı arayüzüdür. (Doğru/Yanlış)")
c.drawString(50, 575, "- Bilgisayar sistemlerinde açılış önyükleyicisi (bootloader), RAM'de saklanır. (Doğru/Yanlış)")
c.drawString(50, 560, "- Önyükleme (booting), işletim sistemini sabit diskten ana belleğe taşır. (Doğru/Yanlış)")

c.setFont("Helvetica", 9)
c.drawString(50, 540, "Not: (a)'da tam puan alabilmek için doğru seçeneği ya da tüm doğru seçenekleri işaretlemeniz gerekmektedir.")
c.drawString(50, 525, "Not: (b)'de doğru ifadeler için √ sembolünü, yanlış ifadeler için X sembolünü kullanınız.")

# Soru 5
c.setFont("Helvetica-Bold", 12)
c.drawString(50, 500, "Soru 5 (İşletim Sistemleri)")
c.setFont("Helvetica", 10)
c.drawString(50, 480, "a) Program ve işlem (process) arasındaki fark nedir?")
c.drawString(50, 465, "b) Bir işletim sisteminde işlemlerden bazıları diğerlerine göre nasıl daha hızlı çalıştırılabilir?")
c.drawString(50, 450, "c) Bir işlem, kendisine tahsis edilen bellek alanının dışına erişebildiğinde tüm makinenin kontrolünü eline nasıl geçirebilir?")
c.drawString(50, 435, "d) Bir işletim sisteminde her zaman dilimi 50 milisaniye ise ve her işlem değişimi en fazla bir mikrosaniye gerektiriyorsa,")
c.drawString(50, 420, "   makine bir saniye içinde kaç işleme hizmet verebilir?")

# PDF'i kaydet
c.save()

file_path
