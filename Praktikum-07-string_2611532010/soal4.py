# Nama: Wafa Hindami
# NIM: 2611532010
# QUESTION 4

phone = "082611532010"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)