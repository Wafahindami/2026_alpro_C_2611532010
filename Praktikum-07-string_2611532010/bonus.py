# Nama: Wafa Hindami
# NIM: 2611532010
# QUESTION bonus
# bonus horeee

sentence = input("Sentence: ")
clean = sentence.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")