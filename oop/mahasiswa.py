class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    def welcome(self):
        print("halo", self.nama, "Di STT Terpadu Nurul Fikri")

    def lulus(self, nilai):
        if (nilai > 90):
            print("lulus")
        else:
            print("tidak lulus")

mhs1 = Mahasiswa("0110222295", "Nadya", "TI13")

mhs1.nama = "Nadya"
mhs1.nim = "0110222295"
mhs1.rombel = "TI13"

print("Nama mahasiswa :", mhs1.nama)
print("NIM mahasiswa :", mhs1.nim)
print("Rombel mahasiswa :", mhs1.rombel)
mhs1.lulus(96)
mhs1.welcome()
