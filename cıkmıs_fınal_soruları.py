# n = 5
# for i in range(n):
#     for j in range(i):
#         print('* ', end="")
#     print('')
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('')








# class Cember:
#     def __init__(self, x, y, r):
#         self.x = x
#         self.y = y
#         self.r = r

#     # Getter metodu
#     def get_yaricap(self):
#         return self.r

#     # Setter metodu
#     def set_yaricap(self, yeni_yaricap):
#         self.r = yeni_yaricap

#     # Küçüktür operatörünü yeniden tanımlayan metod
#     def __lt__(self, other):
#         return self.r < other.r

#     def __str__(self):
#         return f"Merkez: ({self.x}, {self.y}), Yarıçap: {self.r}"

# # Yeni Çember nesneleri oluşturma
# cember1 = Cember(10, 15, 50)
# cember2 = Cember(20, 25, 30)

# # Yarıçapları karşılaştırma
# if cember1 < cember2:
#     print(f"{cember1} çemberinin yarıçapı {cember2} çemberinin yarıçapından küçüktür.")
# else:
#     print(f"{cember1} çemberinin yarıçapı {cember2} çemberinin yarıçapından büyük veya eşittir.")









# x = input(": ")
# y = x[::-1]
# if x==y:
#     print(f"{x} palindromaldir")
# else:
#     print(f"{x} palinromal değildir")






"""

try:
    # Hata oluşturabilecek kod

    try: Bu blok, potansiyel olarak hata oluşturabilecek kodu içerir.
    Eğer bir hata oluşursa, kontrol except bloğuna geçer.



except SomeException:
    # Hata durumunda çalışacak kod

    except: Bu blok, try bloğunda bir hata oluştuğunda çalıştırılır.
    Hatanın türüne göre farklı except blokları kullanılabilir.



else:
    # Hata oluşmazsa çalışacak kod

    else: Bu blok, try bloğunda hata oluşmadığında çalıştırılır.
    Yani, try bloğu başarılı bir şekilde tamamlanırsa else bloğu çalışır.



finally:
    # Her durumda çalışacak kod

    finally: Bu blok, hata oluşup oluşmadığına bakılmaksızın her zaman çalıştırılır.
    Genellikle kaynakları serbest bırakmak veya temizleme işlemleri için kullanılır.



assert condition, "Hata mesajı"

    assert: Bu anahtar kelime, belirli bir koşulun doğru olup olmadığını kontrol eder.
    Eğer koşul yanlışsa, bir AssertionError istisnası oluşturur.


"""






# d = {0:0, 1:1}
# def fib1(n, d):
#     if n in d:
#         return d[n]
#     else:
#         sonuc = fib1(n-1, d) + fib1(n-2, d)
#         d[n] = sonuc
#         return sonuc

# def fib2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib2(n-1) + fib2(n-2)

# print(fib1(10,d))
# print(fib2(10))






# x = int(input(":"))

# y = 0
# for i in range (1,x):
#     for j in range (1,x):
#         if (i**2) + (j**2) == x:
#             c = j
#             k = i
#             y += 1

# if y > 0:
#     print(f"{x}, {c} ve {k} sayılarının kareleri toplamına eşittir")
#     print(int(y/2))

# else :
#     print(f"{x}, herhangi iki tam sayının kareleri toplamına eşit değildir")






# lst = [4,3,2,5,6,1]

# def insertion(lst):
#     for i in range(1, len(lst)):
#         key = lst[i]
#         j = i-1
#         while j >= 0 and key < lst[j] :
#             lst[j + 1] = lst[j]
#             j -= 1
#         lst[j + 1] = key
#     print(lst)


# insertion(lst)









# lst = [[1,2],[3,4],[9,5]]

# z = []

# def fuc(lst):
#     for x in lst:
#         if type(x) == type(z):
#             fuc(x)
#         else:
#             z.append(x)
#     return z

# print(fuc(lst))








    
# class Kisi:
#     def __init__(self, ad, soyad, yas=None):
#         self._ad = ad
#         self._soyad = soyad
#         self._yas = yas

#     # Getter metodları
#     def get_ad(self):
#         return self._ad

#     def get_soyad(self):
#         return self._soyad

#     def get_yas(self):
#         return self._yas

#     # Setter metodları
#     def set_ad(self, ad):
#         self._ad = ad

#     def set_soyad(self, soyad):
#         self._soyad = soyad

#     def set_yas(self, yas):
#         if yas is None or yas > 0:
#             self._yas = yas
#         else:
#             print("Yaş negatif olamaz!")

# # Kullanım
# kisi = Kisi("Ahmet", "Yılmaz")
# print(f"Ad: {kisi.get_ad()}, Soyad: {kisi.get_soyad()}, Yaş: {kisi.get_yas()}")  # Ad: Ahmet, Soyad: Yılmaz, Yaş: None

