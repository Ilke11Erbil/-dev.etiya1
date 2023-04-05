#degiskenler
baslik = "HABERİNİZ OLSUN"  #string
vade = 15  #integer
faizOrani1 = 1.47  #float
faizOrani2 = 1.44
faizOrani = 1.46

print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani1))

mesaj = "Hoşgeldin"
musteriAdi = "Engin"
musteriSoyadi = "Demiroğ"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"

print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)

print(sonucMesaj)
#degiskenler

#donguler
krediler =["Hızlı kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]
  

#alias
for kredi in krediler:
  print("<option>"+kredi+"<option>")


for i in range(len(krediler)):
  print(krediler[i])
  
for i in range(3,10):
  print(i)

for i in range(0,11,2):
  print(i)
#donguler

#sartbloklari
dolarDun = 7.65
dolarBugun = 7.75

if dolarDun > dolarBugun:
  print("Azalış oku")
  print("Bitti")
elif dolarDun < dolarBugun:
  print("Artış oku")
else:
  print("Eşittir oku")
print("bitti")
  
#if dolarDun < dolarBugun:
  #print("Artış oku")
  
#if dolarDun = dolarBugun:
  #print("Eşittir oku")
#sartbloklari

#listeler

krediler =["Hızlı kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]

print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])

print(len(krediler)) #lenght

krediler[0] = "Çabuk Kredi"
print(krediler)

def kredilerilistele():
 krediler =["Hızlı kredi","Maaşını Halkbank'tan alanlara özel", "Mutlu emekli ihtiyaç kredisi"]
 for kredi in krediler:
  print("<option>"+kredi+"<option>")


kredilerilistele()
kredilerilistele();
kredilerilistele();
kredilerilistele();
kredilerilistele();
kredilerilistele();
kredilerilistele();

#listeler