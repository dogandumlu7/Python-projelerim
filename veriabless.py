# # object Oriented progmaing (OOP)


# # class => person (name, surname, birthday, calculateAge())

# class Person:
#     # class attributes
#     address = "no information"



#     # constructor (yapıcı metod)
#     def __init__(self, name, year):
#         # object attributes
#         self.name = name
#         self.year = year
#         print("init metodu çalıştı")
    
    
#     # methods

#     #instance metods
#     def intro(self):
#         print("Hello There I'm " + self.name)

#     def calculateAge (self):
#         return 2024 - self.year



# # instance (object)
# p1 = Person("Doğan", 2005)
# p2 = Person("Mahir", 2014)


# # updating
# p1.name = "Ensar"
# p1.address = "Muş"


# # accessing object attributes
# print(f"name: {p1.name}     year: {p1.year}    address: {p1.address}")
# print(f"name: {p2.name}     year: {p2.year}    address: {p2.address}")


# print(p1)
# print(p2)
# print(p1==p2)

# print("----------------------------------------")

# #object (instance)
# print (f"Adım: {p1.name}     yaşım: {p1.calculateAge()}")
# print (f"Adım: {p2.name}     yaşım: {p2.calculateAge()}")


# p1.intro()
# p2.intro()







# class circle:
#     # class object attribute
#     pi = 3.14


#     def __init__(self, yarıçap = 1):
#         self.yarıçap = yarıçap



#     # Methods
#     def cevre_hesapla(self):
#         return 2*self.pi*self.yarıçap


#     def Alan_Hesapla(self):
#         return self.pi*(self.yarıçap**2)


# c1 = circle() # yarıçap = 1
# c2 = circle(5) # yarıçap = 5

# print(f"alan = {c1.Alan_Hesapla()}  \nÇevre = {c1.cevre_hesapla()} \n \n")
# print(f"alan = {c2.Alan_Hesapla()}  \nÇevre = {c2.cevre_hesapla()}")








# # Interıhance (kalıtım): Miras alma

# # person => name, lastname, age, eat(), run(), drink()
# # student(person), teacher(person)

# # Animal => Dog(Animal), cat(Animal)



# class person():
#     def __init__(self, fname, lname):
#         self.name = fname
#         self.surname = lname
#         print(2**10)

#     def who_am_i (self):
#         print("I am a person")

#     def eat (self):
#         print("I am eating")



# class student(person):
#     def __init__(self, fname, lname, number):
#         person.__init__(self, fname, lname)
#         self.number = number
#         print("Opell")

#     # override
#     def who_am_i(self):
#         print(2**5)    

#     def SayHello(self):
#         print("Hello ı am a student")



# class Teacher(person):
#     def __init__(self, fname, lname, branch):
#         super().__init__(fname, lname)
#         self.branch = branch
        
#     def __str__(self):
#         return f"adım: {self.name}  soyadım: {self.surname}  branşım: {self.branch}"

#     def who_am_i(self):
#         print(f"I am a {self.branch} teacher")



# # s1 = student("Aydın","tohumcu", 240706093)

# # print(s1.name, s1.surname, s1.number)

# # s1.who_am_i()
# # s1.eat()
# # s1.SayHello()

# t1 = Teacher("Serkan", "yılmaz", "Match")
# t1.who_am_i()
# print(t1)







# # myList = [1,2,3]
# # myString = "my string"


# # print(type(myString))
# # print(type(myList))
# # print(len(myList))
# # print(len(myString))


# class Movie():
#     def __init__ (self,title,director,duration):
#         self.title = title
#         self.director = director
#         self.duration = duration
#         print("movie objesi oluşturuldu.")

#     def __str__ (self):
#         return f"{self.title} by {self.director}"
    
#     def __len__(self):
#         return self.duration
    
#     def __del__(self):
#         print("Filim objesi silindi")


# movie = Movie("Filim adı", "Yönetmen adı",120)
# print(f"{movie.title}: Mahkum,  {movie.director}: İsmail Hacıoğlu,  Filmin süresi: {movie.duration}")
# print (str(movie))
# print (len(movie))

# # del movie
# # print(movie)







# # Question
# class Question:
#     def __init__(self,text,choices,answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer
    
#     def checkAnswer(self, answer):
#         return self.answer == answer

# # Quiz
# class Quiz:
#     def __init__(self, questions):
#         self.questions = questions
#         self.score = 0
#         self.questionIndex = 0

#     def getQuestion(self):
#         return self.questions[self.questionIndex]