# kisi.set_yas(30)
# print(f"Ad: {kisi.get_ad()}, Soyad: {kisi.get_soyad()}, Yaş: {kisi.get_yas()}")  # Ad: Ahmet, Soyad: Yılmaz, Yaş: 30









# class Kisi:
#     def __init__(self, ad, soyad, yas=None):
#         self._ad = ad
#         self._soyad = soyad
#         self._yas = yas

#     # Getter metodları
#     def get_ad(self):
#         return self._ad

#     def get_soyad(self):
#         return self._soyad

#     def get_yas(self):
#         return self._yas

#     # Setter metodları
#     def set_ad(self, ad):
#         self._ad = ad

#     def set_soyad(self, soyad):
#         self._soyad = soyad

#     def set_yas(self, yas):
#         if yas is None or yas > 0:
#             self._yas = yas
#         else:
#             print("Yaş negatif olamaz!")

# # İşçi altsınıfı
# class Isci(Kisi):
#     def __init__(self, ad, soyad, yas=None, lisans=None, doktora=None):
#         super().__init__(ad, soyad, yas)
#         self._lisans = lisans
#         self._doktora = doktora

#     # Getter metodları
#     def get_lisans(self):
#         return self._lisans

#     def get_doktora(self):
#         return self._doktora

#     # Setter metodları
#     def set_lisans(self, lisans):
#         self._lisans = lisans

#     def set_doktora(self, doktora):
#         self._doktora = doktora

# # Kullanım
# isci = Isci("Ahmet", "Yılmaz")
# print(f"Ad: {isci.get_ad()}, Soyad: {isci.get_soyad()}, Yaş: {isci.get_yas()}, Lisans: {isci.get_lisans()}, Doktora: {isci.get_doktora()}")  
# # Çıktı: Ad: Ahmet, Soyad: Yılmaz, Yaş: None, Lisans: None, Doktora: None

# isci.set_lisans("Mühendislik")
# isci.set_doktora("Bilgisayar Bilimleri")
# print(f"Ad: {isci.get_ad()}, Soyad: {isci.get_soyad()}, Yaş: {isci.get_yas()}, Lisans: {isci.get_lisans()}, Doktora: {isci.get_doktora()}")  
# # Çıktı: Ad: Ahmet, Soyad: Yılmaz, Yaş: None, Lisans: Mühendislik, Doktora: Bilgisayar Bilimleri












# class Kisi:
#     def __init__(self, ad, soyad, yas=None):
#         self._ad = ad
#         self._soyad = soyad
#         self._yas = yas

#     # Getter metodları
#     def get_ad(self):
#         return self._ad

#     def get_soyad(self):
#         return self._soyad

#     def get_yas(self):
#         return self._yas

#     # Setter metodları
#     def set_ad(self, ad):
#         self._ad = ad

#     def set_soyad(self, soyad):
#         self._soyad = soyad

#     def set_yas(self, yas):
#         if yas is None or yas > 0:
#             self._yas = yas
#         else:
#             print("Yaş negatif olamaz!")

# # İşçi altsınıfı
# class Isci(Kisi):
#     def __init__(self, ad, soyad, yas=None, lisans=None, doktora=None):
#         super().__init__(ad, soyad, yas)
#         self._lisans = lisans
#         self._doktora = doktora

#     # Getter metodları
#     def get_lisans(self):
#         return self._lisans

#     def get_doktora(self):
#         return self._doktora

#     # Setter metodları
#     def set_lisans(self, lisans):
#         self._lisans = lisans

#     def set_doktora(self, doktora):
#         self._doktora = doktora

#     # Eğitim bilgilerini güncelleyen setter metodu
#     def set_egitim(self, egitim_dict):
#         if 'lisans' in egitim_dict:
#             self._lisans = egitim_dict['lisans']
#         if 'doktora' in egitim_dict:
#             self._doktora = egitim_dict['doktora']

# # Kullanım
# isci = Isci("Ahmet", "Yılmaz")
# print(f"Ad: {isci.get_ad()}, Soyad: {isci.get_soyad()}, Lisans: {isci.get_lisans()}, Doktora: {isci.get_doktora()}")  
# # Çıktı: Ad: Ahmet, Soyad: Yılmaz, Lisans: None, Doktora: None

# egitim_bilgileri = {'lisans': 'Mühendislik', 'doktora': 'Bilgisayar Bilimleri'}
# isci.set_egitim(egitim_bilgileri)
# print(f"Ad: {isci.get_ad()}, Soyad: {isci.get_soyad()}, Lisans: {isci.get_lisans()}, Doktora: {isci.get_doktora()}")  
# # Çıktı: Ad: Ahmet, Soyad: Yılmaz, Lisans: Mühendislik, Doktora: Bilgisayar Bilimleri







