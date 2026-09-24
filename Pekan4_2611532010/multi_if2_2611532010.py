# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dan user
total_belanja_2010 = float(input("Input Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y atau 'ya')
input_member_2010 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_2010 = input_member_2010 in ["y", "ya"]

# Input satus kode promo (mengecek apakah user mengetik 'y atau 'ya')
input_promo_2010 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2010 = input_promo_2010 in ["y", "ya"]

total_diskon_persen_2010 = 0

# Multi-if terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2010 > 1000000:
    total_diskon_persen_2010 += 10  # Diskon total besar

if is_member_2010:
    total_diskon_persen_2010 += 5  # Diskon member

if kode_promo_valid_2010:
    total_diskon_persen_2010 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2010 = total_belanja_2010 * (total_diskon_persen_2010 / 100)
total_bayar_2010 = total_belanja_2010 - nominal_diskon_2010

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_2010} (Rp {nominal_diskon_2010:.0f})")
print(f"Total Bayar   : Rp {total_bayar_2010:.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_2010}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid