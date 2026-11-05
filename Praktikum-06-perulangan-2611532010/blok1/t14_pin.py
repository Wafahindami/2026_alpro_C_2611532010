#Mengurutkan kode acak dari A sampai K
Correct_pin = "1234"
MAX_ATTEMPTS = 3
attempts = 1

Pin = input("enter your pin:")
while Pin != Correct_pin and attempts <  MAX_ATTEMPTS:
    print("Incorrect PIN: ")
    if Pin == Correct_pin:
        attempts += 1

Pin = input("Enter PIN: ")
if Pin == Correct_pin:
        print("Access granted")
else:
        print("Account locked")

