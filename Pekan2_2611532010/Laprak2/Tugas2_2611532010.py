# Tugas 2 -  membuat program sederhana untuk menampilkan data praktikan dan hasil pemeriksaan kelulusan


import typing


BATAS_LULUS_2010: typing.Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2010 = input("Masukkan Nama Mahasiswa : ")
jk_2010 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2010 = int(input("Masukkan Umur : "))
skor_2010 = float(input("Masukkan Skor Tes Awal : "))

alamat_2010 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

token_2010 = 100 + 3j

status_lulus_2010 = skor_2010 >= BATAS_LULUS_2010

print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_2010, "| Tipe:", type(nama_2010))
print("Jenis Kelamin :", jk_2010, "| Tipe:", type(jk_2010))
print("Alamat Domisili:")
print(alamat_2010, "| Tipe:", type(alamat_2010))
print("Umur :", umur_2010, "tahun | Tipe:", type(umur_2010))
print("Skor Tes Awal :", skor_2010, "| Tipe:", type(skor_2010))
print("ID Token Sinyal:", token_2010, "| Tipe:", type(token_2010))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS_2010)
print("Apakah Dinyatakan Lulus?:", status_lulus_2010, "| Tipe:", type(status_lulus_2010))