#     def displayQuestion(self):
#         question = self.getQuestion()
#         print(f'Soru {self.questionIndex + 1}: {question.text}')

#         for q in question.choices:
#             print('-'+ q)
        
#         answer = input('cevap: ')
#         self.guess(answer)
#         self.loadQuestion()

#     def guess(self, answer):
#         question = self.getQuestion()

#         if question.checkAnswer(answer):
#             self.score += 1
#         self.questionIndex += 1

#     def loadQuestion(self):
#         if len(self.questions) == self.questionIndex:
#             self.showScore()
#         else:         
#             self.displayProgress()  
#             self.displayQuestion()

#     def showScore(self):
#         print('\nscore: ', self.score)

#     def displayProgress(self):
#         totalQuestion = len(self.questions)
#         questionNumber = self.questionIndex + 1

#         if questionNumber > totalQuestion:
#             print('Quiz bitti.')
#         else:
#             print("\n")
#             print(f'Question {questionNumber} of {totalQuestion}'.center(75,'-'))
#             print("\n")

# q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
# q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
# q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
# q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
# q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')


# # print(q1.checkAnswer("python"))
# # print(q2.checkAnswer("c#"))


# questions = [q1,q2,q3,q4,q5]

# quiz = Quiz(questions)

# quiz.loadQuestion()

# quiz.displayProgress()







# # Yöntem 1
# import math
# import math as islem

# # value = dir(math)
# # value = help(math)
# # value = help(math.factorial)
# # value = math.sqrt(49)
# # value = math.factorial(5)
# # value = math.floor(5.9)
# # value = math.ceil(5.9)

# # value = islem.factorial(5)


# # Yöntem 2
# from math import *

# def sqrt(x):
#     print('x :'+ str(x))

# from math import factorial,sqrt,ceil

# # value = factorial(5)
# value = sqrt(9)
# # value = ceil(9.8)

# print(value)







# import random

# # result = dir(random)
# # result = help(random)

# result = random.random()
# result = random.random()*100
# result = random.uniform(10,15)
# result =int (random.uniform(30,45))
# result = random.randint(1,5*2)

# names = ["doğan", "berat","samet","aydın","kayra","suha"]
# string = "hello doğan"
# result = names[int (random.randint(0,len(names)-1))] 

# result = random.choice(names)
# result = random.choice(string)

# liste = list(range(10))
# random.shuffle(liste)
# result = liste

# liste = range(100)
# result = random.sample(liste,3)
# result = random.sample(names,2)

# print(result)


# # x = 10
# # while True:
# #     import random
# #     result =int (random.randint(1,5))
# #     print (result)
# #     x -= 1
# #     if x == 0:
# #         break







# kendi modülünü oluşturma

# """
#         modül hakında bilgilendirme
# """        

# print("Modül eklendi")

# number = 10
# numbers = [1,2,3]
# kaydır = {
#     "name" : "Ali",
#     "age" : 19,
#     "citiy" : "istanbul"
# }

# def func(x):
#     """
#         fonksiyon hakında bilgilendirme
#     """
#     print(f"x: {x}")

# class person:
#     def speak(self):
#         print("I am speaking...")


# # ==>>> (import veriabless.py) dosyasına git ve çalıştr








# Error
# Error handling => hata yöntemi


# print(a) => NameError
# int('1a2') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem'e) => SyntaxError

# error handling => hata yönetimi









# # try:
# #     x = int(input("x: "))
# #     y = int(input("y: "))
# #     result = x/y
# #     print(result)

# # except ZeroDivisionError:
# #     print("y için 0 girilemez")
# # except ValueError:
# #     print("x ve y için sayısal değer girmelisiniz")

# # ------------------------ veyaa -------------------------

# # except (ZeroDivisionError,ValueError) as hata:
# #     print("yanlış bilgi girdiniz")
# #     print(hata)


# #  ----------------------- veyaa ------------------------- 

# # except:
# #     print("yanlş bilgi girdinizz")



# while True:
#     try:
#         x = int(input("x: "))
#         y = int(input("y: "))
#         result = x/y
#         print(result)

#     except Exception as ex:
#         print("yanlış bilgi girdiniz", ex)
#     else:
#         break
#     finally:
#         print("try except sonlandı")







# x = 10

# if x > 5:
#     raise Exception("x 5 den büyük değer alamaz.")

# ------------------------------------------------------

