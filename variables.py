# # print ve atama
# ali=909
# mehmet=983
# hazal=890
# vergi=0.098
# print("ali:")
# print(ali-(ali*vergi))
# print("mehmet:")
# print(mehmet-(mehmet*vergi))
# print("hazal:")
# print(hazal-(hazal*vergi))





# #int ve float ,toplama çıkarma çarpma
# print(2+2)
# print(2+1.5)
# print(2.0+4)
# print(type(2))
# print(type(2.0))
# print(2+21*7+7)
# print((2+21)*7+7)





# #işlem sembolleri

# "       + toplama                                 "
# "       - çıkarma                                 "
# "       * çarpma                                  "
# "       / bölme                                   "
# "       ** üs alma                                "
# "        %  mod, bölümden kalanı gösterir         "
# "        //  tam bölme, kesri yuvarlar            "





# # işlemler
# print(0.5*4)
# print(4**3)
# print(54%5)
# print(76//8)
# print(64/8)
# print(8-54)
# print(1/2)
# print(65**0.7)
# print(10*5)
# print(23.0%7)
# print(13/4)
# print(13//4)
# print(-6-8)
# print(81/27)






# #değişken atama kuralları

# #DEĞİŞKEN ATAMA KURALLARI

# #Rakamla başlayamaz

# _number = 65     #çalişirr
# number1 = 10     #çalişirr
# # 1number = 10     #bu olmaz rakamla başlayamaz

# # print(number1 += 20)  #çalışmaz
# print(number1)
# print([number1+ i for i in range (20,21)]) #ilerde döngüler konusunda öğreniceksin

# number1 +=20       #çalişirr
# print(number1)

# # BÜYÜK KÜÇÜK HARF DUYARLILIĞI

# age = 20
# AGE = 30
# print(age)
# print(AGE)
# # İkiside farklıdır

# #TÜRKÇE KARAKTER KULLANMAYALIM

# # Yaş olmaz yas veya age olur

# x = 1                 #int
# y = 6.5               #float
# name = "çınar"        #string
# isSutudent = True     #bool
# x, y, name, isStudent = (1, 6.5, "Cinar", True)
# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isStudent))
# # veya
# variables = (1, 6.5, "Cinar", True)  #ilerde döngüler konusunda öğreniceksin
# for var in variables:
#     print(type(var))



# a = 59
# b = 23
# print(a+b) #82

# a = '59'
# b = '23'
# print(a+b)   #5923

# firstname = 'DOĞAN'
# lastname = 'DUMLU'
# print(firstname+lastname)
# print(firstname+" "+lastname)
# print(firstname,lastname)   #virgül boşluk niyetine kullanılır

# #DEĞİŞKENLER ARASINDA BOŞLUK OLAMAZ

# # first name = dogan  #yanlıştır
# lastname = "DUMLU"   #doğrudur
# print(lastname)






# #inputt

# input("müşteri adı:")
# input("müşteri soyadı:")
# input("müşteri adı ve soyadı:")
# input("müşteri cinsiyeti:")
# input("müşteri tc kimlik:")
# input("müşteri doğum yılı:")
# input("müşteri adres bilgisi:")
# input("müşteri yaşı:")







# x = 5                #int
# y = 2.6              #float
# name = 'çınar'       #string   str
# isonline = True      #bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(isonline))

# x = float(x)      #5.0
# y = int(y)        #2
# print(x)
# print(y)


# t = str(x)+str(y)     #5.02
# print(t)

# isonline = str(isonline) #True
# print(isonline)







# saat = 15
# sıcaklık = 39

# saat < 16 and sıcaklık>30 == print("saat 16 dan önce ve sıcaklık 30 dan yüksek")
# saat < 16 and sıcaklık<30 == print("saat 16 dan önce ve sıcaklık 30 dan düşük")
# saat > 16 and sıcaklık>30 == print("saat 16 dan sonra ve sıcaklık 30 dan yüksek")
# sıcaklık <= 30  == print("sıcaklık 30'un üstünde değil")








# r = float(input("DAİRENİN ÇAPINI GİRİN:"))
# pi = 3.14
# dairenin_alanı = pi * (r ** 2)
# çevre = 2 * pi * r
# print("ALAN:",dairenin_alanı)
# print("ÇEVRE:", çevre)

# print(type(dairenin_alanı))

# # dairenin_alanı = str(dairenin_alanı)
# # çevre = str(çevre)
# # print(type(dairenin_alanı))

# print("ALAN: " + str(dairenin_alanı) + "   ÇEVRE: " + str(çevre))
# # print("ALAN: " + (dairenin_alanı) + "   ÇEVRE: " + (çevre)) #çalişmaz çünkü str + int olmaz dair... ve çevre'yi stringe çevir
# print("ALAN:" , (dairenin_alanı) , "  ÇEVRE: " , (çevre))
# print(f"ALAN: {dairenin_alanı}   ÇEVRE: {çevre}")









# name = "DOĞAN"
# surname = "DUMLU"
# age = 19

# print ("my name is " + name + " " + surname + " \nI am " + str(age) + "years old")      #  \n alt satıra geçmek içinn kullanılıyor
# print ("my name is " + name + " " + surname + " and I am " + str(age) + "years old")
# x = "my name is " + name + " " + surname + " and I am " + str(age) + "years old"
# print(x)

# print ("my name is" , name , surname , "and I am" , age , "years old")

# name = "DOĞAN"
# name2 = "AYŞE"

# print(name[0] + "   " + name2[0])
# print(name[1] + "   " + name2[1])
# print(name[2] + "   " + name2[2])
# print(name[3] + "   " + name2[3])
# print(name[4])

# print(len(name))
# print(len(name2))


# print(name[len(name) - 1])
# print(name[-1])

# lenght = len(name)
# lenght2 = len(name2)

# print(name[lenght - 1])

# print("//////////// \n   ")
# print(name[0] + "        ///")
# print(name[1] + "   " + name2[0] + "    ///")
# print(name[2] + "   " + name2[1] + "    ///")
# print(name[3] + "   " + name2[2] + "    ///")
# print(name[4] + "   " + name2[3] + "    ///")
# print("-----------")
# print(name[lenght - 1] + "   " + name2[lenght2 - 1] + "    ///")
# print(name[lenght - 2] + "   " + name2[lenght2 - 2] + "    ///")
# print(name[lenght - 3] + "   " + name2[lenght2 - 3] + "    ///")
# print(name[lenght - 4] + "   " + name2[lenght2 - 4] + "    ///")
# print(name[lenght - 5] + "        /// \n  ")
# print("//////////// ")


# x = "AYŞEGÜL"
# print(x[4:7])
# print(x[0:])
# print(x[:4])
# print(x[0:7:2])







# name = "DOĞAN"
# surname = "DUMLU"

