#skor pertandingan Sepak Bola test cas 1,2,3,4
artikel = input("Masukan artikel yang ingi dipindai: ")
klub = input("Masukan nama klub favorit anda: ")
skor = input("Masukan skor yang ingin dicari: ")

if klub in artikel and skor in artikel:
    print("Hasil pencarian ditemukan")
elif klub in artikel:
    print("Hanya",klub,"yang ditemukan pada artikel ini")
elif skor in artikel:
    print("Hanya",skor,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",klub,"dan",skor,"tidak ditemukan")
        