# def check_password(psw):
#     import re
#     if len(psw) < 8:
#         raise Exception("parola en az 7 karakter olmalıdır.")
#     elif not re.search("[a-z]", psw):
#         raise Exception("parola küçük harf içermelidir.") 
#     elif not re.search("[A-Z]", psw):
#         raise Exception("parola büyük harf içermelidir.")
#     elif not re.search("[0-9]", psw):
#         raise Exception("parola rakam içermelidir.")
#     elif not re.search("[_@$]", psw):
#         raise Exception("parola alpha numeric karakter içermelidir.")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir.")
#     else:
#         print("geçerli parola")

# password = (input("parola gir: "))

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola: else")
# finally:
#     print("validation tamamlandı.")

# -------------------------------------------------------

# class Person:
#     def __init__(self, name, year):
#         if len(name) > 10:
#             raise Exception("name alanı fazla karakter içeriyor.")
#         else:
#             self.name = name

# p = Person("Aliiiiiiiiiiii", 1989)








# liste = ["1", "2", "5a", "10b", "abc", "10", 49]

# number = []
# for x in liste:
#     try:
#         x = int(x)
#         number.append(x)
#     except Exception :
#         continue
# print (number)

# ------------------------------------------------------------

# while True:
#     x = input("sayı: ")

#     if x == "q":
#         break

#     try:
#         x = int(x)
#         print(f"bir sayı girdiniz: {x}")
#     except Exception as t:
#         print("yanlıi bilgi girdiniz ===>    ", t)

# ---------------------------------------------------------------

# x = input("parola: ")

# def c (x):
#     import re
#     if re.search("[İ,ı,ş,ç,ü,ö,ğ]", x):
#         raise Exception(print("türkçe karakter hatası"))
#     else:
#         print("parola başarılı")
    
# try:
#     c(x)
# except Exception as t:
#     print(t)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# def checkPassword(parola):
#     turkce_karakterler = 'şçğüöıİ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('Parola türkçe karakter içeremez.')
#         else:
#             pass
#     print('geçerli parola')    

# parola = input('parola: ')

# try:
#     checkPassword(parola)    
# except TypeError as err:
#     print(err)

# --------------------------------------------------------------

# def faktoriyel(x):
#     x = int(x)

#     if x < 0:
#         raise ValueError('Negatif değer')

#     result = 1

#     for i in range(1, x+1):
#         result *= i

#     return result

# # for x in [5, 10, 20, -3, '10a']:
# #     try:
# #         y = faktoriyel(x)
# #     except ValueError as err:
# #         print(err)
# #         continue 
# #     print(y)

# while True:
#     x = input("x: ")
#     if x == "q":
#         break
#     try:
#         y = faktoriyel(x)
#     except ValueError as err:
#         print(err)
#         continue 
#     print(y)








# """
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
# """


# "w": (Write) yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya içeriğini siler ve yeniden ekleme yapar. 


# file = open("newfile.txt","x",encoding='utf-8')
# file.close()

# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme.txt", "w")
# file.close() 


# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme.txt", "w")
# file.write("Sadık Turan")
# file.close()

# ------------------------------------------------------------------

# """
#         a": (Append) ekleme. Dosya konumda yoksa oluşturur.)
# """

# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme.txt","a",encoding='utf-8')
# file.write("\nDoğan Dumlu")
# file.write(" -  Berat Ülker\n")
# file.close()

# -------------------------------------------------------------------
# """
#         "x": (Create) oluşturma. Dosya zaten varsa hata verir.
# """

# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme2.txt","x",encoding='utf-8')

# -------------------------------------------------------------------

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.








# try:
#     file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r")
# except Exception as r:
#     print("dosya yok veya okunamıyor ===>     ", r)
# finally:
#     print("dosya kapandı")
#     file.close()



# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "w")
# file.write("Doğan Dumlu\nBerat ülker\nCihan yarımdunya\nSellehatin Demirtaş")
# """ bu kodu çalıştırma bu kod dosyayı değiştirir """



# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="latin-1")

# for i in file:
#     print(i, end="")
# file.close()


# x = file.read()
# print(x)
# file.close()



# file = open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="latin-1")

# y = file.read()
# print("--------------------")
# print(y)




# xx = file.read(6)
# print(xx)

# xx = file.read(5)
# print(xx)

# xx = file.read(7)
# print(xx)

# xx = file.read(5)
# print(xx)

# file.close()


# content = file.readline()
# print(content,end="")

# content = file.readline()
# print(content,end="")

# content = file.readline()
# print(content,end="")

