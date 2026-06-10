def decorator(fonk):
    def wrapper():
        print("fonksiyon çalışmadan önceki işlemler")
        fonk()
        print("fonksiyon çalıştıktan sonraki işlemler")
    return wrapper

# @decorator
def fonksiyon():
    print("fonksiyon çalışıyor")

# fonksiyon()



decorator(fonksiyon)

def fonksiyon():
    print("fonksiyon çalışıyor")


# class kişi:
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age


#     def __str__(self):
#         return f"ad: {self.name}  soyad: {self.surname}   age: {self.age}"


#     def üsalma(self,x=None,y=None):
#         if x == None and y == None:
#             return f"{self.surname} {self.name}"
#         return x**y


# kişi1 = kişi("Doğan", "Dumlu", 19)
# kişi2 = kişi("Ayşe","Dumlu", 20)
# kişi3 = kişi("Asya", "Dumlu", 3)



# print(f"ad: {kişi1.name}  soyad: {kişi1.surname}   age: {kişi1.age}")
# print(f"ad: {kişi2.name}  soyad: {kişi2.surname}   age: {kişi2.age}")
# print(f"ad: {kişi3.name}  soyad: {kişi3.surname}   age: {kişi3.age}")

# print(kişi1)
# print(kişi2)
# print(kişi3)

# print(kişi1.üsalma(3,4))
# print(kişi1.üsalma())






# _lt_: < operatörünü tanımlar.

# _le_: <= operatörünü tanımlar.

# _gt_: > operatörünü tanımlar.

# _ge_: >= operatörünü tanımlar.

# _eq_: == operatörünü tanımlar.

# _ne_: != operatörünü tanımlar.





# class OverloadComparison:
#     def __init__(self, num):  # Doğru yazım
#         self.num = num

#     def __lt__(self, obj2):  # Doğru yazım
#         return self.num < obj2.num

#     def __le__(self, obj2):
#         return self.num <= obj2.num

#     def __gt__(self, obj2):
#         return self.num > obj2.num

#     def __ge__(self, obj2):
#         return self.num >= obj2.num

#     def __eq__(self, obj2):
#         return self.num == obj2.num

#     def __ne__(self, obj2):
#         return self.num != obj2.num


# # İki nesne oluşturulmalı
# x = OverloadComparison(34)
# y = OverloadComparison(12)

# # Doğru karşılaştırma
# print(x < y)  # False









# import math

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __add__(self, other):
#         """Toplama: İki vektörün bileşenleri toplanır."""
#         return Vector(self.a + other.a, self.b + other.b)

#     def __sub__(self, other):
#         """Çıkarma: İki vektörün bileşenleri çıkarılır."""
#         return Vector(self.a - other.a, self.b - other.b)

#     def __mul__(self, scalar):
#         """Çarpma: Vektör bir skalerle çarpılır."""
#         return Vector(self.a * scalar, self.b * scalar)

#     def __abs__(self):
#         """Mutlak Değer: Vektörün büyüklüğünü hesaplar."""
#         return math.sqrt(self.a**2 + self.b**2)

#     def __eq__(self, other):
#         """Eşitlik: İki vektörün bileşenlerinin eşit olup olmadığını kontrol eder."""
#         return self.a == other.a and self.b == other.b

#     def __repr__(self):
#         """Vektör yazdırmayı tanımlar."""
#         return f"Vector({self.a}, {self.b})"

# # Örnek Kullanım
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)

# # Toplama
# toplam = v1 + v2
# print(f"{v1} + {v2} = {toplam}")

# # Çıkarma
# cikarma = v1 - v2
# print(f"{v1} - {v2} = {cikarma}")

# # Skaler Çarpma
# skaler_carpim = v1 * 2
# print(f"{v1} * 2 = {skaler_carpim}")

# # Mutlak Değer
# mutlak_deger = abs(v1)
# print(f"|{v1}| = {mutlak_deger}")

# # Eşitlik
# vektor_esitligi = v1 == v2
# print(f"{v1} == {v2} ? {vektor_esitligi}")









# class kitap:
#     def __init__(self,başlık,yazar,tür,ücret):
#         self.başlık = başlık
#         self.yazar = yazar
#         self.tür = tür
#         self.ücret = ücret

#     def __str__(self):
#         return f"Kitabın: \nAdı: {self.başlık} \nYazarı: {self.yazar} \nTürü: {self.tür} \nÜcreti: {self.ücret}"



# kitap = kitap("Bir kürt sevdim", "Dilek Bilgiç Esen", "Roman", "180")
# print(kitap)






# class kitapçı:
#     kitaplar = []
#     def __init__(self,kitap_adı):
#         self.kitap_adı = kitap_adı

