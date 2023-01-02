# membuat list dengan menggunakan kurung siku
buah = ["mangga", "Melon", "Anggur", "Jeruk"]
 
print (buah[0])

# menambah list dengan append()
buah.append("Semangka")

print(buah)

# mengubah data list [indeks yangingin diubah] = nilaibaru
buah[1] = "Duku"

print(buah)

# menghapus list dengan del 
del buah[1]

print(buah)

# mengambil data yang akhir sekaligus menghapus => pop()

print(buah.pop())

# mengetahui jumlah data => len()
print(len(buah))

# Menyisipkan data sesuai indeks yang diinginkan dengan insert
buah.insert(1, "Duku")
print(buah)

# mengambil seluruh data menggunakan for
for i in buah :
    # aksi apa yg ingin dilakukan?
    print("buah",i)

