import csv
from datetime import datetime

FILENAME = "data_barang_gudang.csv"
TRANSAKSI_FILENAME = "data_transaksi_gudang.csv"

def read_csv(file, fieldnames, delimiter=','):
    try:
        with open(file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=delimiter)
            next(reader) 
            return list(reader)
    except FileNotFoundError:
        return []

def simpan_csv(file, data, fieldnames, delimiter=','):
    try:
        with open(file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=delimiter)
            if f.tell() == 0: 
                writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Terjadi kesalahan saat menulis ke file {file}: {e}")

def menambahkan_barang_ke_gudang():
    barang = read_csv(FILENAME, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
    print("\nTambah Barang Baru")
    id_barang = input("Masukkan ID Barang: ")
    if any(item['ID_barang'] == id_barang for item in barang):
        print("Barang dengan ID ini sudah ada pada data gudang!")
        return

    nama_barang = input("Masukkan nama barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    kategori_barang = input("Masukkan kategori barang: ")

    barang.append({
        "ID_barang": id_barang,
        "Nama_barang": nama_barang,
        "Jml_barang": jumlah_barang,
        "Kategori_barang": kategori_barang
    })
    simpan_csv(FILENAME, barang, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
    print(f"Barang {nama_barang} berhasil ditambahkan!")

def menghapus_barang_dari_gudang():
    barang = read_csv(FILENAME, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
    print("\nHapus Barang dari Gudang")
    id_barang = input("Masukkan ID Barang yang ingin dihapus: ")
    barang_baru = [item for item in barang if item['ID_barang'] != id_barang]

    if len(barang_baru) == len(barang):
        print("Barang dengan ID tersebut tidak ditemukan!")
    else:
        simpan_csv(FILENAME, barang_baru, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
        print("Barang berhasil dihapus!")

def menampilkan_data_pada_gudang():
    barang = read_csv(FILENAME, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
    print("\n=== Data Barang Gudang ===")
    if not barang:
        print("Tidak ada data barang di gudang.")
        return
    for item in barang:
        print(f"ID: {item['ID_barang']}, Nama: {item['Nama_barang']}, Jumlah: {item['Jml_barang']}, Kategori: {item['Kategori_barang']}")

def menambahkan_transaksi_barang_masuk_dan_keluar():
    barang = read_csv(FILENAME, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])
    transaksi = read_csv(TRANSAKSI_FILENAME, ['ID_barang', 'Nama_barang', 'Jumlah', 'Jenis', 'Tanggal'])

    print("\nTransaksi Barang Masuk atau Keluar")
    id_barang = input("Masukkan ID Barang: ")
    item = next((item for item in barang if item['ID_barang'] == id_barang), None)

    if not item:
        print("Barang tidak ditemukan!")
        return

    jenis_transaksi = input("Masukkan jenis transaksi (masuk/keluar): ").lower()
    if jenis_transaksi not in ["masuk", "keluar"]:
        print("Jenis transaksi tidak valid!")
        return

    jumlah_transaksi_barang = int(input("Masukkan jumlah barang: "))
    if jenis_transaksi == "keluar" and int(item['Jml_barang']) < jumlah_transaksi_barang:
        print("Stok barang tidak mencukupi!")
        return

    if jenis_transaksi == "masuk":
        item['Jml_barang'] = str(int(item['Jml_barang']) + jumlah_transaksi_barang)
    else:
        item['Jml_barang'] = str(int(item['Jml_barang']) - jumlah_transaksi_barang)

    simpan_csv(FILENAME, barang, ['ID_barang', 'Nama_barang', 'Jml_barang', 'Kategori_barang'])

    transaksi.append({
        "ID_barang": id_barang,
        "Nama_barang": item['Nama_barang'],
        "Jumlah": jumlah_transaksi_barang,
        "Jenis": jenis_transaksi,
        "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    simpan_csv(TRANSAKSI_FILENAME, transaksi, ['ID_barang', 'Nama_barang', 'Jumlah', 'Jenis', 'Tanggal'])

    print(f"Transaksi {jenis_transaksi} berhasil! Barang ID: {id_barang}, Nama: {item['Nama_barang']}, Jumlah: {jumlah_transaksi_barang}")

def sistem_menu():
    while True:
        print("\n=== Sistem Gudang Barang ===")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Transaksi Barang (Masuk/Keluar)")
        print("5. Keluar Sistem")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menambahkan_barang_ke_gudang()
        elif pilihan == "2":
            menghapus_barang_dari_gudang()
        elif pilihan == "3":
            menampilkan_data_pada_gudang()
        elif pilihan == "4":
            menambahkan_transaksi_barang_masuk_dan_keluar()
        elif pilihan == "5":
            print("Keluar dari sistem.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    sistem_menu()
