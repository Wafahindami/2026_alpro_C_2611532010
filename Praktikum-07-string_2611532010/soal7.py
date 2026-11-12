# Nama: Wafa Hindami
# NIM: 2611532010
# QUESTION 7

name = "Wafa Hindami"
nim = "2611532010"
space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]
username = first_name.lower() + nim[-3:]
intake_year = "20" + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name      :' :<10} {name.title()}")
print(f"{'NIM       :' :<10} {nim}")
print(f"{'Username  :' :<10} {username}")
print(f"{'Intake    :' :<10} {intake_year}")
print("=" * 30)