# content = file.readline()
# print(content,end="")


# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")

# file.close()


# liste = file.readlines()
# print(liste)

# print(liste[0],end="")
# print(liste[1],end="")
# print(liste[2],end="")
# print(liste[3],end="")








# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "w", encoding="latin-1",errors="ignore") as file:
#     file.write("DUMLULAR HOLDİNG -DOĞAN DUMLU-")


# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="latin-1") as file:
#     content = file.read(15)
#     print(content)
#     file.seek(16) # imleci 9'a götürür
#     print(file.tell())   # imlecin konumunu verir

#     content = file.read()   # Dosyayı file.tell ile çalıştırdığımzdan imleç sona gelir
#     print(content)






# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "w", encoding="latin-1",errors="ignore") as file:
#      file.write("DUMLULAR HOLDİNG -DOĞAN DUMLU-")



# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r+", encoding="latin-1") as file :
#     file.seek(9)
#     file.write("\n--deneme--")



#     ******* Sayfa sonuna güncelleme ******

# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "a", encoding="utf-8") as file :
#     file.write("\nGİRESUN ÜNÜVERSİTESİ BİLGİSAYAR MÜHENDİSLİĞİ")

# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r+", encoding="utf-8") as file :
#     print(file.read())




# #     ******* Sayfa başını güncelleme ******

# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r+", encoding="utf-8") as file :
#     content = file.read()
#     content = "GİRESUN ÜNİVERSİTESİ\n" + "BİLGİSAYAR MÜHENDİSLİĞİ\n" + "BİLGİSAYAR PROGRAMLAMA DERSİ ÖDEVİ\n" + content
#     file.seek(0)
#     file.write(content)


# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="utf-8") as file :
#     print(file.read())




#     ******* Sayfa başını güncelleme ******

# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r+", encoding="utf-8") as file :
#     list = file.readlines()
#     list.insert(3, "PUAN: 96\n")
#     print(list)
#     file.seek(0)
#     for i in list:
#         file.write(i)


# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="utf-8") as file :
#     print(file.read())



# veya


# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r+", encoding="utf-8") as file :
#     list = file.readlines()
#     list.insert(3, "PUAN: 96\n")
#     print(list)
#     file.seek(0)
#     file.writelines(list)


# with open("c:/Users/dumlu/OneDrive/Masaüstü/deneme1.txt", "r", encoding="utf-8") as file :
#     print(file.read())








# def not_hesapla(satir):
#     satir = satir[:-1]
#     liste = satir.split(':')

#     ogrenciAdi = liste[0]
#     notlar = liste[1].split(',')

#     not1 = int(notlar[0])
#     not2 = int(notlar[1])
#     not3 = int(notlar[2])

#     ortalama = (not1+not2+not3)/3

#     if ortalama>=90 and ortalama<=100:
#         harf = "AA"
#     elif ortalama>=85 and ortalama<=89:
#         harf = "BA"
#     elif ortalama>=80 and ortalama<=84:
#         harf = "BB"
#     elif ortalama>=75 and ortalama<=79:
#         harf = "CB"
#     elif ortalama>=70 and ortalama<=74:
#         harf = "CC"
#     elif ortalama>=65 and ortalama<=69:
#         harf = "DC"
#     elif ortalama>=60 and ortalama<=64:
#         harf = "DD"
#     elif ortalama>=50 and ortalama<=59:
#         harf = "FD"
#     else:
#         harf = "FF"

#     return ogrenciAdi + ": " + harf + "\n"


# def ortalamalari_oku():
#     with open("sinav_notlari.txt","r",encoding="utf-8") as file:
#         for satir in file:
#             print(not_hesapla(satir))


# def not_gir():
#     ad = input('Öğrenci adı: ')
#     soyad = input('Öğrenci soyad: ')
#     not1 = input('not 1: ')
#     not2 = input('not 2: ')
#     not3 = input('not 3: ')

#     with open("sinav_notlari.txt","a", encoding="utf-8") as file:
#         file.write(ad+' '+ soyad+ ':'+not1+','+not2+','+not3+'\n')        


# def notlari_kayitet():
#     with open('sinav_notlari.txt',"r",encoding="utf-8") as file:
#         liste = []

#         for i in file:
#             liste.append(not_hesapla(i))

#         with open("sonuclar.txt","w",encoding="utf-8") as file2:
#             for i in liste:
#                 file2.write(i)

# while True:
#     islem = input('1- Notları Oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n==>> ')

