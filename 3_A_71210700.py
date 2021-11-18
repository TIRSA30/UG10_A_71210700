#test case 1, 2, 3
Peny = input("Mendatar/Menurun?: ")
if Peny == "Mendatar":
    n = int(input("Masukan kolom: "))
    print("#"*n)
elif Peny == "Menurun":
    n = int(input("Masukan baris: "))
    print("*\n"*n)
else: print("Pola tidak dikenali")
