#Soal 2
print (("===== Selamat datang di Toko Andi Tersenyum, selamat belanja! ====="))
total = (int(input("Total belanja :Rp")))
if total <= 100000:
    print (f'Tidak ada diskon! Maka yang Anda bayarkan adalah :Rp.{total}')
elif total >= 100_000:
    print (f'Biaya yang harus dibayar setelah diskon adalah :Rp.{total-(0.02*total)}')
elif total >= 500_000:
    print (f'Biaya yang harus dibayar setelah diskon adalah :Rp.{total-(0.05*total)}')
elif total >= 1_000_000:
    print (f'Biaya yang harus dibayar setelah diskon adalah :Rp.{total-(0.1*total)}')