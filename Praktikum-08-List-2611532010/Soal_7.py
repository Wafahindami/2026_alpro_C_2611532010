# rekap penjualan kantin 
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# kode dibawah sini
for day in range(number_of_days):
    daily_sales = []
    for menu in menus:
        qty = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(qty)
    sales.append(daily_sales)

print("total per day: ")
for day in range(number_of_days):
    day_total = 0
    for col in range(len(menus)):
        day_total += sales [day][col]
    print(f"day {day + 1}: {day_total}")

menu_totals = []
for col in range(len(menus)):
    menu_sum = 0
    for day in range(number_of_days):
        menu_sum += sales[day][col]
    menu_totals.append((menus[col], menu_sum))

print("Total per menu:", menu_totals)

best_name, best_total = menu_totals[0]
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"best seller: {best_name} ({best_total})")