# print("My name is {}" .format(name, surname))
# print("My name is {1} {0}".format(name ,surname))
# print("My name is {s} {n}".format(n = name, s = surname))
# print("My name is {} {} and I'm {} years old".format(name, surname, "19"))
# print("My name is {} {} \nI'm {} years old".format(name, surname, "19"))
# print("My name is I'm years old".format(name, surname, "19")) #==> My name is I'm years old


# x = 2000/870
# print("işlemin soncu: {}".format(x))
# print("işlemin soncu: {y:0.4}" .format(y=x))

# print(f"My name is {name} {surname} and I'm {19} years old")







# website = "http://www.dogandumlu.com"
# course = "python kursu: Baştan sona python programlama rehberiniz (40 saat)"

# print(len(course))
# print(website[7:10])
# print(website[22:25])
# print(course[0:15] + course[50:65])
# print(course[::-1])
# name,surname,age,job = "DOĞAN", "DUMLU", 19, "ENGİNEER"
# print("my name is " + name + " " + surname + ", I'm " + str(age) +" years old and my profession is " + job)
# print("my name is {} {}, I'm {} years old and my profession is {}".format(name,surname,age,job))
# print(f"my name is {name} {surname}, I'm {age} years old and my profession is {job}")


# x = "Hello world"
# print(x[:6] + "W" + x[-4:])
# x = x.replace("w","k")
# print (x)
# print(x.replace("l","x"))    #bundan sonrakini etkilemez sadece burda Hexxo worxd  yazar geri kalan hello world'dür
# print(x)

# print("abc "*5)
# x ="dogan"*5
# print(x)
# print(x[::5])







# message = "hello, my name is Doğan DUMLU"

# print(message)

# print(message.upper())

# print(message.lower())

# print(message.title())

# print(message.capitalize())


# message = "  hello, my name is Doğan DUMLU"

# print(message.strip())


# message = "hello, my name is Doğan DUMLU"

# print(message.split())
# print(message.split()[0] + "\n" + message.split()[3])


# print(message.split(","))

# message = message.split()
# print(message)


# message = "doğan"
# print("".join(message))
# print(" " .join(message))
# print(" * " .join(message))


# message = "hello, my name is Doğan DUMLU"

# x = message.find("my")
# print(x)

# print(message.find("Doğan"))
# print(message[18:23])

# print(message.find("MAHİR"))

# print(message.startswith("h"))
# print(message.endswith("U"))
# print(message.replace("Doğan", "MAHİR").replace("hello", "Hello there").replace(" ", "_"))

# print(message.center(50))
# print(message.center(50, "*"))

# x = message.center(50, "*")
# print(len(x))


# message = "hello, my name is Doğan DUMLU"
# print(message.split())
# print(message.split()[3])

# mylist1 = ["1", "2" ,"3"]
# mylist2 = ["4", "5" ,"6"]

# print( mylist1 + mylist2)
# print( len(mylist1 + mylist2))
# print((mylist1 + mylist2)[2])

# userA = ["doğan", 19]
# userB = ["mahir", 10]
# print([userA ]+[ userB])
# print(([userA ]+[ userB])[0])
# print((([userA ]+[ userB])[0])[1])
# x = (([userA ]+[ userB])[0])[1]
# print(str(x)[0])
# print(str((([userA ]+[ userB])[0])[1])[1])



# userA = ["doğan", 19]
# userB = ["mahir", 10]
# x = [userA] + [userB]
# print(x)
# print((x)[0])
# print(((x)[0])[1])
# x = ((x)[0])[1]
# print(str(x)[0])
# print(str((([userA] + [userB])[0])[1])[1])





# liste = ["bmv", "mercedes", "opel", "mazda"]

# print(liste)

# print(len(liste))

# print(liste[0] + " " + liste[3])
# print((liste[0])[0] + " " + (liste[3])[len(liste[3])-1])

# print(str(liste))
# print(str(liste).replace("mazda", "toyota"))
# liste[-1] ="toyota"
# print(liste)



# liste = ["bmv", "mercedes", "opel", "mazda"]

# print(str(liste).find("mercedes"))
# print("mercedes" in liste )
# print(str(liste)[9:17])

# print(liste[-2])
# print(str(liste)[-2])

# print(str(liste)[:3])
# print(liste[0:3])

# print(str(liste).replace("opel", "toyota") .replace ("mazda", "renault"))
# liste[-2:] = "toyota", "renault"
# print(liste)

# liste = ["bmv", "mercedes", "opel", "mazda"]

# print(len(str(liste)))

# print(liste + ["audi", "nissan"])
# print (str(liste)[0:35] + ", 'audi'" + ", " + "'nissan'" + "]")



# liste = ["bmv", "mercedes", "opel", "mazda"]
# del liste[-1]
# print(liste)

# liste = ["bmv", "mercedes", "opel", "mazda"]

# print (str(liste).replace(", 'mazda'", ""))
# print(liste[:3])
# print(liste[::-1])



# tyt = "Doğan", "DUMLU", 2005 , [86,94,97]
# print(f"{2025-tyt[2]} yaşında olan {tyt[0]} {tyt[1]}'nun not ortalaması", (tyt[3][0]+tyt[3][1]+tyt[3][2]) / 3)
# print(f"{2025-tyt[2]} yaşında olan {tyt[0]} {tyt[1]}'nun not ortalaması {(tyt[3][0]+tyt[3][1]+tyt[3][2]) / 3}")








# numbers = [2, 9, 0, 7, 5, 82, 6, 5, 21]
# latters = ["a", "t", "k", "h", "y", "f", "d", "h"]
# print(max(numbers))  #82
# print(min(numbers))  #0
# print(numbers[3:6])  #7,5,82
# print(numbers[:3])   #2,9,0

# numbers[5] = 32
# print(numbers[5])
# print(numbers)
# numbers.reverse()
# print(numbers)


# numbers.append(49)
# print(numbers)

# numbers.append(15)
# print(numbers)

# numbers.insert(3, 11)
# print(numbers)

# numbers.insert(-1, 41)
# print(numbers)

# numbers.insert(13, 19)
# print(numbers)



# numbers = [2, 9, 0, 7, 5, 82, 6, 5, 21,5]
# latters = ["a", "t", "k", "h", "y", "f", "d", "h"]

# print(numbers)
# print(latters)


# numbers.pop()  #listedeki son indexi siler
# print(numbers)



# numbers.pop(0)
# print(numbers)

# numbers.pop(-1)
# print(numbers)


# numbers.remove(82) #82'yi listeden siler
# print(numbers)

# numbers.sort()
# latters.sort()
# print(numbers)
# print(latters)

# numbers.reverse()
# print(numbers)
# latters.reverse()
# print(latters)

# print(len(numbers))  #9 -- 82'yi silmiştik
# print(len(latters))  #8

# print(latters.count("h"))  #liatede kaç tane h,5 var onu söyler
# print(numbers.count(82))


