### FITUR PERNCARIAN BUKU

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

pencarian = input("Masukan Judul Buku: ".lower())

ditemukan = False

for kategori, daftar in buku.items():
    for judul in daftar:

        if pencarian == judul.lower():
            print(f"Judul buku : {judul}")
            print(f"Kategori   : {kategori}")
            
            ditemukan = True
            
if ditemukan == False:
    print("Maaf buku yang anda cari belum ditambahkan!")            
