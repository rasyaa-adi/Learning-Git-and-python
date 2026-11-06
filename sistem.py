buku = {
    "Pendidikan": [
        " Fisika Dasar",
        " Matematika Diskrit",
        " Kalkulus",
        " Pendidikan Pancasila"
    ],

    "Novel": [
        "Home Sweet Loan",
        "Laut Bercinta",
        "Intermezzo"
    ],

    "Sejarah": [
        "Sejarah Indonesia"
    ],
}

### DI BAWAH INI UNTUK MENGECEK STATUS BUKU
dipinjam = {}   # {judul: nama_peminjam}

def cari_buku(judul):
    for kategori, daftar in buku.items():
        for b in daftar:
            if b.lower() == judul.lower():
                return b  # mengembalikan judul asli
    return None


### FITUR PEMINJAMAN
def pinjam_buku(judul, nama):
    asli = cari_buku(judul)
    if asli is None:
        print("Buku tidak ditemukan. ")
    elif asli in dipinjam:
        print(f"'{asli}' Buku sedang dipinjam {dipinjam[asli]}.")
    else:
        dipinjam[asli] = nama
        print(f"'{nama}' Berhasil meminjam '{asli}'.")


### FITUR PENGEMBALIAN
def kembalikan_buku(judul):
    asli = cari_buku(judul)
    if asli is None:
        print("Buku tidak ditemukan.")
    elif asli not in dipinjam:
        print(f"'{asli}' Tidak sedang dipinjam.")
    else:
        nama = dipinjam.pop(asli)
        print(f"'{asli}' Dikembalikan oleh {nama}.")

### TAMPILKAN DAFTAR BUKU
def tampilkan_buku():
    print("\n==== Daftar Buku ====")
    for kategori, daftar in buku.items():
        print(f"\n[{kategori}]")
        for b in daftar:
            if b in dipinjam:
                status = f"Dipinjam oleh {dipinjam[b]}"
            else:
                status = "Tersedia"
            print(f"- {b} ({status})")


### MENU PAKAI
def menu():
    while True:
        print("\n==== PERPUSTAKAAN DIGITAL ====")
        print("1. Lihat daftar buku")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Keluar")

        pilihan = input("Pilih menu antara (1-4): ")

        if pilihan == "1":
            tampilkan_buku()
        elif pilihan == "2":
            nama = input("Nama peminjam: ")
            judul = input('Judul buku: ')
            pinjam_buku(judul, nama)
        elif pilihan == "3":
            judul = input("Judul buku yang ingin dikembalikan: ")
            kembalikan_buku(judul)
        elif pilihan == "4":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

menu()