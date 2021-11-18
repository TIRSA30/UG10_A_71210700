print("############################")
print("Kalkulator Advance Sederhana")
print("1. Menghitung sisa hasil bagi")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

Mis = int(input("Masukan menu yang anda pilih: "))
if Mis == 1:
    a = int(input("Masukan bilangan yang ingin dibagi: "))
    b = int(input("Masukan bilangan pembagi: "))
    c = int(a%b)
    print("Sisa hasil bagi",float(a),"dibagi dengan",float(b),"adalah",float(c))
elif Mis == 2:
    a = int(input("Masukan bilangan yang ingi dibagi: "))
    b = int(input("Masukan bilangan pembagi: "))
    c = int(round(a/b,1))
    print("Hasil pembagian",float(a),"dibagi dengan",float(b),"dibulatkan kebawah adalah",float(c))
elif Mis == 3:
    a = int(input("Masukan bilangan yang ingin dicari akar kubiknya: "))
    b = int(a**(1/3))
    print("Akar kubik dari",float(a), "adalah",float(b))
else:
    print("Menu yang anda pilih tidak tersedia")
    
    
