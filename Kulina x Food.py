"""
Given an integer n can be inputted by Users. After the input is inputted, the program will show an
output in a form of an array of string, which will have the values with conditions:
● If the current integer is divisible by 3, change the integer to “Kulina” and then insert it
● If the current integer is divisible by 5, change the integer to “Food” and then insert it
● If the current integer is divisible by both 3 and 5, change the integer to “Kulina x Food’
and then insert it
● Otherwise, insert the integer in string form.
"""

"""
saya berasumsi bahwa parameter int n selalu lebih besar dari 0. apabila int n lebih kecil dari 0, maka fungsi akan mengembalikan array kosong.

output yang diharapkan dari fungsi ini adalah sebuah array dengan ukuran n yang berisikan string. python menggunakan zero based numbering, sedangkan output yang 
diminta dimulai dari angka 1. oleh karena itu saya membuat loop dengan index awal '1' sebanyak n+1 kali. selama loop berjalan, untuk mengetahui apakah integer i 
bisa dibagi dengan 3 dan atau 5, saya menggunakan operasi matematika modulo untuk mencari sisa dari pembagian integer i. apabila hasil modulo integer i adalah 0, 
maka string yang memenuhi syarat akan dimasukan ke dalam array. namun apabila hasil modulo integer i bukan 0, maka yang dimasukan ke dalam array adalah string
dari hasil operasi cast integer i menjadi string i.
"""
def kulinaXfood(n: int):
    result = []
    for i in range (1, n+1):
        if i%15 == 0:
            result.append("Kulina x Food")
        elif i%5 == 0:
            result.append("Food")
        elif i%3 == 0:
            result.append("Kulina")
        else:
            result.append(str(i))
    return result