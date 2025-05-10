'fungsi melihat dan menyimpan kontak'


def melihat_data_kontak(path="data_kontak.txt"):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak


def menyimpan_kontak(path="data_kontak.txt", isi=()):
    with open(path, mode='w') as file:
        file.writelines(isi)