#     def kitap_ekle(self):
#         kitapçı.kitaplar.append(self.kitap_adı)
#         print(f"{self.kitap_adı} listeye eklendi")

#     def kitap_çıkar(self):
#         if self.kitap_adı in kitapçı.kitaplar:
#             kitapçı.kitaplar.remove(self.kitap_adı)
#             print(f"{self.kitap_adı } silindi")
#             print(kitapçı.kitaplar)
#         else :
#             print(f"listede {self.kitap_adı} adında kitap bulunamadı")

#     def kitap_ara(kitap_ara):
#         print(f"{kitapçı.kitaplar}")
#         if kitap_ara in kitapçı.kitaplar:
#             print(f"{kitap_ara} kitabı listede vardr")
#         else:
#             print(f"{kitap_ara} kitabı listede yoktur")



# k1 = kitapçı("Bir kürt sevdim")
# k2 = kitapçı("havanın üç kızı")
# k3 = kitapçı("beyaz diş")
# k4 = kitapçı("bach yürken")

# k1.kitap_ekle()
# k2.kitap_ekle()
# k3.kitap_ekle()
# k4.kitap_ekle()

# kitapçı.kitap_ara("beyaz diş")
# kitapçı.kitap_ara("ölmek kolaydır sevmekten")
# k3.kitap_çıkar()








# class Kitap:
#     def __init__(self, baslik, yazar):
#         self.baslik = baslik
#         self.yazar = yazar

#     def __str__(self):
#         return f"{self.baslik} - {self.yazar}"

# class kitapci:
#     kitaplar = []
#     def __init__(self, ad):
#         self.ad = ad

#     def kitap_ekle(kitap):
#         kitapci.kitaplar.append(kitap)
#         print(f"{kitap} eklendi.")

#     def kitap_cikar(kitap):
#         if kitap in kitapci.kitaplar:
#             kitapci.kitaplar.remove(kitap)
#             print(f"{kitap} çıkarıldı.")
#         else:
#             print(f"{kitap} bulunamadı.")

#     def kitap_ara(arama_kriteri):
#         bulunan_kitaplar = [kitap for kitap in kitapci.kitaplar if arama_kriteri.lower() in kitap.baslik.lower() or arama_kriteri.lower() in kitap.yazar.lower()]
#         if bulunan_kitaplar:
#             for kitap in bulunan_kitaplar:
#                 print(kitap)
#         else:
#             print("Kitap bulunamadı.")

# # Örnek kullanım
# kitap1 = Kitap("Savaş ve Barış", "Lev Tolstoy")
# kitap2 = Kitap("Suç ve Ceza", "Fyodor Dostoyevski")
# kitap3 = Kitap("1984", "George Orwell")

# # kitapci = Kitapci("Kitap Dünyası")
# kitapci.kitap_ekle(kitap1)
# kitapci.kitap_ekle(kitap2)
# kitapci.kitap_ekle(kitap3)

# kitapci.kitap_ara("Savaş")
# kitapci.kitap_ara("Orwell")

# kitapci.kitap_cikar(kitap2)
# kitapci.kitap_ara("Dostoyevski")









# class kişi:
#     def __init__(self,ad,soyad,numara):
#         self.ad = ad
#         self.soyad = soyad
#         self.numara = numara

#     def __str__(self):
#         return f"ad: {self.ad}    soyad: {self.soyad}    numara: {self.numara}"

#     def __doğan__(self):
#         print("kod çalışıcak")
#         return 3**4
#         print("kod çalışmicak")



# # k1 = kişi("Doğan", "Dumlu", "240706012")

# # print(k1)
# # print(k1.ad, k1.soyad, k1.numara)

# # print(k1.__doğan__())
# # print(kişi.__doğan__(k1))
# # k1.__doğan__()




# class çalışan(kişi):
#     çalışanlar = []
#     çalışan_sayısııı = 0
#     numara = []
#     def __init__(self,ad,soyad,numara,meslek,alan):
#         super().__init__(ad, soyad, numara)
#         self.meslek = meslek
#         self.alan = alan


#     def __str__(self):
#         return f"ad: {self.ad}  soyad: {self.soyad}  numara: {self.numara}  meslek: {self.meslek}  alan: {self.alan}"


#     def çalışan_ekle(self):
#         çalışan.çalışanlar.append(f"ad: {self.ad}  soyad: {self.soyad}  numara: {self.numara}  meslek: {self.meslek}  alan: {self.alan}")
#         çalışan.numara.append(self.numara)
#         çalışan.çalışan_sayısııı += 1
#         print(f"Çalışan bilgileri eklendi")



