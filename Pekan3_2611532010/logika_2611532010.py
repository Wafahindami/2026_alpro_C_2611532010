# Buat file dengan nama logika_2611532010.py
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Munculkan nilai boolean
# input tidak peka terhadap huruf besar dan huruf kecil
a1 = input("input nilai boolean-1 (True/False): ") .strip().lower() == "True"
a2 = input("input nilai boolean-2 (True/False): ") .strip().lower() == "False"

print("\nA1 =", a1)
print("\nA2 =", a2)

# Konjungsi: bernilai true jika keduanya true
hasil = a1 and a2
print("\nkonjungsi (and)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil = a1 or a2
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilai A1
hasil = not a1
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi A2: membalik nilai A2
hasil = not a2
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1 != a2
print("\nDisjungsi Eklusif (XOR)")
print ("A1 XOR A2 =", hasil)