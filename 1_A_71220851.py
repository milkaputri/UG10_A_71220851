#Soal 1
nama = str(input("Masukan nama mahasiswa :"))
nim = str(input("Masukan NIM-nya :"))
if nim [0:2]=="71" and int(nim[2:4])<=22 and int(nim [2:4]) >=20:
    print (f'{nama}, Merupakan mahasiswa informatika angkatan 20 hingga 22')
else:
    print (f'{nama}, bukan merupakan mahasiswa informatika angkatan 20 hingga 22')