# def pozitif_sayi_mi(sayi):
#     assert sayi > 0, "Sayı pozitif olmalı!"
#     return f"{sayi} pozitif bir sayıdır."

# # Kullanım
# print(pozitif_sayi_mi(5))  # 5 pozitif bir sayıdır.
# print(pozitif_sayi_mi(-3))  # AssertionError: Sayı pozitif olmalı!









# x = int(input(":"))
# x = str(x)
# y = len(x)
# k = 0
# for i in x:
#     i = int(i)
#     c = i**y
#     k += c

# if k == int(x):
#     print(f"{x} bir armstrong sayıdır")

# else:
#     print(f"{x} bir armstrong sayı değildir")








# def fonksiyon(lst):
#     n = len(lst)
#     total = 0
#     product = 1
#     for i in range(n):
#         total += lst[i][-1]
#     for i in range(n):
#         product *= lst[i][0]
#     return total, product

# print(fonksiyon([120, 244, 848]))   
# """ hatallı """









# def cift_sayi_toplami(n):
#     if n < 0:
#         return 0
#     elif n % 2 == 0:
#         return n + cift_sayi_toplami(n - 2)
#     else:
#         return cift_sayi_toplami(n - 1)

# # Örnek kullanım
# print(cift_sayi_toplami(7))  # Çıktı: 12
# print(cift_sayi_toplami(10))  # Çıktı: 30






# """
# Bir Kişi sınıfı oluşturacaksınız. Bu sınıfın: örnek nesneleri 
# sadece adı ve soyadı nitelikleri ile oluşturulabilsin
# """


# class Kisi:
#     def __init__(self, ad, soyad):
#         self.ad = ad
#         self.soyad = soyad

#     def __str__(self):
#         return f"{self.ad} {self.soyad}"

# # Kişi sınıfından bir örnek nesne oluşturma
# kisi = Kisi("Doğan", "Dumlu")
# print(kisi)







# """
# Bir Öğrenci altsınıfı tanımlayacaksınız. Bu, Kişi sınıfının bütün niteliklerine 
# ek olarak öğrenci no ve yemek olmak üzere iki ek nitelik daha içersin ve örnek 
# oluşturulurken bunları girmeye gerek olmasın, yani varsayılan None olsun     """


# class Kisi:
#     def __init__(self, ad, soyad):
#         self.ad = ad
#         self.soyad = soyad

#     def __str__(self):
#         return f"{self.ad} {self.soyad}"

# class Ogrenci(Kisi):
#     def __init__(self, ad, soyad, ogrenci_no=None, yemek=None):
#         super().__init__(ad, soyad)
#         self.ogrenci_no = ogrenci_no
#         self.yemek = yemek

#     def __str__(self):
#         return f"{self.ad} {self.soyad}, Öğrenci No: {self.ogrenci_no}, Yemek: {self.yemek}"

# # Ogrenci sınıfından bir örnek nesne oluşturma
# ogrenci = Ogrenci("Doğan", "Dumlu")
# print(ogrenci)






# """
# Yemek niteliği için bir setter ve bir getter metodu tanımlayın
# """

# class Kisi:
#     def __init__(self, ad, soyad):
#         self.ad = ad
#         self.soyad = soyad

#     def __str__(self):
#         return f"{self.ad} {self.soyad}"

# class Ogrenci(Kisi):
#     def __init__(self, ad, soyad, ogrenci_no=None, yemek=None):
#         super().__init__(ad, soyad)
#         self.ogrenci_no = ogrenci_no
#         self.yemek = yemek

#     def __str__(self):
#         return f"{self.ad} {self.soyad}, Öğrenci No: {self.ogrenci_no}, Yemek: {self.yemek}"

#     # Getter metodu
#     def get_yemek(self):
#         return self.yemek

#     # Setter metodu
#     def set_yemek(self, yemek):
#         self.yemek = yemek

# # Ogrenci sınıfından bir örnek nesne oluşturma
# ogrenci = Ogrenci("Ali", "Veli")

# # Yemek niteliğini ayarlama
# ogrenci.set_yemek("Karnıyarık")
# print(ogrenci)

# # Yemek niteliğini alma
# print("Yemek:", ogrenci.get_yemek())






# """
# Bir günlük Menü sınıfı oluşturacaksınız. Bu sınıfın: örnek nesneleri çorba, 
# ana yemek, salata ve tatlı nitelikleri ile oluşturulabilsin. (7 puan) Bu sınıfın 
# bir sınıf niteliği olarak sayaç bulunsun ve her örnek Menü nesnesi 
# oluşturulduğunda bir artırılsın                                      """


