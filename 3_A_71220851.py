#Soal 3
satu = int(input("Masukan nilai soal 1:"))
dua = int(input("Masukan nilai soal 2:"))
tiga = int(input("Masukan nilai soal 3:"))
umur = int(input("Masukan umur anda:"))
nilai1 = (satu*50/100)
nilai2 = (dua*30/100)
nilai3 = (tiga*20/100)
ratarata = (nilai1+nilai2+nilai3)
print ("Rata-rata nilai anda: "+str(ratarata))
if umur<=25:
    if ratarata>=80:
        print ("Selanat anda lulus!")
    else:
        print("Coba lagi tahun depan!")
else:
    if ratarata>=90:
        print("Selamat anda lulus!")
    else:
        print("Coba lagi tahun depan!")