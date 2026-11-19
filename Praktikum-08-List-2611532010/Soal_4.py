# Harga Menu kantin  (in rupiah not dolar)
prices = [15000, 22000, 8000, 30000]
# buat discounted copy : diskonnya 2000 untuk setiap item
sale_prices = prices.copy()
for i in range(len(sale_prices)):
    sale_prices[i] = sale_prices[i] - 2000
# Naikkan harga normal setiap item 1000
for i in range(len(prices)):
    prices[i] = prices[i] + 1000
print("Normal:", prices)
print("Sale:", sale_prices)