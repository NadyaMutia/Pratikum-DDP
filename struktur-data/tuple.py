# mendeklarasikan tuple dengan ()
 #tuple : soal

gorengan = ('bakwan', 'combro', 'misro')             #indeks 0
sop = ('sop iga', 'sop buntut', 'sop kaki')            #indeks 1
nasi = ('nasi uduk','nasi goreng', 'nasi rames')      #indeks 2

# tuple didalam tuple
makanan = (gorengan, sop, nasi)

# cetak gorengan aja

print(makanan[0])

for i in makanan[0] :
    print(i)

# cetak sop buntut

print(makanan[1][1])

# cetak nasi rames

print(makanan[2][2])

# cetak semua
for i in makanan:
    for semuamakanan in i :
        print(semuamakanan)