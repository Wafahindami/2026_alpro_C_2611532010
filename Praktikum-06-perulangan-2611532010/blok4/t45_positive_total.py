total = 0

while True:
    number = int(input("Masukkan angka: "))  
    if number < 0:
        break
    elif number == 0:
        continue
    print("Positive number:", number)
    total += number
print("Total:", total)