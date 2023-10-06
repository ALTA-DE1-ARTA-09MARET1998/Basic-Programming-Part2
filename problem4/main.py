'''
Input Harga: 370000
Input Diskon: 15
Output: harga yang harus dibayar adalah Rp. 314.500
'''

import sys

harga = int(input("Masukkan harga: "))
diskon = int(input("Masukkan diskon: "))

harga_akhir = harga - (diskon / 100 * harga)

print("Harga yang perlu dibayar adalah Rp. ",harga_akhir)