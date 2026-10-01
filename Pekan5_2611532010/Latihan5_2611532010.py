# Latihan 5 membuat program untuk perulangan for (segitiga bintang)

tinggi_2010 = int(input("Masukkan tinggi segitiga: "))

for i_2010 in range(1, tinggi_2010 + 1):
    for j_2010 in range(tinggi_2010 - i_2010):
        print(" ", end="")
    for k_2010 in range(i_2010):
        print("* ", end="")
    print()