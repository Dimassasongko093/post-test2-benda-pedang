#imputan data benda
print("===mencari pedang===")
pedang=[]
list=[]

#string
pedang = input("Enter nama pedang :")
list.append(pedang)
warna = input("Enter warna pedang :")
list.append(warna)
logam = input("Enter jenis logam pedang :")
list.append(logam)
#integar
panjang = int(input("Enter panjang pedang :"))
list.append(panjang)
lebar = int(input("Enter lebar pedang  :"))
list.append(lebar)
#float
tahun = float(input("Enter tahun berapa pedang itu dibuat :")) 
list.append(tahun)
harga = float(input("Enter harga pedang :"))
list.append(harga)

print("===================================")
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print("jadi anda mencari pedang bernama",pedang, "berwarna",warna, "berjenis logam",logam,
"dengan panjang",panjang, "lebarnya",lebar, "ada sejak tahun",tahun, "dan berharga",harga)

print("===================================")
print("pedang :", pedang, "bertipe:", type(pedang))
print("warna :", warna, "bertipe:", type(warna))
print("logam :", logam, "bertipe:", type(logam))
print("panjang :", panjang, "bertipe:", type(panjang))
print("lebar :", lebar, "bertipe:", type(lebar))
print("tahun :", tahun, "bertipe:", type(tahun))
print("harga  :", harga,"tipe data :", type(harga))