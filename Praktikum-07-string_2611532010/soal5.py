# Nama: Wafa Hindami
# NIM: 2611532010
# QUESTION 5

# Bagian a
username = input("Username: ")
if len(username) < 5:
    print("invalid, at least 5 characters")
elif not username.isalnum():
    print("invalid, letters and digits only")
elif not username[0].isalpha():
    print("invalid, must start with a letter")
else:
    print(username)


#Bagian B
NIM = input("NIM: ")
if len(NIM) == 10 and NIM.isdigit():
    print("Valid, intake year 20" + NIM[:2])
else:
    print("Invalid Nim")
