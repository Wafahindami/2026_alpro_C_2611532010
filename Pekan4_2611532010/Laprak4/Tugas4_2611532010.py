# === SISTEM LOKET ASTRA ADVENTURE PARK ===

# 1. Input Data Pengunjung & String Handling
nama_pengunjung_2010 = input("Masukkan Nama Pengunjung        : ")
umur_2010 = int(input("Input umur anda                  : "))
sim_2010 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

# Menu Paket Wahana di ASTRA Adventure Park
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_2010 = input("Masukkan nomor paket (1-5)      : ")

# 2. Pemilihan Wahana Menggunakan match-case
match paket_2010:
    case "1":
        nama_paket_2010 = "Wahana Safari Rimba"
        harga_satuan_2010 = 50000
    case "2":
        nama_paket_2010 = "Wahana Arung Jeram"
        harga_satuan_2010 = 75000
    case "3":
        nama_paket_2010 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2010 = 120000
    case "4":
        nama_paket_2010 = "Wahana Roller Coaster Kilat"
        harga_satuan_2010 = 100000
    case "5":
        nama_paket_2010 = "Wahana All-Access VIP"
        harga_satuan_2010 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

jumlah_tiket_2010 = int(input("Masukkan jumlah tiket            : "))

# Validation: IF Tunggal
if jumlah_tiket_2010 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    exit()

is_member_2010 = input("Apakah Anda member? (y/t)        : ").strip().lower()
kode_promo_valid_2010 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else / if-else
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_2010 == "3":
    if umur_2010 >= 17 and sim_2010 in ['y', 'ya']:
        print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_2010 >= 17 and sim_2010 not in ['y', 'ya']:
        print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
    elif umur_2010 < 17 and sim_2010 in ['y', 'ya']:
        print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
    else:
        print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
else:
    if umur_2010 >= 10:
        print("Status Akses: Pengunjung memenuhi batas usia minimum wahana.")
    else:
        print("Status Akses: Pengunjung belum memenuhi batas usia minimum wahana.")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_2010 = harga_satuan_2010 * jumlah_tiket_2010
total_diskon_persen_2010 = 0

if subtotal_2010 >= 200000:
    total_diskon_persen_2010 += 10

if is_member_2010 in ['y', 'ya']:
    total_diskon_persen_2010 += 5

if kode_promo_valid_2010 in ['y', 'ya']:
    total_diskon_persen_2010 += 15

if jumlah_tiket_2010 >= 5:
    total_diskon_persen_2010 += 5

# 5. Perhitungan & Evaluasi Audit Menggunakan if-else
nominal_diskon_2010 = subtotal_2010 * (total_diskon_persen_2010 / 100)
total_bayar_2010 = subtotal_2010 - nominal_diskon_2010

if total_bayar_2010 > 300000:
    catatan_layanan_2010 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2010 = "Terima kasih telah berkunjung."

# Tampilan Rincian Pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Nama Pengunjung  : {nama_pengunjung_2010}")
print(f"Umur             : {umur_2010} tahun")
print(f"Subtotal Belanja : Rp {subtotal_2010:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2010}% (Rp {nominal_diskon_2010:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2010:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2010}")
print("Program Selesai")