# print(min(latters))
# print(max(latters))

# numbers.clear() #listeyi komple siler
# print(numbers)
# latters.clear() #listeyi komple siler
# print(latters)








# names = ["ali", "yağmur", "hakan", "deniz"]
# years = [1998, 2000, 1998, 1987]
# print (names)
# print (years)

# names += ["cenk"]
# print(names)
# names.append("cenk")
# print(names)

# names.insert(0, "sena")
# print(names)
# names.insert(len(names), "berat")
# print(names)


# names.pop(2)
# print(names)
# names.remove("yağmur")
# print(names)

# print(names.index("deniz"))
# print("ali" in names)
# print(names.index("ali"))


# names.reverse()   #listeyi ters çevirir
# print(names)
# print(names[::-1])


# names.sort()
# print(names)

# years.sort()
# print(years)

# str = "chevrolet, dacia"
# print(str.split(","))

# years.sort()
# print(len(years))
# print(f"{years[0]} {years[len(years) - 1]}" )
# print(f"{min(years)} {max(years)}")

# print(years.count(1998)) #2 tane 1998 var

# years.clear()
# print(years)


# mark1 = input("1. markayı giriniz:")
# mark2 = input("2. markayı giriniz:")
# mark3 = input("3. markayı giriniz:")

# marks = [mark1, mark2, mark3]
# print(marks)


# liste = []
# for i in range(3):
#     x = input(f"{i+1}. markayı girin: ")
#     liste.append(x)

# print("girdiğiniz markalar: ", liste)







list = [1, 2, 3]
tuple = (1, "iki", 3, "onbeş")
# print (list)
# print (tuple)

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(tuple[2])
# print(tuple[3])

# print(len(tuple))

# tuple += ("ayşe", 7)
# list += [5, 6]
# print(tuple)
# print(list)


# tuple = ("ayşe", 7, "ayşe")
# list = [5, 6]
# print(tuple)
# print(list)

# list[1] = "altı"
# tuple[0] = "beş" # buna izin vermez
# print(list)

# print(tuple.count("ayşe"))
# print(tuple.index("ayşe"))

# tuple = ("beyza", 12, "fatma")
# names = ("fatih", "ahmet", "yılmaz") + tuple
# print(names)

# number = tuple[1] + 5
# number2 = names[4] + 12
# print(number)    #17
# print(number2)   #24






# şehirler = ["istanbul", "muş", "tekirdağ"]
# plakalar = [34, 49, 59]

# print(şehirler.index("muş"))
# print(plakalar[şehirler.index("muş")])


# plakaşehir = {"istanbul" :34, "muş" :49, "tekirdağ" :59}
# print(plakaşehir["muş"])

# plakaşehir["ankara"] = 6
# print(plakaşehir)

# plakaşehir["tekirdağ"] = "inşaat"
# print(plakaşehir)


# doğandumlu = {
#     "age" : 19,
#     "email" : "dumludogano131@gmail.com"  ,
#     "adres" : "muş",
#     "phone no" : "05376428742",
# }
# print (doğandumlu)
# print(doğandumlu["age"])

# user = {
#      "doğandumlu" :  {
#     "rolls" : ["admin", "user", "klan"],
#     "age" : 19,
#     "email" : "dumludogano131@gmail.com"  ,
#     "adres" : "muş",
#     "phone no" : "05376428742",
# }}

# print(user)
# print(user["doğandumlu"])
# print (user["doğandumlu"]["email"])
# print (user["doğandumlu"]["rolls"][0:2])








# öğrenci = {}


# ad = input("ögrencinin adı :" )
# soyad = input("ögrencinin soyadı :")
# yaş = input("ögrencinin yaşı :")
# okul_numara = input("ögrencinin okul numarası :")

# öğrenci["ad"] = ad
# öğrenci["soyad"]= soyad
# öğrenci["yaş"] = yaş
# öğrenci["numara"] = okul_numara
# print (öğrenci)

# print (öğrenci["ad"])
# print (öğrenci["soyad"])
# print (öğrenci["yaş"])
# print (öğrenci["numara"])



# öğrenciler = {}
# for i in range(3):
#     number = input("öğrencinin okul numarası: ")
#     name = input("öğrenci adı :")
#     soyad = input("öğrenci soyadı :")
#     yaş = input("öğrenci yaşı :")
#     phone = input("öğrenci telefon numrası :")
#     öğrenciler.update({number : {
#          "ad" : name ,
#          "soyad" : soyad   ,
#          "yaş" : yaş ,
#          "telefon numarası" : phone}})

# print(öğrenciler)
# x = input ("bilgisini öğrenmek istediğiniz öğrencinin okul numarası :")
# print (öğrenciler[x])

# y = öğrenciler[x]
# print(f"aradığınız {x} nolu öğrencinin adı: {y["ad"] } soyadı: {y["soyad"]} yaşı: {y["yaş"]} telefon numarası: {y["telefon numarası"]} ")









# fruits = {"orange", "apple", "banana"}

# #print(fruits[1])   indekslenemez

# print(fruits)

# fruits.update(["grape", "mango", "apple"])
# print(fruits)

# fruits.add("cherry")
# print(fruits)

# for a in fruits:
#     print(a)


# fruits.remove("grape")
# print(fruits)

# fruits.discard("banana")
# print(fruits)

# fruits.pop()   #herhangi bir elemanı siler
# print(fruits)

# fruits.clear()
# print(fruits)


# Mylist = [7, 1, 6, 5, 4, 1 ,5]
# print(Mylist)
# print(set(Mylist))









# x = 5
# y = 25

# x = y
# y = 10

# print(x,y)    #bunlar valu types oluyor ve y nin üzerinde yapılan değişiklik x'i etkilemez



# x = ["banana", "apple", "orange"]
# y = ["banana", "apple", "orange"]    #bunlar referance types oluyor ve y nin üzerinde yapılan değişiklik x'i etkiler
#                                      #isteler eşitlenirse adresler eşitleniyor ve birinde değişiklik olması ikisinide etkiler
# x = y
# y[0] = "grape"
# print(x,y)

# x = ["banana", "apple", "orange"]
# y = ["apple", "orange"]

# x = y
# x[1] = "grape"
# print(x,y)

# y[1] = "mango"
# print(x,y)








# x,y,z = 10,20,30
# print (x,y,z)

# x,y = y,x
# print (x,y,z)

# x,y,z = 10,20,30

# x += 5
# y -= 5
# z /= 3
# print(x,y,z)

# x *= 5
# y %= 6
# z //= 4
# print(x,y,z)

# x,y = 6,2
# x **= y
# print(x)


# values = 1,2,3
# print(values)
# print(type(values))

# x,y,z = values
# print(x,y,z)

# values = 1,2,3,4,5
# x,y,*z = values
# print (x,y,z)
# print(x,y,z[2])








# x,y,z = 2,5,10
# numbers = 1,5,7,10,6

