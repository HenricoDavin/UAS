print ("========================================")
print ("*********** Justice League *************")
print ("========================================")

user = input("Masukan username anda: ")
if user == "brucewyne":
    print ("===== WELCOME ", user, ("====="))
    print ("1. Tambah Anggota Justice League")
    print ("2. Hapus Anggota Justice League")
    print ("3. Tampilkan Anggota Justice League")
    print ("4. Exit")
elif user == "victorstone":
    print ("===== WELCOME ", user, ("====="))
    print ("1. Tambah Anggota Justice League")
    print ("2. Hapus Anggota Justice League")
    print ("3. Tampilkan Anggota Justice League")
    print ("4. Exit")
elif user == "ciscoramon":
    print ("===== WELCOME ", user, ("====="))
    print ("1. Tambah Anggota Justice League")
    print ("2. Hapus Anggota Justice League")
    print ("3. Tampilkan Anggota Justice League")
    print ("4. Exit")
else: print ("Access denied")

task = input ("Masukan pilihan anda : ")
if task == "1":
    tambah = input ("Nama Anggota Baru : ")
    print ("data", tambah, "berhasil ditambahkan")
elif task == "2":
    hapus = input ("Anggota yang akan dihapus : ")
    print ("data", hapus, "berhasil dihapus")
elif task == "3":
    print
elif task == "4":
    print ("see u next time MR.", user, ", GLHF")