#     if islem == '1':
#         ortalamalari_oku()
#     elif islem == '2':
#         not_gir()
#     elif islem == '3':
#         notlari_kayitet()
#     else:
#         break










# def greeting(name):
#     print('hello ', name)

# print(greeting('ali'))
# print(greeting)

# sayHello = greeting
# del sayHello
# # print(sayHello)
# print(greeting)


# # encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)

# outer(10)
# # inner_increment(10)


# def factorial(number):
#     if not isinstance(number, int):
#         raise TypeError("number must be an integer")

#     if not number >=0:
#         raise ValueError("number must be zero or positive")

#     def inner_factorial(number):
#         if number <= 1:
#             return 1

#         return number * inner_factorial(number - 1)

#     return inner_factorial(number)
# try:
#     print(factorial(5))
# except Exception as ex:
#     print(ex)










# def usalma(number):
#     def inner(power):
#         return number ** power
    
#     return inner


# two = usalma(2)(3)
# three = usalma(3)(4)

# print(two)  # 2-3
# print(three)  # 3-4



# def yetki_sorgula(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} rolü {1} sayfasına ulaşabilir.".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz.".format(role,page)
#     return inner

# user1 = yetki_sorgula("Product Edit")
# print(user1("Admin"))
# print(user1("User"))



# def islem(islem_adi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam+=i
#         return toplam

#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim*=i
#         return carpim

#     if islem_adi == "toplama":
#         return toplam
#     else:
#         return carpma


# toplama = islem("toplama")
# print(toplama(1,3,5,6,7))

# carpma = islem("carpma")
# print(carpma(1,2,3,6,4))








# def toplama(a,b):
#     return a+b
# def cikarma(a,b):
#     return a-b
# def carpma(a,b):
#     return a*b
# def bolme(a,b):
#     return a/b

# def islem(f1, f2, f3, f4, islem_adi):
#     if islem_adi== "toplama":
#         print(f1(2,3))
#     elif islem_adi == "cikarma":
#         print(f2(5,3))
#     elif islem_adi == "carpma":
#         print(f3(3,4))
#     elif islem_adi == "bolme":
#         print(f4(10,2))
#     else:
#         print("geçersiz işlem...")

# islem(toplama, cikarma, carpma, bolme, "toplama")
# islem(toplama, cikarma, carpma, bolme, "cikarma")
# islem(toplama, cikarma, carpma, bolme, "carpma")
# islem(toplama, cikarma, carpma, bolme, "bolme")
# islem(toplama, cikarma, carpma, bolme, "carpmaa")










# def my_decorator(func):
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# # @my_decorator
# def sayHello(name):
#     print("hello", name)

# # sayHello("Doğan")

# my_decorator(sayHello)("Doğan")



# import math
# import time

# def calculate_time(func):
#     def inner(*args,**kwargs):        
#         start = time.time()
#         time.sleep(0.1)
#         func(*args,**kwargs)        
#         finish = time.time()
#         print("fonksiyon "+func.__name__ +" " + str(finish-start) + " saniye sürdü.")
#     return inner

# # @calculate_time
# # def usalma(a,b):
# #     print(math.pow(a,b))   

# # @calculate_time
# # def faktoriyel(num):
# #     print(math.factorial(num))

# # @calculate_time
# # def toplama(a,b):
# #     print(a+b)

# # usalma(2,3)
# # faktoriyel(4)
# # toplama(10,20)

# def faktoriyel(num):
#     print(math.factorial(num))

# def usalma(a,b):
#     print(math.pow(a,b))

# def toplama(a,b):
#     print(a+b)


# calculate_time(usalma)(2,3)
# calculate_time(faktoriyel)(4)
# calculate_time(toplama)(10,20)








# liste = [1,2,3,4,5]

# iterator = iter(liste)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator))

# for i in liste:
#     print(i)

# liste = [1,2,3,4,5]
# iterator = iter(liste)

# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break




# class MyNumbers:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration

# list = MyNumbers(20,50)

# myiter = iter(list)

# # print(next(myiter))
# # print(next(myiter))

# while True:
#     try:
#         element = next(myiter)
#         print(element)
#     except StopIteration:
#         break


# # for x in list:
# #     print(x)








# # def cube():
# #     for i in range(5):
# #         yield i ** 3
# # print(cube())

# # for i in cube():
# #     print(i)

# generator = (i**3 for i in range(5))
# print(generator)

# for i in generator:
#     print(i)
# # print(next(generator))
# # print(next(generator))
# # print(next(generator))











