# a = int(input("1.sayıyı girin:"))
# b = int(input("2.sayıyı girin:"))

# print((a*b)-(x+y+z))
# print(y//x)
# print((x+y+z) % 3)
# print(y**x)

# x,*y,z = numbers
# print(x,y,z)
# print(z**3)


# print(f"{y[0]+y[1]+y[2]}")








# a,b,c,d = 5,5,6,8

# result = a==b
# print (result)

# result = a != c
# print (result)

# result = c==d
# print (result)

# result = d==a
# print (result)

# result = b >= a
# print (result)

# result = c <= d
# print (result)

# result = True == 1
# print (result)
# result = False == 0
# print (result)


# username = "dogandumlu"
# pasaword = "ab1331"

# x = input("username:")
# y = input("pasaword: ")

# result = username == x
# print (result)

# result = pasaword == y
# print (result)








# x = int(input("1.sayıyı gir: "))
# y = int(input("1.sayıyı gir: "))

# result = x > y
# print(f"{x}'in {y}'den büyük olma durumu: {int(result)}")



# x = int(input("1. vize notu: "))
# y = int(input("2. vize notu: "))
# z = int(input("final notu: "))

# vize_ort = (x+y)*(60/100)/2
# final_ort = z*(40/100)

# ortalama = vize_ort + final_ort

# t = ortalama >= 50

# print(f"{ortalama} ortalamasıyla geçme durumunuz : {t}")



# x = int(input("sayıyı girin: "))

# t = x%2 == 0

# print (f"girdiğiniz {x} sayısının çift olma durumu: {t}")




# x = int(input("sayıyı giriniz: "))

# t = x > 0

# print(f"girdiğiniz {x} sayısının pozitif olma durumu: {t}")



# x = "dumludogan@gmail.com"
# y = "ab1331"    #lower hepsini küçük harf yapar strip ise boşluk girildiyse onu siler (burda çalıştıramadın)
# #               #burdaki hatan şu strip sadece başta ve sonda boşluk varsa siler ortaya karışmaz "   merhaba dünya!  " => "merhaba dünya!"
# #               #replace cümlede yer değiştirme görevi görür replace(" ","") boşluğu siler başta,sonda,ortada

# a = input("email: ")
# b = input("password: ")

# t = a.lower().strip() == x
# z = b.lower().replace(" ", "") == y

# print(f"girilen email doğrumu? : {t} \ngirilen şifre doğrumu? : {z}")


# x = "merhaba"
# y = "ayhan"
# x =y
# y = "mahir"
# print(x)





# x = 5

# result = 5 <= x < 10
# print(result)

# result = 5 < x and x < 10
# print(result)

# hak = 5
# devam = "e"
# result = hak > 0 and devam == "e"
# print(result)


# x = 13

# result = x>0 and x%2==0
# print(result)

# result = x>0 or x%2==0
# print(result)

# result = not(x%2==0)
# print(result)           #x'in yani 13'ün 2 ile bölümü sıfır olmaz cevap false'di
# #                       #ancak (not)ını aldığımız için cevap true olucaktır


# x = 8
# result = 5<x<10 and x%2 == 0
# print(result)








# x = int(input("bir sayı gir: "))
# result = 0<x<100
# print(f"girdiğiniz sayının sıfırla 100 arasında olma durumu: {result}" )


# x = int(input("bir sayı gir: "))
# result = x > 0 and x%2==0
# print(f"girdiğiniz sayının çift pozitif sayı olma durumu: {result}")


# eposta = "dogandumlu0131@gmail.com"
# password = "ab1331"
# x = input("epostanızı girin: ") #lower hepsini küçük harf yapar
# y = input("parolanızı girin: ") #strip boşlukları siler   (burda çalıştırabildin)
# result = x.lower().strip() == eposta and y.lower().strip() == password       #tüm boşlukları silmez başta ve sonda olan boşlukları siler sadece
# print(f"girdiğiniz eposta ve şifrenin doğruluk değeri: {result}'dur")


# x = int(input("bir sayı gir: "))
# y = int(input("bir sayı gir: "))
# z = int(input("bir sayı gir: "))
# result1 = x>y and x>z
# result2 = y>x and y>z
# result3 = z>y and z>x
# print(f"x hepsinden büyüktür: {result1}")
# print(f"y hepsinden büyüktür: {result2}")
# print(f"z hepsinden büyüktür: {result3}")


# x = int(input("1.vize notu: "))
# y = int(input("2.vize notu: "))
# z = int(input("final notu: "))
# final = z*0.4
# vizeort = (x+y)/2
# ort = final + vizeort*0.6
# result = (ort==50 and z>=50 ) or (ort>50) or (z>70)
# print(f"{ort} ortalamasıyla sınıfı geçme durumunuz: {result}")


# x = (input("adınz:"))
# y = float(input("kilonuz:"))
# z = float(input("boyunuz:"))
# kiloindeksi = (y/z**2)
# result1 = 0<=kiloindeksi<=18.4
# result2 = 18.5<=kiloindeksi<=24.9
# result3 = 25<=kiloindeksi<=29.9
# result4 = 30<=kiloindeksi<=34.9
# print(f"{x} kilo durumunuz: \nzayıf: {result1} \nnormal: {result2} \nfazla kilolo: {result3} \nşişman (obez): {result4}  ")








# x = y = [1, 2, 3]
# z = [1, 2, 3]

# print(x==y)     #x ve y nin değerleri aynı  True
# print(x==z)     #x ve z nin değerleri aynı  True
# print(x is y)   #x ve y aynı adrese sahip   True
# print(x is z)   #x ve z aynı adrese sahip değil  False


# x = [1, 4, 7]
# y = [5, 9]

# print(x==y)     #False
# print(x is y)   #False

# del x[2]
# print(x)
# print(x==y)     #False
# print(x is y)   #False

# y[0] = 4
# y[1] = 1
# print(y)
# y.reverse()
# print(y)
# print(x==y)
# print(x is y)
# print(x is not y)

# x = ["apple", "banana"]
# print("banana" in x)    #x listesinin içinde "banana" varmı (true)

# x = "doğan"
# print("do" in x)
# x = {12, "ayşe", 6.6}
# print(6.6 in x)
# print(6 not in x)








# kullanıcı_adı = "dogandumlu"
# parola = "OPELL"

# x = input("kullanıcı adı: ")
# y = input("parola: ")

# if (x==kullanıcı_adı):
#     if (y==parola):
#         print("hoş geldiniz")
#     else:
#          print("parola yanlış")
# else :
#     if (y==parola):
#         print("kullanıcı adı yanlş")
#     else:
#         print("kulanıcı adı ve parola yanlış")








# x = int(input("x: "))
# y = int(input("y: "))

# if x>y :
#      print(f"{x} {y}'den büyük")
# elif x==y:
#      print(f"{x} {y}'ye eşit")
# else:
#     print(f"{y} {x}'den büyük")


