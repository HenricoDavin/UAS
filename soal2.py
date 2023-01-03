print ("===== Selamat datang di XXV =====")
tanggal = input ("Masukkan tanggal hari ini: ")

print ("== Berikut genre film yang tersedia ==")
print ("1. Horror")
print ("2. Action")

genre = input ("Silahkan pilih mau nonton film bergenre apa: ")
if genre == "1":
    print ("== Berikut pilihan film Horror ==")
    print ("1. The Devil's Light")
    print ("2. Pengabdi Setan")
elif genre == "2":
    print ("== Berikut pilihan film Action")
    print ("1. Black Panther: Wakanda Forever")
    print ("2. Avatar: The Way of Water")

film = input ("Silahkan pilih mau nonton film apa: ")
tiket = int(input ("Mau memesan tiket sebanyak: "))
if tanggal == "12":
    harga1 = tiket * 25000 - 2/100
    print ("Total yang harus dibayar adalah Rp.",harga1)
elif tanggal == "5":
    harga2 = tiket * 25000 - 5/100
    print ("Total yang harus dibayar adalah Rp.",harga2)