#     def Çalışan_sil(self):
#         # if f"ad: {self.ad}  soyad: {self.soyad}  numara: {self.numara}  meslek: {self.meslek}  alan: {self.alan}" in çalışan.çalışanlar:
#         #     çalışan.çalışanlar.remove(f"ad: {self.ad}  soyad: {self.soyad}  numara: {self.numara}  meslek: {self.meslek}  alan: {self.alan}")
#         #     print(f"{self.numara} numaralı çalışan silindi")
#         #     çalışan.çalışan_sayısııı -= 1
#         y = -1
#         for x in çalışan.numara:
#             y += 1
#             if x == self.numara:
#                 break

#         if self.numara in çalışan.numara:
#             çalışan.çalışanlar.remove(çalışan.çalışanlar[y])
#             çalışan.numara.remove(self.numara)
#             print(f"{self.numara} numaralı çalışan silindi")
#             çalışan.çalışan_sayısııı -= 1
#         else:
#             print("Çalışan bulunamadı")


#     def çalışan_sayısı():
#         print(f"çalışan sayısı: {çalışan.çalışan_sayısııı}")


#     def çalışan_kimler():
#         print("Çalışanlar: ")
#         for x in çalışan.çalışanlar:
#             print(f"     {x}")


#     def çalışan_ara(self):
#         if self.numara in çalışan.numara:
#             print(f"{self.numara} numaralı çalışan vardırr")
#             for x in çalışan.çalışanlar:
#                 if not x.find(str(self.numara)) == -1:
#                     print(f"aradığınız çalışan => {x}")
#         else:
#             print(f"{self.numara} numaralı çalışan yoktur")



# ç1 = çalışan("Doğan", "dumlu", 24070612, "B.M", "Programlama")
# ç2 = çalışan("Ayşe", "kornek", 24070613, "hazılık", "yok")
# ç3 = çalışan("Mahir","Dumlu", 24070614, "okuyor", "3.sınıf")

# ç1.çalışan_ekle()
# ç2.çalışan_ekle()
# ç3.çalışan_ekle()

# çalışan.çalışan_sayısı()
# çalışan.çalışan_kimler()
# print("çalışan numaraları => ",çalışan.numara)

# ç2.Çalışan_sil()
# ç1.Çalışan_sil()

# çalışan.çalışan_sayısı()
# çalışan.çalışan_kimler()


# print("çalışan numaraları => ",çalışan.numara)

# ç3.çalışan_ara()
# ç1.çalışan_ara()








# class çember:
#     def __init__(self,x,y,r):
#         self.x = x
#         self.y = y
#         self.r = r

#     def setter(self):
#         self.r = r
#     def getter(self):
#         return self.r

#     def __lt__(self,other):
#         return self.r < other.r



# ç1 = çember(15,20,50)
# ç2 = çember(10,6,32)

# print(f"çemberin x ekseni: {ç1.x}   çemberin y ekseni: {ç1.y}  çemberin yarıçapı:{ç1.r}")
# print(f"çemberin x ekseni: {ç2.x}   çemberin y ekseni: {ç2.y}  çemberin yarıçapı:{ç2.r}")
# print(ç1.getter())
# print(ç2.getter())

# print(ç2<ç1)









# while True:
#     x = input("==> ")

#     if x == "0":
#         break

#     elif x == x[::-1]:
#         print("palindromal")

#     else:
#         print("palindromal değil")









# l1 = [[1,2], [3,4]]
# l2 = []

# def fonc(list):
#     for x in list:
#         if type(x) == type(list):
#             fonc(x)
#         else:
#             l2.append(x)
#     return l2

# print(fonc(l1))








# class kişi:
#     def __init__(self,ad,soyad):
#         self.ad = ad
#         self.soyad = soyad
#         self.yaş = None

#     def setter(self,yaş):
#         self.yaş = yaş
#         print(f"{self.ad} kişisinin yaşı güncellendi")

#     def getter(self):
#         return self.yaş



# class işçi(kişi):
#     def __init__(self,ad,soyad,lisans = None,doktora = None):
#         super().__init__(ad,soyad)
#         self.lisans = lisans
#         self.doktora = doktora

#     def setter2(self,lisans2 = None, doktora2 = None):
#         self.lisans = lisans2
#         self.doktora = doktora2
#         print(f"{self.ad} işçisinin eğtim bilgisi güncellendi")

#     def __str__(self):
#         return f"ad: {self.ad}   soyad: {self.soyad}   yaş: {self.yaş}  lisans:{self.lisans}   doktora: {self.doktora}"


