# =========================================================================
# Nama File : tugas3_2010.py
# Deskripsi : Sistem Simulasi Transaksi dan Validasi Akses Toko (Kasir)
# NIM       : 2010
# =========================================================================

print("=== SISTEM TRANSAKSI TOKO ===\n")

# 1. OPERATOR ASSIGNMENT & INPUT DATA
nama_2010 = input("Masukkan Nama Pelanggan : ")
status_2010 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_2010 = float(input("Masukkan Total Belanja : "))
jumlah_barang_2010 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2010 = input("Masukkan Kode Promo : ").strip().upper()

# 2. OPERATOR KEANGGOTAAN (MEMBERSHIP)
# Daftar promo resmi dari modul praktikum
daftar_promo_2010 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
promo_tersedia_2010 = kode_promo_2010 in daftar_promo_2010

# 3. OPERATOR PERBANDINGAN
syarat_belanja_2010 = total_belanja_2010 >= 200000
syarat_barang_2010 = jumlah_barang_2010 >= 3
is_member_2010 = status_2010 == "member"

# 4. OPERATOR LOGIKA
# Mendapatkan diskon jika dia member DAN total belanjanya memenuhi syarat
mendapat_diskon_2010 = is_member_2010 and syarat_belanja_2010
# Mendapatkan promo tambahan jika kode promo tersedia DAN jumlah barang memenuhi syarat
mendapat_promo_2010 = promo_tersedia_2010 or syarat_barang_2010

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan       :", nama_2010)
print("Status Pelanggan     :", status_2010)
print("Total Belanja        : Rp" + str(int(total_belanja_2010)))
print("Jumlah Barang        :", jumlah_barang_2010)
print("Kode Promo           :", kode_promo_2010)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000        :", syarat_belanja_2010)
print("Jumlah Barang >= 3         :", syarat_barang_2010)
print("Status Member              :", is_member_2010)
print("Kode Promo Tersedia        :", promo_tersedia_2010)
print("Mendapatkan Diskon         :", mendapat_diskon_2010)
print("Mendapatkan Promo          :", mendapat_promo_2010)

# 5. OPERATOR ARITMATIKA
# Menghitung nilai diskon (10% jika memenuhi syarat diskon)
diskon_2010 = total_belanja_2010 * 0.10 if mendapat_diskon_2010 else 0.0
total_pembayaran_2010 = total_belanja_2010 - diskon_2010

# Menghitung rata-rata harga barang
rata_rata_2010 = total_belanja_2010 / jumlah_barang_2010

# Menggunakan sisa bagi % sebagai syarat minimal instruksi aritmatika
sisa_bagi_2010 = int(total_belanja_2010) % jumlah_barang_2010

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                                : Rp" + str(int(diskon_2010)))
print("Total Pembayaran              : Rp" + str(int(total_pembayaran_2010)))
print("Rata-rata Harga Barang     : Rp" + str(int(rata_rata_2010)))

# 6. OPERATOR AUGMENTED ASSIGNMENT (PENUGASAN GABUNGAN)
poin_pelanggan_2010 = 0
if syarat_belanja_2010:
    poin_pelanggan_2010 += 50  # Menambahkan 50 poin secara langsung

# 7. OPERATOR IDENTITAS (IDENTITY)
# Membuat objek tiruan untuk membuktikan kesamaan nilai tetapi objek memori berbeda
total_duplikat_2010 = total_belanja_2010
total_kloning_2010 = float(str(total_belanja_2010))

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses             :", poin_pelanggan_2010)
print("Member Access              :", is_member_2010 is True)
print("Promo Access                 :", mendapat_promo_2010 is not False)
print("Free Shipping Access     :", kode_promo_2010 == "GRATISONGKIR")

# 8. OPERATOR BITWISE
# Inisialisasi bit biner berdasarkan kondisi (1 jika True, 0 jika False)
bit_member_2010  = 0b0001 if is_member_2010 else 0b0000
bit_belanja_2010 = 0b0010 if syarat_belanja_2010 else 0b0000
bit_barang_2010  = 0b0100 if syarat_barang_2010 else 0b0000
bit_promo_2010   = 0b1000 if promo_tersedia_2010 else 0b0000

# Menggabungkan bit menggunakan operator OR (|)
kode_status_biner_2010 = bit_member_2010 | bit_belanja_2010 | bit_barang_2010 | bit_promo_2010
kode_referensi_biner_2010 = 0b1011  # Kode acuan pembanding dari dosen

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner   : {format(kode_status_biner_2010, '04b')}")
print(f"Kode Desimal : {kode_status_biner_2010}")

print("=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_status_biner_2010, '04b')} & 0001")
hasil_and_member_2010 = kode_status_biner_2010 & 0b0001
print(f"Hasil Biner   : {format(hasil_and_member_2010, '04b')}")
print(f"Hasil Desimal : {hasil_and_member_2010}")

print("\nCek Promo")
print(f"{format(kode_status_biner_2010, '04b')} & 1000")
hasil_and_promo_2010 = kode_status_biner_2010 & 0b1000
print(f"Hasil Biner   : {format(hasil_and_promo_2010, '04b')}")
print(f"Hasil Desimal : {hasil_and_promo_2010}")

print("=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_status_biner_2010, '04b')}")
print(f"Kode Referensi : {format(kode_referensi_biner_2010, '04b')}")
print(f"{format(kode_status_biner_2010, '04b')} ^ {format(kode_referensi_biner_2010, '04b')}")
hasil_xor_2010 = kode_status_biner_2010 ^ kode_referensi_biner_2010
print(f"Hasil Biner   : {format(hasil_xor_2010, '04b')}")
print(f"Hasil Desimal : {hasil_xor_2010}")

print("=== Shift ===")
print(f"{format(kode_status_biner_2010, '04b')} << 1")
hasil_shift_2010 = kode_status_biner_2010 << 1
print(f"Hasil Biner   : {format(hasil_shift_2010, '05b')}")
print(f"Hasil Desimal : {hasil_shift_2010}")

print("\n=== SELESAI ===")
