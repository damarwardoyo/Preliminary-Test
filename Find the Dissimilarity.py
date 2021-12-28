"""
Find the difference between 2 string inputs (s and t). Both s and t are inputted by the User. String
t must be a shuffled string of String s. Return and print the letter that was added to t.
"""

"""
string t dianggap sah apabila string s merupakan subset dari string t. apabila s adalah string kosong dan t juga string kosong, maka tidak ada karakter yang ditambahkan pada 
string s untuk membuat string t. oleh karena itu kita bisa mengembalikan sebuah string kosong sebagai output dari fungsi ini. apabila t adalah string kosong atau panjang 
string t lebih kecil dari string s maka string t tidak valid. apabila string s adalah string kosong dan string t bukanlah string kosong dapat disimpulkan bahwa string t adalah 
sebuah string kosong yang ditambah n buah karakter. kumpulan karakter yang ditambakan ke string s sehingga terbentuk string t adalah string t itu sendiri. apabila string s dan t 
bukanlah string kosong, saya menggunakan dictionary untuk menemukan karakter apa saja yang ditambahkan ke string s, sehingga terbentuk string t. saya memilih dictionary karena 
saya bisa menyimpan masing masing karakter yang ada pada string s sebagai key dan frekuensi masing - masing karakter sebagai valuenya. setelah saya membuat dictionary untuk 
masing - masing karakter dari string s beserta frekuensinya, saya bisa mengecek apakah karakter ch yang ada pada string t ada di dictionary. apabila karakter ch tidak ada di 
dictionary, concat karakter ch dengan string diff. apabila karakter ch ada di dictionary, kurangi frekuensi karakter ch pada dictionary dengan 1. apabila karakter ch ada di 
dictionary namun frekuensinya 0, maka karakter ch pada string t lebih banyak jumlahnya dibandingkan pada string s. ini berarti karakter ch merupakan karakter tambahan, concat 
karakter ch ke string diff. setelah iterasi selesai, fungsi akan nge-print string diff.
"""

def findTheDifference(s: str, t: str):
    diff = ""

    if len(s) == 0 and len(t) == 0:
        print(diff)
    elif len(t) == 0 or len(t)<len(s):
        print("Input tidak valid!")
    elif len(s) == 0:
        print(t)
    else:
        dictn = {}
        for ch in s:
            if dictn.get(ch) != None:
                dictn[ch]+=1
            else:
                dictn[ch] = 1

        for ch in t:
            if dictn.get(ch, 0) == 0:
                diff+=ch
            elif dictn[ch] > 0:
                dictn[ch] -= 1
        
        print(diff)