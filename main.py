"""
Contact Management Program: View, Add, Delete, and Save Contacts.
"""


def melihat_data_kontak(path="data_kontak.txt"):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak


def menyimpan_kontak(path="data_kontak.txt", isi=()):
    with open(path, mode='w') as file:
        file.writelines(isi)


class Kontak:
    def __init__(self):
        self.kontak = melihat_data_kontak()

    def melihat_kontak(self):
        # melihat kontak
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}. ' + item)
        else:
            print("Kontak masih kosong")
            return 1

    def menambah_kontak(self):
        # menambah kontak
        nama = input("Masukkan nama kontak yang baru: ")
        hp = input("Masukkan no. HP yang baru: ")
        email = input("Masukkan alamat email yang baru: ")
        kontak_baru = f'{nama}, ({hp}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

    def menghapus_kontak(self):
        if self.melihat_kontak() == 1:
            return
        else:
            i_hapus = int(input(f"\nMasukkan nomor kontak yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak yang dimaksud sudah di hapus")

    def keluar_kontak(self):
        menyimpan_kontak(isi=self.kontak)


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
        kontak_kantor.keluar_kontak()
        break
    else:
        print('Anda memasukkan pilihan yang salah')
