## KATEGORI BUKU

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

print("==== Kategori & Daftar Buku ====")

for kategori, daftar in buku.items ():
    print(f"\nKategori: {kategori}")

    for nomor, judul in enumerate(daftar, start=1):
        print(f"{nomor}. {judul}")