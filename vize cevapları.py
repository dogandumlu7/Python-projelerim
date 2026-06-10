# print(len("merhaba"))




# tuple = (1,2,3,4,5)
# tuple.append("0")

# print(tuple)





# my_tuple = (1, 2, 3)
# print("Orijinal tuple:", my_tuple)

# Tuple'ın bir elemanını değiştirmeye çalışalım
# try:
#     my_tuple[1] = 4
# except TypeError as e:
#     print("Hata:", e)

# Tuple'a yeni bir eleman eklemeye çalışalım
# try:
#     my_tuple.append(5)
# except AttributeError as e:
#     print("Hata:", e)

# Tuple'dan bir eleman çıkarmaya çalışalım
# try:
#     my_tuple.remove(1)
# except AttributeError as e:
#     print("Hata:", e)





# def calculate_lcm(x, y):
#     # Büyük ve küçük sayıyı belirle
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if (greater % x == 0) and (greater % y == 0):
#             lcm = greater
#             break
#         else: greater += 1

#     return lcm

# # Kullanıcıdan iki pozitif tamsayı al
# num1 = int(input("Birinci sayıyı girin: "))
# num2 = int(input("İkinci sayıyı girin: "))

# print("OKEK:", calculate_lcm(num1, num2))



# def f(x,y):
#     if x>y:
#         ebob = y
#     else:
#         ebob = x
#     while True:
#         if x%ebob==0 and y%ebob==0:
#             break
#         else:
#             ebob -= 1
#     print(ebob)
#     return ebob

# num1 = int(input("Birinci sayıyı girin: "))
# num2 = int(input("İkinci sayıyı girin: "))
# f(num1,num2)




# n=5;
# for i in range(n):
#     for j in range(i):
#         print ('*', end="")
#     print('')
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*', end="")
#     print('')



# x = int(input("."))
# z=[]
# y = x
# while True:
#     y += 1
#     b = 0
#     for a in range(2,y):
#         if y%a!=0:
#             b +=1
#     if b == (y-2):
#         z.append(y)
#     if len(z)==5:
#         print(z)
#         break
    


# list= [1, 2, [3,4],[5,6]]
# z=[]
# c = 0
# for x in list:
#     if type(x) == type(z):
#         for a in x:
#             c += a
#     else :
#         c += x
# print(c)






# for i in range(50,0,-2):
#     print(i)

# t = 50
# while t > 0:
#     print(t)
#     t -= 2
    



# a = int(input("BİR SAYI GİR: "))
# x = 0
# for j in range(1,a+1,2):
#     for k in range(0,a+1,2):
#         x = x+j+k
# print(x)




# z = []
# x = [5, 4, 6, 14, 25]
# # print(len(set(x)))
# for a in x:
#     for b in x:
#         c = a-b
#         z.append(c)
# z.sort()
# while z[0]<=0:
#     z.pop(0)

# if len(x) == len(set(x)):
#     enkucuk = z[0]
# else:
#     enkucuk=0
# enbuyuk = z[len(z)-1]
# print (f"en büyük fark {enbuyuk}, en küçük fark {enkucuk}")




# z = []
# x = [5, 4, 6, 3, 276]
# # print(len(set(x)))
# for a in x:
#     for b in x:
#         c = a-b
#         z.append(c)
# z.sort()
# enbuyuk = z[len(z)-1]
# print (f"en büyük fark {enbuyuk}")







# x = 0
# b=0
# while x<75:
#     a = int(input(f"{x+1}. sayıyı gir: "))
#     x += 1
#     b += a
# print(b)


# x =int(input("sayıyı gir: "))
# x = str(x)
# x = tuple(x)
# b=0
# for a in range(0,len(x)):    
#     b += int(x[a])
# print(b)



# x =int(input("sayıyı gir: "))
# b=0
# while True:
#     b += x%10
#     x = x//10
#     if 1 == len(str(x)):
#         b+=x
#         break
# print(b)





# x = 5
# for i in range(x+1):
#   for j in range (x-1):
#     print(' ', end='')
#   for k in range(i):
#     print('*', end='')
#   print()





