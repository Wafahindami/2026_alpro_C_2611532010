# Buat file dengan nama logika_2611532010.py
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Munculkan nilai boolean
# input tidak peka terhadap huruf besar dan huruf kecil
a1_2010 = input("input nilai boolean-1 (True/False): ") .strip().lower() == "True"
a2_2010 = input("input nilai boolean-2 (True/False): ") .strip().lower() == "False"

print("\nA1 =", a1_2010)
print("\nA2 =", a2_2010)

# Konjungsi: bernilai true jika keduanya true
hasil_2010 = a1_2010 and a2_2010
print("\nkonjungsi (and)")
print("A1 and A2 =", hasil_2010)

# Disjungsi: bernilai True jika salah satunya True
hasil_2010 = a1_2010 or a2_2010
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2010)

# Negasi A1: membalik nilai A1
hasil_2010 = not a1_2010
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_2010)

# Negasi A2: membalik nilai A2
hasil_2010 = not a2_2010
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_2010)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2010 = a1_2010 != a2_2010
print("\nDisjungsi Eklusif (XOR)")
print ("A1 XOR A2 =", hasil_2010)