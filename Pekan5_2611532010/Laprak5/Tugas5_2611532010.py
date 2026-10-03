# === PROGRAM JAM PASIR KRISTAL PALINDROMIK ===

# Input ukuran skala jam pasir N
n_2010 = int(input("Masukkan ukuran skala jam pasir (N): "))

# 1. BORDER ATAS
print("#", end="")
for i_2010 in range(4 * n_2010 + 5):
    print("=", end="")
print("#")

# 2. FASE 1: JAM PASIR ATAS (Baris N turun ke 1)
for baris_2010 in range(n_2010, 0, -1):
    # Dinding kiri
    print("| ", end="")
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_2010 in range(2 * (n_2010 - baris_2010)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1
    for angka_2010 in range(baris_2010, 0, -1):
        print(angka_2010, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris
    for angka_2010 in range(1, baris_2010 + 1):
        print("", angka_2010, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_2010 in range(2 * (n_2010 - baris_2010)):
        print(" ", end="")
        
    # Dinding kanan
    print(" |")

# 3. FASE 2: POROS TITIK PUSAT (SINGULARITY)
print("|", end="")

# Spasi penyeimbang kiri: 2 * N + 1
for spasi_2010 in range(2 * n_2010 + 1):
    print(" ", end="")

# Poros kristal tunggal
print("<*>", end="")

# Spasi penyeimbang kanan: 2 * N + 1
for spasi_2010 in range(2 * n_2010 + 1):
    print(" ", end="")

print("|")

# 4. FASE 3: JAM PASIR BAWAH (Baris 1 naik ke N)
for baris_2010 in range(1, n_2010 + 1):
    # Dinding kiri
    print("| ", end="")
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_2010 in range(2 * (n_2010 - baris_2010)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1
    for angka_2010 in range(baris_2010, 0, -1):
        print(angka_2010, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris
    for angka_2010 in range(1, baris_2010 + 1):
        print("", angka_2010, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_2010 in range(2 * (n_2010 - baris_2010)):
        print(" ", end="")
        
    # Dinding kanan
    print(" |")

# 5. BORDER BAWAH
print("#", end="")
for i_2010 in range(4 * n_2010 + 5):
    print("=", end="")
print("#")