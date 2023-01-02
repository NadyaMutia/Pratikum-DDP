# # membuat dictionary menggunakan key : value
# data_diri = {'nama' : 'Nadya'}

# print(data_diri['nama'])

nilai = {'firda' : 89, 'inaya': 78, 'fawwas' : 90, 'rahmah' :75}

for i in nilai.values() :
    print(i)

for i in nilai.key() :
    print(i)

# mencetak key dan value menggunakan items()
for nama,skor in nilai.items() :
    print(nama,'=',skor)