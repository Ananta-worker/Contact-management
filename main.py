"""
Contact Management Program: View, Add, Delete, and Save Contacts.
"""

kontak1 = {'nama': "Andi", 'HP': '0812374646', 'email': 'Andi@gmail.com'}
kontak2 = {'nama': "Baba", 'HP': '0812379867', 'email': 'Baba@gmail.com'}
kontak = [kontak1, kontak2]

while True:
    print('\nMenu Kontak')
    print('1. Melihat Semua Kontak')
    print('2. Menambah Kontak Baru')
    print('3. Menghapus Kontak')
    print('4. Keluar dari Kontak')

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == "1":
        # melihat kontak
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')

    elif pilihan == "2":
        # menambah kontak
        nama = input("Masukkan nama kontak yang baru: ")
        HP = input("Masukkan no. HP yang baru: ")
        email = input("Masukkan alamat email yang baru: ")
        kontak_baru = {'nama':nama, 'HP':HP, 'email':email}
        kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")
    elif pilihan == "3":
        for num, item in enumerate(kontak, start=1):
            print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')

        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus: "))
        del kontak[i_hapus-1]
        print("Kontak yang dimaksud sudah di hapus")
    elif pilihan == "4":
        break
    else:
        print('Anda memasukkan pilihan yang salah')
