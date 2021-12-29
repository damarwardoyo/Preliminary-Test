"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M, which has the
values of:
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
For example, 2 is written as II in Roman numerals, just two one's added together. 12 is written as
XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral
for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we
subtract it making four. The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
● I can be placed before V (5) and X (10) to make 4 and 9.
● X can be placed before L (50) and C (100) to make 40 and 90.
● C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

"""
angka romawi menggunakan kombinasi dari tujuh simbol yang dimana masing-masing simbol memiliki nilai tertentu. struktur data dictionary dapat mempermudah kita untuk mengetahui 
nilai dari masing-masing simbol dengan cara menjadikan simbol sebagai key dan nilai dari simbol tersebut sebagai valuenya. cara menghitung angka romawi adalah dengan menjumlahkan 
nilai dari masing - masing simbol, dimulai dari kiri ke kanan. nilai simbol disebelah kiri biasanya lebih besar atau sama dengan nilai simbol disebelah kanannya, kecuali dalam 
beberapa kondisi tertentu. untuk memulai mengkonversi angka romawi menjadi integer, kita bisa mengecek masing masing simbol pada string s dari kiri ke kanan. namun ada kondisi 
khusus yang perlu diperhatikan, apabila nilai simbol pada posisi n lebih besar daripada posisi n-1 maka nilai simbol pada posisi n yang sebenarnya adalah (nilai simbol [n] - nilai simbol [n-1]). 
oleh karena itu, kita perlu menyimpan nilai simbol yang sudah dibaca ke variabel int prev supaya kita bisa mengecek apakah nilai simbol pada posisi n itu lebih besar daripada posisi n-1. 
secara default, nilai dari masing-masing simbol karakter ch pada string s akan dijumlah dengan int total. apabila terjadi kondisi dimana nilai simbol n lebih besar daripada nilai 
simbol n-1, cara mendapatkan nilai total yang sebenarnya adalah dengan menjumlahkan nilai total yang sudah dikoreksi dan nilai simbol pada karakter ch yang sebenarnya. untuk mengetahui 
nilai simbol pada karakter ch yang sebenarnya, kita mengurangi nilai simbol pada karakter ch dengan nilai karakter yang sebelumnya disimpan pada variabel int prev. lalu untuk mendapat 
nilai total yang sebenernya, nilai total perlu untuk dikurangi dengan nilai prev karena pada iterasi sebelumnya nilai prev sudah dijumlahkan ke nilai total. 
secara matematika bisa digambarkan sebagai berikut.

int total = (int total - int prev) + (int curr - int prev); 
int total = int total + int curr - int prev - int prev;
int total = int total + int curr - (2*int prev);

fungsi akan mengembalikan nilai int total apabila iterasi sudah selesai.
"""

def romanToInt(s: str):
    total = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    prev = 0
    for ch in s:
        curr = romans[ch]
        if curr > prev:
            total += curr - 2 * prev
        else:
            total += curr
        prev = curr
    return total