# x = int(input("x: "))

# if x>0:
#     print("girilen sayı pozitif")
# elif x<0:
#     print("girilen sayı negatiftir")
# else : print("girilen sayı sıfır")









# name = input("isim: ")
# age = int(input("yaş: "))
# egtim = input("eğtim düzeyi: ")

# if age>=18 :
#     if (egtim == "lise") or (egtim == "üniversite"):
#         print("eliyet alabilrsin")
#     else:
#         print("eliyet almak için eğtim seviyeniz üniversite veyaa lise olmalıdır")
# else:
#      print("eliyet almanız için en az 18 yaşında olmanız lazım")



# yazılı1 = int(input("1.yazılı notu: "))
# yazılı2 = int(input("2.yazılı notu: "))
# sözlü = int(input("sözlü notu: "))

# yazılıort = (yazılı1+yazılı2) / 2
# genelort = (yazılıort+sözlü) / 2

# if 0<=genelort<=24:
#     print(f"sınav notunuz {genelort} üzerinden 0")
# elif 25<=genelort<=44:
#     print(f"sınav notunuz {genelort} üzerinden 1")
# elif 45<=genelort<=54:
#     print(f"sınav notunuz {genelort} üzerinden 2")
# elif 55<=genelort<=69:
#     print(f"sınav notunuz {genelort} üzerinden 3")
# elif 70<=genelort<=84:
#     print(f"sınav notunuz {genelort} üzerinden 4")
# elif 85<=genelort<=100 :
#     print(f"sınav notunuz {genelort} üzerinde  5")
# else:
#     print("yanlış bilgi girdiniz")



# import datetime
# #datetime modülü içe aktarılır. Bu modül tarih ve saatle ilgili işlemleri yapmaya yarar.
# #now değişkeni, o anki tarih ve saati alır.
# #now ile trafigeCikis arasındaki fark (gün olarak) hesaplanır ve fark değişkenine atanır
# #farka göre aracın servis aralığı yazdırılır


# history = input("aracınız hangi tarihte trafiğe çıktı (ör: 2019/09/11): ")
# history = history.split("/")   # split metodu ayırma işlemi yapıp listeye ekler (?)
# print (history)
# print (history[0])
# print (history[1])
# print (history[2])

# trafiğeçıkış = datetime.datetime(int(history[0]), int(history[1]), int(history[2]))
# now = datetime.datetime.now()
# print(trafiğeçıkış)
# print(now)
# fark = (now - trafiğeçıkış).days
# print (fark)

# if 0<=fark<=360 :
#     print("1. servis aralığı")
# elif  360<fark<=360*2 :
#     print("2. servis aralığı")
# elif  360*2<fark<=360*3 :
#     print("3. servis aralığı")
# else : print("yanlış tarih girdiniz")








# x = int(input("bir sayı gir: "))

# if 0<x<100 :
#     print("sayı 0 ve 100 arasında")
# elif x == 0:
#     print("sayı sıfıra eşit")
# elif x == 100:
#     print("sayı yüze eşit")
# else:
#     print("sayı 0 ve 100 arasında değil")



# x = int(input("bir sayı gir: "))
# if x%2==0 :
#     if x>0 :
#         print(f"{x} sayısı çift ve pozitif sayıdır")
#     else:
#         print(f"{x} sayısı çift ve negatif bir sayı")
# else:
#     if x>0 :
#         print(f"{x} sayısı pozitif tek sayı ")
#     else:
#         print(f"{x} sayısı negatif, tek bir tam sayıdır")



# x = int(input("bir sayı gir: "))
# y = int(input("bir sayı gir: "))
# z = int(input("bir sayı gir: "))

# if x>y>z or x>z>y:
#     print("x sayısı en büyük sayıdır")
# elif y>x>z or y>z>x:
#     print("y sayısı en büyük sayıdır")
# elif z>x>y or z>y>x:
#     print("z sayısı en büyük sayıdır")
# else :
#     print("girilen 3 sayı arasında en az ikisinde eşitlik vardır")



# vize1 = int(input("1. vize notunuzu girin: "))
# vize2 = int(input("2. vize notunuzu girin: "))
# final = int(input("final notunuzu girin: "))

# ort = ((vize1+vize2)/2)*0.6 + final*0.4

# if 100>=ort>=50:
#     if 100 >= final >= 50:
#          print(f"{ort} not ortalaması ile geçtiniz ")
#     else  :
#         print(f"ortalamanız: {ort} ancak final notunuz 50'den düşük olduğu için kaldınız")
# elif ort == 50 and 100>=final>=50:
#     print(f"{ort} not ortalaması ile geçtiniz ")
# elif 0<ort<50 and 100>=final>=70:
#     print(f"ortalamanız: {ort}, final notu 70 veya üzeri olduğu için geçtiniz ")
# elif 0<=ort< 50 :
#         print(f"{ort} not ortalaması ile kaldınız ")
# else:
#    print("notları yanlış girdiniz")



# x = (input("adınz:"))
# y = float(input("kilonuz:"))
# z = float(input("boyunuz:"))

# kiloindeksi = (y/z**2)

# if 0<=kiloindeksi<=18.4 :
#     print(f"{x} zayıfsın kilo alman gerek")
# elif 18.5<=kiloindeksi<=24.9:
#     print(f"{x} kilo durumun normal kilonu koru")
# elif  25<=kiloindeksi<=29.9:
#     print(f"{x} kilolusun zayıflaman gerek")
# elif 30<=kiloindeksi<=34.9:
#     print(f"{x} çok kilolusun acil kilo alman gerek")
# else : print("yanlış bilgi girdiniz")








# numbers = [1, 2, 3, 4, 5]

# for a in numbers:
#     print(a)

# for a in numbers:
#     print("DOĞAN DUMLU")


# names = ["DOĞAN ", "MAHİR ", "ENSAR ", "NEDİM ", "VAHAP"]
# for x in names :
#     print(f"my name is {x}")

# for x in names :
#     for y in x :
#         if y== " ":
#             print("")
#         else:
#             print(f"my name is {y}")


# name = "doğan dumlu".upper()
# for x in name:
#     print (x)


# tuble = [[1,2], (2,3), (3,4), (4,5), (5,6)]
# for x,y in tuble:
#     print(x,y)  #print(x) sadece 1 2 3 4 5 i yazdırırdı
# #               #print(y) ise sadece 2 3 4 5 6  yı yazdırırdı

# d = {"k1":1, "k2":2, "k3":3}
# for x in d:
#     print(x)

# d = {"k1":1, "k2":2, "k3":3}
# for x in d.items():
#     print(x)

# d = {"k1":1, "k2":2, "k3":3}
# for x,y in d.items():
#     print(x,y)









# numbers = [1,3,5,7,9,12,19,21]

# for x in numbers:
#     if x%3==0 :
#         print(x)



