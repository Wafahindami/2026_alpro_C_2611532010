# Bonus? again thank you pak
number_of_rows = 4
seats_per_row = 5

# kode percobaan dibawha
seats =[]
for i in range(number_of_rows):
    seats.append(["."] * seats_per_row)

taken_count = 0

while True:
    for r in range(number_of_rows):
        row_str = f"Row {r + 1}: "
        for c in range(seats_per_row):
            row_str += " " + seats[r] [c]
        print(row_str)

    row_choice = int(input("Row (0 to stop): "))
    if row_choice == 0:
        break

    seat_choice = int(input("Seats: "))

    if row_choice < 1 or row_choice > number_of_rows or seat_choice < 1 or seat_choice > seats_per_row:
        print("invalid seat.")
    elif seats[row_choice - 1][seat_choice - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_choice - 1][seat_choice - 1] = "X"
        taken_count += 1
        print("Seat booked.")

print(f"Seats taken: {taken_count}")