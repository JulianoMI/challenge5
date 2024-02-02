print("Kode kota:")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuklinggau")
kota = int(input("Pilihan kota(1/2/3): "))
print("Kode kelas:")
print("4. Ekonomi")
print("5. Bisnis")      
print("6. Eksekutif")
kelas = int(input("Pilihan Kelas(4/5/6): "))
banyak_tiket = int(input("Banyak tiket?: "))

if kota == 1:  
    if kelas == 4:
        harga = 100000
    elif kelas == 5:
            harga = 400000
    elif kelas == 6:
            harga = 700000
elif kota == 2:
    if kelas == 4:
        harga = 200000
    elif kelas == 5:
            harga = 500000
    elif kelas == 6:
            harga = 800000
elif kota == 3:
    if kelas == 4:
        harga = 300000
    elif kelas == 5:
            harga = 600000
    elif kelas == 6:
            harga = 900000

print("_"*15)
if kota == 3 and kelas == 6:
    kode_promo = input("Kode Promo: ")
    if kode_promo == "igs":
        diskon = 0.10
else:
      diskon = 0

       
if kota == 2 and kelas == 4:
    kode_promo = input("Kode Promo: ")
    if kode_promo == "igs":
        diskon = 0.10
    else:
      diskon = 0

subTotal = harga * banyak_tiket
harga_diskon = subTotal * diskon
Total = subTotal - harga_diskon

print("Harga Tiket: ", harga)
print("Subtotal: ", subTotal)
print("Diskon: ", harga_diskon)
print("Total Bayar: ", Total)