# class Menu:
#     sayac = 0  # Sınıf niteliği olarak sayaç

#     def __init__(self, corba, ana_yemek, salata, tatli):
#         self.corba = corba
#         self.ana_yemek = ana_yemek
#         self.salata = salata
#         self.tatli = tatli
#         Menu.sayac += 1  # Her yeni nesne oluşturulduğunda sayaç artırılır

#     def __str__(self):
#         return f"Çorba: {self.corba}, Ana Yemek: {self.ana_yemek}, Salata: {self.salata}, Tatlı: {self.tatli}"

# # Menü sınıfından örnek nesneler oluşturma
# menu1 = Menu("Mercimek Çorbası", "Karnıyarık", "Çoban Salata", "Baklava")
# menu2 = Menu("Ezogelin Çorbası", "Tavuk Sote", "Mevsim Salata", "Sütlaç")

# print(menu1)
# print(menu2)
# print(f"Oluşturulan Menü sayısı: {Menu.sayac}")








# """Ancak, sayaç 1000’i geçmediği sürece yeni Menü örnekleri üretilebilmeli. 
# Bu işlevi if komutu kullanmadan bir satır kod ile nasıl yazarız     """


# class Menu:
#     sayac = 0  # Sınıf niteliği olarak sayaç

#     def __init__(self, corba, ana_yemek, salata, tatli):
#         self.corba = corba
#         self.ana_yemek = ana_yemek
#         self.salata = salata
#         self.tatli = tatli
#         if Menu.sayac < 1000:  # Sayaç 1000'i geçmediği sürece artırılır
#             Menu.sayac += 1

#     def __str__(self):
#         return f"Çorba: {self.corba}, Ana Yemek: {self.ana_yemek}, Salata: {self.salata}, Tatlı: {self.tatli}"

# # Menü sınıfından örnek nesneler oluşturma
# for _ in range(1003):  # 1000'den fazla örnek üretmeye çalışalım
#     menu = Menu("Mercimek Çorbası", "Karnıyarık", "Çoban Salata", "Baklava")

# print(f"Oluşturulan Menü sayısı: {Menu.sayac}")









# """
# Menü sınıfının bir nesnesi olarak bir örnek yemek oluşturun ve bir değişkene 
# atayın. Aynı şekilde bir örnek öğrenci nesnesi oluşturun (niteliklerini siz belirleyin)  """


# class Menu:
#     sayac = 0  # Sınıf niteliği olarak sayaç

#     def __init__(self, corba, ana_yemek, salata, tatli):
#         self.corba = corba
#         self.ana_yemek = ana_yemek
#         self.salata = salata
#         self.tatli = tatli

#         if Menu.sayac < 1000:   #  Sayaç 1000'i geçmediği sürece artırılır
#             Menu.sayac += 1 

#     def __str__(self):
#         return f"Çorba: {self.corba}, Ana Yemek: {self.ana_yemek}, Salata: {self.salata}, Tatlı: {self.tatli}"

# class Kisi:
#     def __init__(self, ad, soyad):
#         self.ad = ad
#         self.soyad = soyad

#     def __str__(self):
#         return f"{self.ad} {self.soyad}"

# class Ogrenci(Kisi):
#     def __init__(self, ad, soyad, ogrenci_no=None, yemek=None):
#         super().__init__(ad, soyad)
#         self.ogrenci_no = ogrenci_no
#         self.yemek = yemek
        
#     def set_yemek(self, yemek):
#         self.yemek = yemek

#     def __str__(self):
#         return f"{self.ad} {self.soyad}, Öğrenci No: {self.ogrenci_no}, Yemek: {self.yemek}"

# # Menü sınıfından bir örnek yemek oluşturma
# yemek = Menu("Mercimek Çorbası", "Karnıyarık", "Çoban Salata", "Baklava")
# print(yemek)

# # Öğrenci sınıfından bir örnek öğrenci oluşturma
# ogrenci = Ogrenci("Ahmet Yılmaz", "Veli", 12345, yemek)
# print(ogrenci)






# """
# Oluşturduğunuz örnek yemek ile, c) de yemek niteliği için tanımladığınız 
# setter’ı kullanarak f) de oluşturduğunuz örnek öğrencinin yemeğini güncelleyin (atayın).
# """

# # Yemek niteliği için oluşturduğumuz setter metodunu kullanarak güncelleme
# ogrenci.set_yemek(yemek)

# # Güncellenmiş öğrenci nesnesini ekrana yazdırma
# print(ogrenci)




d = {0:0, 1:1}
def fib1(n, d):
 if n in d:
    return d[n]
 else:
    sonuc = fib1(n-1, d)+fib1(n-2, d)
    d[n] = sonuc
    return sonuc

print(fib1(4,d))






