# t=0
# for x in numbers:
#     t += x
# print(t)



# for x in numbers:
#     if x%2 != 0:
#         print(x**2)



# sehirler = ["kocaeli", "istanbul" ,"ankara", "izmir", "rize"]

# for x in sehirler:
#     if len(x)<=5:
#         print(x)



# urunler = [{"name":"samsungs6", "price":"3000"}, {"name":"samsungs7", "price":"4000"}, {"name":"samsungs8", "price":"5000"}, {"name":"samsungs9", "price":"6000"}, {"name":"samsungs10", "price":"7000"}]

# t = 0
# for x in urunler:
#     for z,y in x.items():
#         if len(y) == 4:
#             t += int(y)
# print(t)
# #bunun diğer bir yolu ise
# t = 0
# for x in urunler:
#     t  += int(x["price"])
# print (t)



# for x in urunler:
#     for z,y in x.items():
#         if len(y) == 4:
#             if int(y) <= 5000:
#                 print(y)

# #bunun diğer bir yolu ise

# for x in urunler:
#     if  int(x["price"]) <= 5000:
#         print(x["name"])










# t = 1
# x = int(input("sayı gir:"))
# while 0<x:
#     t *= x
#     x -= 1
# print(t)



# x=0
# while x<100:
#     x += 1
#     if x%2==0:
#         print(x)
# print("bitti...")



# name = ""
# while not name.strip():       #strip boşluk girilirse sayılmamasını sağlıyor örn: ("  ")  karakterini ("") karakterine çevirir
#     name = input("isminizi girin: ")
# print(f"{name} iyki varsın")



# x=0
# numbers = [1,3,5,7,9,12,19,21]    #lan(numbers) = 8
# while x != len(numbers):
#     print(numbers[x])
#     x+=1

# #diğer bir versionu

# x=0
# numbers = [1,3,5,7,9,12,19,21]    #lan(numbers) = 8
# while True:
#     print(numbers[x])
#     x+=1
#     if x == 8:
#         break




# numbers = [1,3,5,7,9,12,19,21]

# x = int(input("1.sayıyı gir: "))
# y = int(input("2. sayıyı gir: "))

# t = 0
# ctrlz = []
# while t != len(numbers):
#     if numbers[t]%2==1:
#         if x<numbers[t]<y or y<numbers[t]<x :
#             ctrlz.append(numbers[t])
#             print(numbers[t])
#     t += 1
# print(ctrlz)



# x=100
# while 0 < x :
#     print(x)
#     x -= 1



# x=0
# y=[]
# while x<5:
#     t = int(input("sayı gir: "))
#     x+=1
#     y.append(t)
# print(y)

# y.sort()
# # y = y[::-1]
# # y.reverse()
# print(y)
# for t in y:
#     print(t)



# t = []
# x = int(input("kaç ürün giricekiniz?: "))
# y=0
# while 0 < x:
#     ürünname = input("ürünün adı:")
#     ürünprice = int(input(f"{ürünname} fiyatı:"))
#     t += [{"name":(ürünname), "price":(ürünprice)}]
#     x -= 1
# print(t)

# for a in t:
#     print(f"ürün adı: {a["name"]}    ürün fiyatı: {a["price"]}")

# #başka bir yolu

# t = []
# x = int(input("kaç ürün giricekiniz?: "))
# while 0 < x:
#     ürünname = input("ürünün adı:")
#     ürünprice = int(input(f"{ürünname} fiyatı:"))
#     t.append({
#         "name":ürünname,
#         "price":ürünprice
#     })
#     x -= 1

# for a in t:
#     print(f"ürün adı: {a["name"]}    ürün fiyatı: {a["price"]}")








# while True :
#     t = 1
#     x = int(input("sayı gir:"))
#     if x == 0:
#         print("0! 1'e eşittir")
#         break
#     while 0<x:
#         t *= x
#         x -= 1
#     print(t)










# x=0
# while x < 5:
#     if x==2 :
#         break
#     print(x)
#     x+=1

# x=0
# while x < 5:
#     x+=1
#     if x==2:
#         continue
#     print(x)




# x=0
# toplam = 0
# while x<100:
#     x += 1
#     if x%2==0:
#         continue
#     toplam += x
# print(toplam)



# range
# for x in range(0,5):
#     print(x)

# for x in range(10,60,10):
#     print(x)

# print(list(range(5,21,5)))


# #enumerate
# name = "DOĞAN"
# index = 0
# for x in name:
#     print (f"index: {index}   letter: {name[index]}")    #print (f"index:  {index} letter: {x}")
#     index += 1


# name = "DOĞANDUMLU   "
# for x in name:
#     print(x)


# for x in name:
#     if x == "N":
#         continue
#     print(x)


# for x in name:
#     if x == "N":
#         break
#     print(x)

# name = "DOĞAN"
# for x,y in enumerate(name):
#     print(f"index: {x}   letter: {y}")


# zip

# list1 = [1,2,3,4,5]
# list2 = ["a","b","c","d","e"]
# list3 = [100,200,300,400,500]
# print(list(zip(list1,list2,list3)))

# for x in zip(list1,list2,list3):
#     print(x)

# for x,y,z in zip(list1,list2,list3):
#     print(x,y,z)







# for x in range(4):
#     print(x)

# numbers = [x for x in range(50,9,-10)]
# print(numbers)

# #yada bu yolu deneriz

# numbers = []
# for x in range(50,9,-10):
#     numbers.append(x)
# print(numbers)



# numbers = [x**2 for x in range(2,11,2)]  #2,4,6,8,10 sayılarının karesini
# print (numbers)                          #alır ve listeye ekler

# numbers = [x*x for x in range(1,11,2) if x%3==0]   #1,3,5,7,9 sayıları arasında 3 ile tam bölünenlerin
# print (numbers)                                    #karesini alır yani 3 ve 9 un karesi 9 ve 81 dir



# mystring = "hello"
# mylist = []
# for t in mystring:
#     mylist.append(t)
# print(mylist)

# #yada bu yolu deneriz

# mylist = [t for t in mystring]
# print(mylist)



# years = [1983, 1980, 1984, 1973, 2005]
# ages = [2019 - x for x in years]
# print (ages)



# result = [x if x%2 != 0 else "çift" for x in range(1,11)]
# print(result)

# result= []
# for x in range(3):
#     for y in range(5,7):
#         result.append((x,y))
# print(result)

# #yada bu yolu deneriz

# numbers = [(x,y) for x in range(3) for y in range (5,7) ]
# print((numbers))

# numbers = [(x,y,z) for x in range(2) for y in range (2) for z in range(2) ]
# print((numbers))






# import random
# x = random.randint(1,100)