# işçi1 = işçi("Caner","yudum" , "bilgisayar" , "AI")
# print((işçi1))
# işçi1.setter(12)
# işçi1.setter2("inşaat","AI")
# print(işçi1)
# print(işçi1.getter())


# print("-------------"*5)


# işçi2 = işçi("Kayra","ateş" , "makina" , "AI")
# print(işçi2)
# işçi2.setter(14)
# işçi2.setter2("Elektrik","AI")
# print(işçi2)
# print(işçi2.getter())











# def fonksiyon(x):
#     if x == 1:
#         return 0
#     elif x == 0:
#         return 0
#     elif x%2==0:
#         return x + fonksiyon(x-2)
#     else:
#         return fonksiyon(x-1)


# print(fonksiyon(12))
# print(fonksiyon(7))









# class kişi:
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad

# class öğrenci(kişi):
#     def __init__(self,ad,soyad,öğrenci_no=None,yemek=None):
#         super().__init__(ad,soyad)
#         self.öğrenci_no = öğrenci_no
#         self.yemek = yemek

#     def setter(self,yeni_yemek):
#         self.yemek = yeni_yemek
#     def getter(self):
#         return self.yemek



# class Menü:
#     sayaç = 0
#     def __init__(self,çorba,ana_yemek,salata,tatlı):
#         if Menü.sayaç >= 1000:
#             raise Exception("Yeni Menu nesnesi oluşturulamaz, sayaç sınırı aşıldı.")
#         Menü.sayaç += (Menü.sayaç <= 1000) * 1  # Sayaç artırma işlemi
#         assert Menü.sayaç <= 1000, "Yeni Menu nesnesi oluşturulamaz, sayaç sınırı aşıldı."
#         self.çorba = çorba
#         self.ana_yemek = ana_yemek
#         self.salata = salata
#         self.tatlı = tatlı

#     def yemek(self):
#         return f"çorba: {self.çorba}    ana yemek: {self.ana_yemek}    salata: {self.salata}   tatlı: {self.tatlı}"


# m1 = Menü("mercimek çorbası", "etli pilav", "çoban salatası","kazan dibi")
# ö1 = öğrenci("Doğan","Dumlu",345)

# print(ö1.getter())

# ö1.setter(m1.yemek())

# print(ö1.getter())



# for x in range(999):
#     Menü("mercimek çorbası", "etli pilav", "çoban salatası","kazan dibi")
# print(Menü.sayaç)

# Menü("mercimek çorbası", "etli pilav", "çoban salatası","kazan dibi")








# class Kisi:
#     def __init__(self, ad, soyad):
#         self.ad = ad
#         self.soyad = soyad

# class Ogrenci(Kisi):
#     def __init__(self, ad, soyad, ogr_no=None, yemek=None):
#         super().__init__(ad, soyad)
#         self.ogr_no = ogr_no
#         self._yemek = yemek

#     @property
#     def yemek(self):
#         return self._yemek

#     @yemek.setter
#     def yemek(self, yeni_yemek):
#         self._yemek = yeni_yemek

# class Menu:
#     sayac = 0

#     def __new__(cls, *args, **kwargs):
#         if cls.sayac >= 1000:
#             raise Exception("Yeni Menu nesnesi oluşturulamaz, sayaç sınırı aşıldı.")
#         cls.sayac += 1
#         return super(Menu, cls).__new__(cls)

#     def __init__(self, corba, ana, salata, tatli):
#         self.corba = corba
#         self.ana = ana
#         self.salata = salata
#         self.tatli = tatli

# Örnek kullanım
# ogrenci = Ogrenci("Ahmet", "Yılmaz")
# menu = Menu("Mercimek", "Kebap", "Çoban", "Baklava")

# ogrenci.yemek = menu

# print(f"Öğrencinin adı: {ogrenci.ad} {ogrenci.soyad}")
# print(f"Öğrencinin yemeği: Çorba - {ogrenci.yemek.corba}, Ana - {ogrenci.yemek.ana}, Salata - {ogrenci.yemek.salata}, Tatlı - {ogrenci.yemek.tatli}")


# for x in range(999):
#     x = Menu("Mercimek", "Kebap", "Çoban", "Baklava")

# print(Menu.sayac)








# def mukemmel_sayı(x1,x2):
#     z = []
#     for x in range (x1,x2):
#         a = x-1
#         c = 0
#         while 0<a:
#             if x%a == 0:
#                 c += a
#             a -= 1
#         if x == c:
#             z.append(x)
#     print(f"{x1-1} ve {x2} arasındaki mükemmel sayılar: {z}")
            
# mukemmel_sayı(33550335,33550337)
# mukemmel_sayı(1,500)





# for i in range(100,40,-5):
#     c = i/20
#     print(i,":",c)







































































