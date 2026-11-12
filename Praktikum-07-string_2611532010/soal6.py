# Nama: Wafa Hindami
# NIM: 2611532010
# QUESTION 6

#pemanasan
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

#username kampus
full_name = "Wafa Hindami"
nim = "2611532010"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]
print(username)