# hak = int(input("kaç hamlede bulursun?: "))
# t = 100/hak
# y = 100
# k = 0
# while 0<hak:
#     hak -= 1
#     k+=1
#     tahmin = int(input("tahmininizi girin: "))
#     if tahmin == x:
#         print(f"tebrikler buldunuz tahmin sayıs {x} idi: {k}. denemenizde buldunuz puanınız {y}")
#         break
#     else:
#         y -= t
#         if tahmin>x:
#             print("daha küçük bir sayı deneyiniz")
#         elif tahmin < x:
#             print("daha büyük bir sayı deneyiniz")
#     if hak==0:
#         print(f"malesef bulamadınız deneme sayısını aştınız :(\ntahmin edilicek sayı {x} idi")







# x = int(input("asalığını öğrenmek isteiğin sayıyı gir: "))
# t = x
# c=0
# while 2 < t:
#     t -= 1
#     if x%t == 0:
#         print(f"{x} sayısı asal değildir")
#         break
#     else:
#         c+=1
# if x == 1 :
#     print("1 sayısı asal değidir")
# if c == x - 2:
#     print(f"{x} sayısı asaldır")

# #bunun diğer biri yolu ise

# sayi = int(input('sayı: '))
# asalmi = True

# if sayi == 1:
#     asalmi = False

# for i in range(2, sayi):
#     if (sayi % i == 0):
#         asalmi = False
#         break

# if asalmi:
#     print('sayı asaldır.')
# else:
#     print('sayı asal değildir.')






# #method

list = [1,2,3, "mahir"]
# for i in range(4,6):
#     list.append(i)
# print(list)                #append listeye elaman ekler

# print(list.pop(3))
# print(list)        #pop listenin son elemanını silerr
# list.pop()         #ama eyer pop print içine yazılırsa listenin son elemanı yazılır
# print(list)

# name = "doğan"
# print(name.upper())        #upper methodu tüm karakterleri büyük harf yapar
# print(name.capitalize())   #capitalize methodu baş harfi büyük yapar diğer harfleri küçültür
# " "                        #bundan sonrakileri etkilemez yazdırmadan sonra doğan diye devam eder Doğan olmaz

# print(type(list))      #type listenin tipini gösterir (list, float, str, int)
# print(type(name))

# print(tuple(list))     #tuple methodu işlem gördüğü diziyi tupleye çevirir
# print(tuple(name))     #yani paranteze alır stringleri harflerini ayırarak tuple listesine ekler
# print([x   for x in tuple(name)])
# print([tuple(name)[i] for i in range(0,5,2)])





# def x():
#     print("DOĞAN")
# x()

# def x(surname = "DUMLU"):
#     print("DOĞAN", surname)
# x()
# x("ENSAR")

# def x(surname = "DUMLU"):
#     return ("DOĞAN", surname)
# y = x("MAHİR")
# print(y)



# def x(num1 = 5, num2 = 4):
#     print( num1 + num2)
# x()
# x(3,7)
# x(3)


# def x(num1 = 5, num2 = 4):
#     return num1 + num2
# print(x())
# t = int(input("1. sayı: "))
# m = int(input("2. sayı: "))
# print(x(t,m))



# def x(t):
#     from datetime import datetime
#     a = datetime.now().year - t
#     print(a)
# t = int(input("Doğum yılını gir: "))
# x(t)


# from datetime import datetime
# def x(t):
#     return (datetime.now().year - t)
# t = int(input("Doğum yılını gir: "))
# print(x(t))




# def x(t):
#     '''
#     DOCSTRİNG; fonksiyon girlen t(doğum yılı) ile yaşı hesaplanır
#     İNPUT; doğum yılı
#     QUTPUT; yaş bilgisi
#     '''
#     from datetime import datetime # t = doğum yılı
#     a = datetime.now().year - t   # a = yaş
#     print(a)
#     return a
# t = int(input("Doğum yılını gir: "))
# y = input("isminiz: ")
# # print(x(t))

# def emekli(t, y):
#     '''
#     DOCSTRİNG; x(t) fonksiyonundan aldığı yaş bilgisine göre
#     kişinin emeklikiğine ne kadar kaldığını gösterir
#     İNPUT; doğum yılı
#     QUTPUT; emekliliğe kaç yıl kaldı bilisi
#     '''
#     age = x(t)
#     emeklilik = 65 - age
#     if emeklilik>0:
#         print(f"{y} emekliliğne {emeklilik} yıl kaldı")
#     else:
#         print(f"{y} zaten emeklisin")

# emekli(t,y)
# print(help(x))
# print(help(emekli))

# list = [1,2,3]
# print(help(list.append))


# list = [1,2,-4,-8,-11,-23,3]
# t = [abs(x)      for x in list]
# print(t)



# def x(n):
#     n = "ada"
#     print(name)
# name = "yiğit"
# x(name)
# print(name)


# def x(n,t):
#     n[t] = "istanbul"
# list = ["ankara", "izmir", "muş"]
# print(list)
# x(list,2)
# print(list)

# list = ["ankara", "izmir", "muş"]
# n = list
# n[2] = "istanbul"
# print(list)

# list = ["ankara", "izmir", "muş"]
# n = list[:]    #slicinge
# n[2] = "istanbul"
# print(list)
# print(n)


# def x(n,t):
#     n[t] = "konya"            #liste değişmez
#     print(n[t])
#     print([list[:][t]])
# list = ["ankara", "izmir", "muş"]
# x(list[:],1)
# print(list)
# print(list[:])


# def add(a,b):
#     return sum((a,b))   #sum burda kullanılan bir methotur a ve b yi toplar
# print(add(3,4))

# def add(a,b):
#      c = sum((a,b))   #sum burda kullanılan bir methotur a ve b yi toplar
#      print(c)
# add(6,8)


# def add(a,b,c=0,d=0,e=0):
#     return sum((a,b,c,d,e))
# print(add(7,2))
# print(add(3,8,11))
# print(add(4,65,11,2,3))

# def add(*n):
#     print(type(n))
#     print(n)
#     print(n[3])
#     print(n[9])
#     return sum((n))
# print(add(1,2,3,4,5,6,7,8,9,10))

#toplama yapmak için sam ı kulanmak istemesek
# def add(*n):
#     x = 0
#     for t in n:
#         x += t
#     return x
# x = add(3,4,5,8)
# print(x)


# def x(**n):
#     print(type(n))
#     print(n)
#     print(n.items())
#     for a,b in n.items():
#         print(f"{a} is {b} ")
# x(name="doğan", age=19,citiy= "istanbul")


# def x(a,b,*n,**t):
#     print(a)
#     print(b)
#     print(n)
#     print(t)
# x(34, 49, "muş", "istanbul", "konya", name="doğan", surname="dumlu", age=19)
# x("muş", "istanbul", 49, 34, 61, name="doğan", surname="dumlu", age=19)


# list =[chr(i) for i in range(ord("a"), ord("e") + 1)]
# print(list)








