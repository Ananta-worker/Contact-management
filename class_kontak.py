import dokumen


class Kontak:
    def __init__(self):
        self.kontak = dokumen.melihat_data_kontak()

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
        dokumen.menyimpan_kontak(isi=self.kontak)

