#buat dile dengan nama Boolean_NIM.py
#nama variabel ditambah 4 digit terakhir NIM contoh : Nilai_1234
#Deklarasi variabel dengan tipe data boolean
is_lulus_2010 = True
is_cumlaude_2010 = True

# menggunakan Boolean
Nilai_2010 = 85
batas_lulus_2010 = 75

# Menentukan nilai boolean dari kondisi
status_kelulusan = Nilai_2010 >= batas_lulus_2010 #hasilnya akan True

print("=== check kelulusan ===")
print("Nilai_2010?:", status_kelulusan)
if is_lulus_2010 and is_cumlaude_2010:
    print("selamat, anda lulus dengan predikat Cumlaude!")