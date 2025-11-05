### Sistem Manajemen Gudang Barang
Program ini merupakan aplikasi berbasis Python yang dirancang untuk membantu proses pencatatan dan pengelolaan barang di gudang. Sistem bekerja melalui Command Line Interface (CLI) dan menggunakan file CSV sebagai media penyimpanan data permanen.
Terdapat dua file CSV utama yang digunakan:
  1. data_barang_gudang.csv → menyimpan daftar barang yang ada di gudang.
  2. data_transaksi_gudang.csv → mencatat riwayat transaksi barang masuk dan keluar.
Program ini memungkinkan pengguna untuk menambah, menghapus, menampilkan, serta memperbarui data barang, sekaligus mencatat setiap transaksi keluar-masuk dengan tanggal otomatis.

### Gambaran Umum
Sistem ini berfungsi sebagai solusi sederhana untuk mengelola stok barang tanpa perlu menggunakan database yang kompleks. Data disimpan dalam format CSV (Comma-Separated Values) yang bisa dibuka langsung menggunakan aplikasi seperti Excel, Google Sheets, atau editor teks biasa.
Dengan sistem ini, pengguna dapat:
  1. Menambahkan barang baru ke gudang.
  2. Menghapus barang tertentu dari daftar.
  3. Melihat seluruh data barang yang tersedia.
  4. Melakukan transaksi masuk dan keluar stok barang, lengkap dengan pencatatan waktu transaksi.
Semua fungsi diatur melalui menu interaktif berbasis teks yang mudah digunakan, bahkan untuk pengguna pemula.

### Mekanisme Kerja Program
Pembacaan dan Penulisan Data CSV
Dua fungsi utama menangani proses I/O data, yaitu read_csv() dan simpan_csv().
Fungsi read_csv() membuka file CSV dan mengonversi setiap baris menjadi dictionary agar mudah diolah dalam Python. Jika file belum ada, fungsi ini otomatis mengembalikan list kosong agar program tetap berjalan normal.
Fungsi simpan_csv() menulis kembali seluruh data ke file CSV. Jika file baru dibuat, program akan otomatis menulis header kolom sebelum data disimpan. Dengan cara ini, file CSV tetap terstruktur dan dapat dibuka tanpa error.

### Menambahkan Barang ke Gudang
Fungsi menambahkan_barang_ke_gudang() memungkinkan pengguna memasukkan data baru seperti ID barang, nama barang, jumlah stok, dan kategori barang.
Sebelum data disimpan, sistem akan mengecek apakah ID barang sudah ada di dalam file CSV. Jika ada duplikasi, program akan menolak input tersebut untuk menghindari kesalahan data.
Apabila valid, data baru ditambahkan ke list, lalu disimpan ke file data_barang_gudang.csv.

### Menghapus Barang dari Gudang
Fungsi menghapus_barang_dari_gudang() digunakan untuk menghapus barang tertentu berdasarkan ID.
Program membaca seluruh data dari file CSV, lalu memfilter ulang semua barang kecuali yang memiliki ID yang ingin dihapus. Jika ID ditemukan, data baru yang sudah difilter disimpan ulang ke file. Jika tidak ditemukan, program akan menampilkan pesan bahwa barang tersebut tidak ada.

### Menampilkan Data Gudang
Fungsi menampilkan_data_pada_gudang() menampilkan seluruh daftar barang yang saat ini ada di gudang.
Program membaca file data_barang_gudang.csv, lalu mencetak setiap data dengan format rapi berisi ID, nama, jumlah, dan kategori.
Jika file kosong atau belum ada data, sistem menampilkan pesan “Tidak ada data barang di gudang.”

### Transaksi Barang Masuk dan Keluar
Fitur ini merupakan inti dari sistem. Fungsi menambahkan_transaksi_barang_masuk_dan_keluar() mencatat setiap aktivitas penambahan atau pengurangan stok.
Prosesnya dimulai dengan memasukkan ID barang untuk menentukan barang yang ingin diubah. Program kemudian menanyakan jenis transaksi, apakah masuk (penambahan stok) atau keluar (pengurangan stok).
Apabila transaksi bertipe masuk, jumlah stok ditambah sesuai nilai input.
Sebaliknya, jika bertipe keluar, stok akan dikurangi, dengan validasi bahwa jumlah stok di gudang mencukupi. Jika stok tidak cukup, program menolak transaksi untuk mencegah nilai negatif.
Setiap transaksi dicatat dalam file data_transaksi_gudang.csv dengan detail berikut:
  1. ID barang
  2. Nama barang
  3. Jumlah barang yang masuk/keluar
  4. Jenis transaksi (masuk atau keluar)
  5. Waktu transaksi otomatis (datetime.now())
Dengan pencatatan ini, pengguna dapat memantau riwayat aktivitas stok kapan saja melalui file CSV tersebut.

### Sistem Menu Utama
Seluruh fungsi di atas dijalankan dari menu interaktif melalui fungsi sistem_menu().
Menu ini ditampilkan secara berulang dalam loop agar pengguna dapat melakukan beberapa operasi tanpa perlu menjalankan ulang program.
Pilihan menu terdiri dari:
  1. Tambah Barang
  2. Hapus Barang
  3. Tampilkan Barang
  4. Transaksi Barang (Masuk/Keluar)
  5. Keluar Sistem
Ketika pengguna memilih opsi “Keluar Sistem”, program berhenti dengan aman setelah menyimpan seluruh perubahan data.

### Alur Logika Program
Ketika program dijalankan, Python mengeksekusi blok if __name__ == "__main__":, yang memanggil fungsi sistem_menu().
Dari sana, menu utama ditampilkan di terminal.
Setiap pilihan angka yang dimasukkan pengguna akan memanggil fungsi terkait.
Contohnya, jika pengguna memilih 1, maka fungsi menambahkan_barang_ke_gudang() akan dipanggil. Setelah selesai, pengguna akan kembali ke menu utama hingga memilih untuk keluar.
Alur kerja sederhana namun efisien ini membuat sistem mudah digunakan sekaligus terhindar dari error input berulang.

### Kesimpulan
Sistem Manajemen Gudang Barang ini menunjukkan bagaimana Python dapat digunakan untuk membangun aplikasi pengelolaan data yang efisien dan terstruktur tanpa database tambahan.
Melalui integrasi file CSV, program ini mampu menyimpan data secara permanen sekaligus tetap mudah diakses dan dimodifikasi.
Dengan struktur kode modular dan logika sederhana, sistem ini dapat dikembangkan lebih lanjut menjadi aplikasi inventori berskala lebih besar, seperti dengan penambahan fitur pencarian, pelaporan stok otomatis, hingga integrasi antarmuka berbasis web.
