import random
x = []
t = int(input("liste kaç elemanlı olsun?: "))
while 0<t:
    t-=1
    x.append(random.randint(1,100))
print(x)

z = []
for a in x:
    for b in x:
        z.append(a - b) 
# print(z)
z.sort()
# print(z)

while len(x) == len(set(x)):
    if z[0] <= 0:
        z.pop(0)
        if z[0]>0:
            print(z)
            print (f"listedeki sayıların farkalarının en büyük değeri: {z[len(z)-1]}")
            print (f"listedeki sayıların farkalarının en küçük pozitif değeri {z[0]}")
            break

if len(x) != len(set(x)):
    while z[0] < 0:
        z.pop(0)
        if z[0]>=0:
            z = list(set(z))
            print(z)
            print (f"listedeki sayıların farkalarının en büyük değeri: {z[len(z)-1]}")
            print ("listedeki sayıların farkalarının en küçük pozitif değeri 0")


    
