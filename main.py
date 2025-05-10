"""
Contact Management Program: View, Add, Delete, and Save Contacts.
"""
# kontak1 = {'nama': "Andi", 'HP': '0812374646', 'email': 'Andi@gmail.com'}
# kontak2 = {'nama': "Baba", 'HP': '0812379867', 'email': 'Baba@gmail.com'}
# kontak = [kontak1, kontak2]
class Kontak:
    def __init__(self):
        self.kontak=[]

    def melihat_kontak(self):
        # melihat kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak masih kosong")
            return 1


    def menambah_kontak(self):
        # menambah kontak
        nama = input("Masukkan nama kontak yang baru: ")
        hp = input("Masukkan no. HP yang baru: ")
        email = input("Masukkan alamat email yang baru: ")
        kontak_baru = {'nama': nama, 'HP': hp, 'email': email}
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")


    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input(f"\nMasukkan nomor kontak yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah di hapus")


kontak_kantor = Kontak()


while True:
    print('\nMenu Kontak')
    print('1. Melihat Semua Kontak')
    print('2. Menambah Kontak Baru')
    print('3. Menghapus Kontak')
    print('4. Keluar dari Kontak')

    pilihan = input("Masukkan pilihan menu kontak (1,2,3 atau 4): ")

    if pilihan == "1":
        kontak_kantor.melihat_kontak()

    elif pilihan == "2":
        kontak_kantor.menambah_kontak()

    elif pilihan == "3":
        kontak_kantor.menghapus_kontak()

    elif pilihan == "4":
        break
    else:
        print('Anda memasukkan pilihan yang salah')