# gonderilen_kelime = input("kelimeyi yaz: ")
# xkezyazdırma = int(input("girilen kelime kaç defa tekrar etsin: "))
# def kelime(y, x):
#     print((y)*x)
# kelime(gonderilen_kelime + "\n", xkezyazdırma)   #ikisindede sadece en altakine boşluk yazdırıyor anlamadım
# kelime(f"{gonderilen_kelime} \n", xkezyazdırma)


# def x(*a):
#     liste = []
#     for x in a:
#         liste.append(x)
#     print(liste)
# x(5,2,4,"altı","yedi")

# z=[]
# t = int(input("kaç parametre girmek istersin: "))
# sayaç = t
# while 0<t:
#     t -= 1
#     y = input(f"{(sayaç - (t))}. paremetreyi gir: ")
#     z.append(y)
# print(z)
# k = " ".join(z)
# print(k)
# x(k)



# def x(x,y):
#     z = []
#     if x<y:
#         for a in range(x+1,y):
#             b = 1
#             t = 0
#             c = a-2
#             while c > 0:
#                 c-=1
#                 b += 1
#                 if a%b != 0:
#                     t += 1
#             if t == (a - 2):
#                 z.append(a)
#         print(z)
#     if y<x:
#         for a in range(y+1,x):
#             b = 1
#             t = 0
#             c = a-2
#             while c > 0:
#                 c-=1
#                 b += 1
#                 if a%b != 0:
#                     t += 1
#             if t == (a - 2):
#                 z.append(a)
#         print(z)
# sayı1 = int(input("1.sayıyı gir:"))
# sayı2 = int(input("2.sayıyı gir:"))
# x(sayı1,sayı2)

#başkabir yolu

# def x(x,y):
#     z = []
#     for a in range (x+1,y):
#         if a > 1:
#             for i in range(2,a):
#                 if a%i == 0 :
#                     break
#             else:
#                 z.append(a)
#     print(z)
# sayı1 = int(input("1.sayıyı gir:"))
# sayı2 = int(input("2.sayıyı gir:"))
# x(sayı1,sayı2)



# def x(y):
#     z = []
#     for a in range(2,y+1):
#         if y%a == 0:
#             z.append(a)
#     print(z)
# y = int(input("bölenlerni bulmak istediğin sayı: "))
# x(y)







# def x(y):
#     return y**2
# y = int(input("sayı gir: "))
# print(x(y))


# def x(y):
#     return y**2
numbers = [1,2,3,5,8,9,11]
# print(list(map(x, numbers)))


# def x(y):
#     print(y**2)

# list(map(x, numbers))


# def x(y):
#     return y**2

# for a in map(x, numbers):
#     print(a)


# numbers = [1,2,3,5,8,9,11]
# x = list(map(lambda num: num**2, numbers))
# print (x)




# numbers = [1,2,3,5,8,9,11]
# square = lambda num: num**2
# x = list(map(square , numbers))
# print (x)


# square = lambda num: num**2
# print(square(7))


# numbers = [1,2,3,5,8,9,11]
# def x(t):
#     return t%2==0
# y = list(filter(x,numbers))
# print(y)


# numbers = [1,2,3,5,8,9,11]
# y = list(filter(lambda x: x%2==0, numbers))
# print(y)



# numbers = [1,2,3,5,8,9,11]
# y = list(filter(lambda x: x%2==0, numbers))
# print(y)


# resault = lambda x: x%2==0
# print(resault(7))
# print(resault(8))






# x = "global x"
# def t():
#     x = "local x"
#     print(x)
# t()
# print(x)


# x = "global x"
# def t():
#     print(x)
# t()
# print(x)


# name = "doğan"
# def x(t):
#     name = t
#     print(name)
# x("mahir")
# print(name)


# name = "global string"

# def x():
#     # name = "nedim"
#     def hello():
#         # name = "vahap"
#         print("hello " + name)
#     hello()
# x()



# x = 50
# def test(x):
#     print("x ", x)
#     x = 100
#     print (f"x sayısı {x} ile değiştirldi")
# test(10)
# print(x)


# x = 50
# def test():
#     global x
#     print("x :", x)
#     x = 100
#     print (f"x sayısı {x} ile değiştirldi")
# test()
# print(x)


# name = "doğan"
# def x(t):
#     global name
#     name = t
#     print(name)
# x("mahir")
# # print(name)



# doğanhesap = {
#     "ad": "Doğan Dumlu",
#     "hesap no":"0537642",
#     "bakiye":4000,
#     "ekhesap":2000
# }

# mahirhesap = {
#     "ad": "Mahir Dumlu",
#     "hesap no":"0536432",
#     "bakiye":1000,
#     "ekhesap":1250
# }


# def paracek(hesap,miktar):
#     print(f"Merhaba {hesap["ad"]}")
#     if hesap["bakiye"] >= miktar :
#         hesap["bakiye"] -= miktar
#         print("paranizi alabilirsiniz")
#         bakiyesorgula(hesap)
#     else:
#         toplam = hesap["bakiye"] + hesap["ekhesap"]
#         if toplam >= miktar :
#             a = input("bakiyeniz yetersiz ek hesap kulanılsınmı(e/h):?")
#             if a == "e" :
#                 hesap["ekhesap"] -= (miktar - hesap["bakiye"])
#                 hesap["bakiye"] = 0
#                 print("paranızı çekebilirsiniz")
#                 bakiyesorgula(hesap)
#             elif a == "h":
#                 print(f"{hesap["hesap no"]} nolu hesabınızda {hesap["bakiye"]} Tl bulunmaktadır")
#             else:
#                 print("e yada h karakterine basmanız gerekirdi")
#         else:
#             print("üzgünüm bakiyeniz yetersiz")
#             bakiyesorgula(hesap)


# def bakiyesorgula(hesap):
#     print(f"{hesap["hesap no"]} nolu hesabınızda {hesap["bakiye"]} Tl bulunmaktadır. ek hesap limitinit ise {hesap["ekhesap"]} Tl bulunmaktadır")

# hesap = 0
# while int(hesap) != 2 :
#     hesap = input("hangi hesapın para çekmek istersin? (doğanhesap(0),mahirhesap(1)): ")
#     y = int(input("ne kadar çekmek istersin?: "))

#     if hesap == "0":
#       paracek(doğanhesap, y)
#     elif hesap == "1":
#         paracek(mahirhesap, y)
#     else:
#         print(f"{hesap} adında bir hesap bulunmuyor")



# z = []
# b = 0
# for c in range(3):
#     c = input("yaz: ")
#     z.append(c)

# for a in z:
#     if a == "true":
#         a = bool(a)
#         if type(a)==type(x):
#             b += 1
#     if a == "false":
#         a = bool(a)
#         if type(a)==type(x):
#             b += 1
#     else:
#         continue
# print(b)




# while True:
#     print("eyşoo ",end="")
#     b += 1
#     if b==100:
#         break
