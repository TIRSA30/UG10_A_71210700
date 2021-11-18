#Pengujian input menu 1, 2, dan 3
R = float(input("Masukan nilai rata-rata UG anda: "))
T = float(input("Masukan nilai TTS anda:  "))
A = float (input("Masukan nilai TAS anda:  "))
print("=========================")
#Rumus
R1 = R*70/100
T1 = T*15/100
C1 = A*15/100
Peny = float(R1+T1+C1)
print("Nilai anda: ", Peny)
if Peny >= 85:
    print("Nilai huruf anda: A")
elif Peny >= 80:
    print("Nilai huruf anda: A-")
elif Peny >= 75:
    print("Nilai huruf anda: B+")
elif Peny >= 70:
    print("Nilai huruf anda: B")
elif Peny >= 65:
    print("Nilai huruf anda: B-")
elif Peny >= 60:
    print("Nilai huruf anda: C+")
elif Peny >= 55:
    print("Nilai huruf anda: C")
elif Peny >= 45:
    print("Nilai huruf anda: D")
else:
    print("Nilai huruf anda: E")

